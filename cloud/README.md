# Nebulous serverless app demonstrating use of Google Cloud APIs
### Featuring the Cloud Translation API

## Description

This is the code repo for a set of codelab tutorials highlighting a ["nebulous" sample app](https://twitter.com/googledevs/status/1433113274984271875?utm_source=twitter&utm_medium=unpaidsoc&utm_campaign=CDR_wes_aap-serverless_mgrcrbdpk_sms_201031&utm_content=-) demonstrating how to access Google Cloud APIs from one of our serverless platforms. There are [Python](python) and [Node.js](nodejs) versions of this app available.


## Inspiration and implementation

This code sample was inspired by a [user's suboptimal experience](https://www.mail-archive.com/google-appengine@googlegroups.com/msg94549.html) trying to create a simple App Engine app using a Cloud API. It was also inspired by a [colleague's blog post](https://dev.to/googlecloud/portable-code-migrating-across-google-cloud-s-serverless-platforms-2ifk) showing a similar Node.js example "drifting" between GCP serverless platforms.

This app shows developers how to use the [Cloud Translation API](https://cloud.google.com/translate), the API for [Google Translate](https://translate.google.com), and one of GCP's [AI/ML "building block" APIs](https://web.archive.org/web/20210308144225/https://cloud.google.com/products/ai/building-blocks). Such APIs are backed by pre-trained machine learning models, allowing developers with little or no background in AI/ML to leverage machine learning with only API calls. The application implements a mini Google Translate "MVP" (minimally-viable product) web service.


## Authentication and authorization: service account credentials (local deployments only)

Google Cloud compute platforms feature [default service account credentials](https://cloud.google.com/iam/docs/service-accounts#default) which are used for these app deployments. However, such credentials are not available when running locally, so users will need to **run** `gcloud auth application-default login` before starting the server.


## Cost

While the Translation API does not explicitly list a free quota on the ["Always Free" tier page](https://cloud.google.com/free/docs/gcp-free-tier#free-tier-usage-limits), its [pricing page](https://cloud.google.com/translate/pricing#charged-characters) indicates a certain number of [translated characters](https://cloud.google.com/translate/pricing#charged-characters) as a free monthly quota applied as a credit, so long as you stay within that limit, you should not incur any additional charges.


## Enable Google Cloud services used

Once you have a billing account, you can enable the services/APIs for each product used. Go to the Cloud console pages for each respective Cloud product used and enable the service:

1. [App Engine](https://console.cloud.google.com/appengine)
1. [Cloud Functions](https://console.cloud.google.com/functions)
1. [Cloud Run](https://console.cloud.google.com/run)
1. [Cloud Translation](https://console.cloud.google.com/apis/api/translate.googleapis.com)

Alternatively, you use the [`gcloud` CLI (command-line interface)](https://cloud.google.com/sdk/gcloud) available from the [Cloud SDK](https://cloud.google.com/sdk). Review the [Cloud SDK install instructions](https://cloud.google.com/sdk/docs/quickstart) if needed. New users should also reference the [`gcloud` cheatsheet](https://cloud.google.com/sdk/docs/cheatsheet).

Enable all 4 services with this one `gcloud` command: `gcloud services enable translate.googleapis.com run.googleapis.com cloudfunctions.googleapis.com appengine.googleapis.com`


## The application itself

The app consists of a simple web page prompting the user for a phrase to translate from English to Spanish. The translated results along with the original phrase are presented along with an empty form for a follow-up translation if desired.

This is what the app looks like after completing one translation (Cloud Run version):

![app screenshot](https://user-images.githubusercontent.com/1102504/133918482-fc66d512-aeb7-4982-bcd2-75794cd21349.png)


## References

1. Google Cloud serverless product pages
    - App Engine
        - [App Engine home page](https://cloud.google.com/appengine)
        - [App Engine documentation](https://cloud.google.com/appengine/docs)
        - [Default service accounts](https://cloud.google.com/appengine/docs/standard/nodejs/service-account)
    - Cloud Functions
        - [Cloud Functions home page](https://cloud.google.com/functions)
        - [Cloud Functions documentation](https://cloud.google.com/functions/docs)
        - [Default service accounts](https://cloud.google.com/functions/docs/concepts/iam#access_control_for_service_accounts)
    - Cloud Run
        - [Cloud Run home page](https://cloud.run)
        - [Cloud Run documentation](https://cloud.google.com/run/docs)
        - [Default service accounts](https://cloud.google.com/run/docs/securing/service-identity)

1. Cloud SDK and `gcloud` product pages
    - [Cloud SDK](https://cloud.google.com/sdk)
    - [Cloud SDK installation](https://cloud.google.com/sdk/docs/quickstart)
    - [`gcloud` CLI](https://cloud.google.com/sdk/gcloud) (command-line interface)
    - [`gcloud` cheatsheet](https://cloud.google.com/sdk/docs/cheatsheet)

1. Cloud build-relevant product pages
    - [Cloud Buildpacks announcement](https://cloud.google.com/blog/products/containers-kubernetes/google-cloud-now-supports-buildpacks)
    - [Cloud Buildpacks repo](https://github.com/GoogleCloudPlatform/buildpacks)
    - [Cloud Artifact Registry home page](https://cloud.google.com/artifact-registry)
    - [Cloud Artifact Registry documentation](https://cloud.google.com/artifact-registry/docs)

1. Google AI/ML API product pages
    - [Cloud Translation home page](https://cloud.google.com/translate)
    - [Cloud Translation documentation](https://cloud.google.com/translate/docs)
    - [Cloud Translation Python client library (v3 for 3.x)](https://cloud.google.com/translate/docs/reference/libraries/v3/python)
    - [Cloud Translation Python client library (v2 for 2.x)](https://cloud.google.com/translate/docs/reference/libraries/v2/python)
    - [Translation API pricing page](https://cloud.google.com/translate/pricing)
    - [All Cloud AI/ML "building block" APIs](https://web.archive.org/web/20210308144225/https://cloud.google.com/products/ai/building-blocks)
    - [Google ML Kit (Cloud AI/ML API subset for mobile)](https://developers.google.com/ml-kit)
    - [Google ML Kit Translation API](https://developers.google.com/ml-kit/language/translation)

1. Other Google Cloud documentation
    - [Google Cloud Python support](https://cloud.google.com/python)
    - [Google Cloud client libraries](https://cloud.google.com/apis/docs/cloud-client-libraries)
    - [Google Cloud "Always Free" tier](https://cloud.google.com/free/docs/gcp-free-tier#free-tier-usage-limits)
    - [All Google Cloud documentation](https://cloud.google.com/docs)

1. External links
    - [Docker](https://docker.com)
    - [`Dockerfile` documentation](https://docs.docker.com/engine/reference/builder)
    - [`Dockerfile` best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices)
    - [`Procfile` documentation](https://devcenter.heroku.com/articles/procfile)
    - [CNCF Buildpacks open spec](https://buildpacks.io)
