# Instructions

A Helm chart to deploy LFH FHIR server with cert-manager and K8s secret store and connect to CloudSQL (postgres)

## Installation

`helm dep up`

`helm upgrade --install fhir-server . --namespace fhir-server --create-namespace -f <VALUES YAML>`

## NOTE

The Let's Encrypt production issuer has very strict rate limits (5 times in 1 week). Hence, when you're experimenting, please use the URL https://acme-staging-v02.api.letsencrypt.org/directory in `spec.acme.server` in `templates/cert-issuer.yaml` file. When it is ready for production, replace the URL with https://acme-v02.api.letsencrypt.org/directory instead.

## Testing

Staging: `curl -v --insecure https://fhir.enduesoftware.com`

Prod: `curl -v https://fhir.enduesoftware.com`
