from google.api_core.client_options import ClientOptions
from google.cloud import documentai
import pandas as pd
from collections import defaultdict

# project_id = 'YOUR_PROJECT_ID'
# location = 'YOUR_PROCESSOR_LOCATION' # Format is 'us' or 'eu'
# processor_id = 'YOUR_PROCESSOR_ID' #  Create processor before running sample
# file_path = '/path/to/local/pdf'
# mime_type = 'application/pdf' # Refer to https://cloud.google.com/document-ai/docs/file-types for supported file types

def parser(project_id: str, location: str, processor_id: str, file_path: str, mime_type: str):
    # You must set the api_endpoint if you use a location other than 'us', e.g.:
    opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    client = documentai.DocumentProcessorServiceClient(client_options=opts)

    # The full resource name of the processor, e.g.:
    # projects/project_id/locations/location/processor/processor_id
    processor_name = client.processor_path(project_id, location, processor_id)

    # Read the file into memory
    with open(file_path, "rb") as file:
        file_content = file.read()

    # Load Binary Data into Document AI RawDocument Object
    raw_document = documentai.RawDocument(content=file_content, mime_type=mime_type)

    # Configure the process request
    request = documentai.ProcessRequest(name=processor_name, raw_document=raw_document)
    result = client.process_document(request=request)

    # For a full list of Document object attributes, please reference this page:
    # https://cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.Document
    return result.document.text





def extract_info(parsed_text, filename):
    parsed_text = parsed_text.split('\n')
    field_dict = defaultdict(set)
    field_dict = {'PATIENT DEMOGRAPHICS': {'PATIENT NAME', "PATIENT'S CONTACT #", 'DATE OF BIRTH', 'DATE OF REFERRAL',
                                           'ADDRESS', 'CITY, STATE, ZIP'},
                  'PRESCRIBER INFORMATION': {'PROVIDER NAME', 'OFFICE CONTACT', 'PHONE', 'FAX', 'EMAIL',
                                             'ADDRESS', 'CITY, STATE, ZIP'}
                 }

    tab_list = []; info_list = []; df_col_list = []; df_info_list = []
    for text in parsed_text:
        field = ''
        for i in range(len(text)):
            field += text[i].upper()
            if field in field_dict:
                if df_info_list:
                    info_list.append([df_col_list, df_info_list])
                    df_col_list = []; df_info_list = []
                tab_list.append(field)
                break
            else:
                if tab_list and field in field_dict[tab_list[-1]]:
                    info = text[i+3:]
                    if info:
                        df_col_list.append(field)
                        df_info_list.append(info)
                        break
    if df_info_list: info_list.append([df_col_list, df_info_list])


    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        for i in range(len(tab_list)):
            info_df = pd.DataFrame()
            for j in range(len(info_list[i])):
                info_df[df_col_list[j]] = info_list[i][j]
            info_df.to_excel(writer, sheet_name=tab_list[i].lower(), index=False)




    


if __name__ == '__main__':
    project_id = 'minh-sandbox'; location = 'us'; processor_id = '6d371b3eb63ff1a2'
    file_path = './example-form1.pdf'; mime_type = 'application/pdf'

    parsed_text = parser(project_id, location, processor_id, file_path, mime_type)
    filename = 'referral_info.xlsx'
    extract_info(parsed_text, filename)