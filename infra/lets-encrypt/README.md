# Instructions

This Helm chart deploys Cluster Let's Encrypt issuer.

## Installation

`helm upgrade --install cluster-lets-encrypt . --namespace cert-manager --create-namespace -f <VALUES YAML>`

## NOTE

The Let's Encrypt production issuer has very strict rate limits (5 times in 1 week). Hence, when you're experimenting, please use the URL https://acme-staging-v02.api.letsencrypt.org/directory in `spec.acme.server` in `templates/cert-issuer.yaml` file. When the webapp is ready for production, replace it with https://acme-v02.api.letsencrypt.org/directory instead.
