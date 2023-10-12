# Instructions

This Helm chart installs External Secrets Operator (https://external-secrets.io)

## Installation ##

`helm dependencies update`

`helm upgrade --install external-secrets . --namespace external-secrets --create-namespace`