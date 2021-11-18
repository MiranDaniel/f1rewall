# How to set up the Cloudflare tunnel to host your gateway

**Warning: this method requires you to change your domain namesevers to Cloudflare**

Cloudflare tunnel is an easy way to host your gateway on a subdomain (ex. chat.<>.<>)

## Cloudflare docs

1. https://support.cloudflare.com/hc/en-us/articles/201720164-Creating-a-Cloudflare-account-and-adding-a-website
2. https://support.cloudflare.com/hc/en-us/articles/205195708
3. https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/tunnel-guide

## Notes
When setting up your tunnel, it's application localhost post has to match your preconfigured port in config.yaml!
