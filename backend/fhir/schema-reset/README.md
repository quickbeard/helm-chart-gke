# Instructions

A Helm chart to drop and recreate schemas in FHIR postgres DB in CloudSQL.

## Installation

`helm dep up`

`helm upgrade --install schema-reset . --namespace fhir-server --create-namespace`
