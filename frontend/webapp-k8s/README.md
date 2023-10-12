# Instructions

This Helm chart deploys Endue webapp.

## Installation

`helm upgrade --install webapp . --namespace webapp --create-namespace -f <VALUES YAML>`

If you don't want to use the `latest` tag, you can use `--set` to set to another tag (first 8 characters of HEAD githash):

`helm upgrade --install webapp . --namespace webapp --create-namespace --set image.tag=<DOCKER_IMAGE_TAG> -f <VALUES YAML>`

## NOTE

The Let's Encrypt production issuer has very strict rate limits (5 times in 1 week). Hence, when you're experimenting, please use the URL https://acme-staging-v02.api.letsencrypt.org/directory in `spec.acme.server` in `templates/cert-issuer.yaml` file. When the webapp is ready for production, replace it with https://acme-v02.api.letsencrypt.org/directory instead.

## Testing

Staging: `curl -v --insecure https://app.enduesoftware.com`

Prod: `curl -v https://app.enduesoftware.com`
