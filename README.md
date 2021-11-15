# Nebulous Google Cloud serverless &amp; API sample application
### Run your own mini-"Google Translate" service locally, on App Engine, Cloud Functions, or Cloud Run

## Description

This is the code repo for a set of codelab tutorials highlighting a single ["nebulous" sample app](https://twitter.com/googledevs/status/1433113274984271875?utm_source=twitter&utm_medium=unpaidsoc&utm_campaign=CDR_wes_aap-serverless_mgrcrbdpk_sms_201031&utm_content=-). What makes this app unique is that it demonstrates the flexibility of _where_ you can run your apps as far as [Google Cloud serverless](https://cloud.google.com/serverless#serverless-products) compute platforms go. With minor configuration tweaks, this app can be deployed (at least) eight different ways:

Deployment | Python 2 | Python 3
--- | --- | ---
Local/hosted Flask|[codelab](https://codelabs.developers.google.com/codelabs/cloud-nebulous-serverless-python-flask?utm_source=codelabs&utm_medium=et&utm_campaign=CDR_wes_aap-serverless_nebservflask_sms_201020&utm_content=-)|_same as Python 2_
App Engine|[codelab](https://codelabs.developers.google.com/codelabs/cloud-nebulous-serverless-python-gae2?utm_source=codelabs&utm_medium=et&utm_campaign=CDR_wes_aap-serverless_nebservgae2_sms_201020&utm_content=-)|[codelab](https://codelabs.developers.google.com/codelabs/cloud-nebulous-serverless-python-gae3?utm_source=codelabs&utm_medium=et&utm_campaign=CDR_wes_aap-serverless_nebservgae3_sms_201020&utm_content=-)
Cloud Functions| _N/A_ |[codelab](https://codelabs.developers.google.com/codelabs/cloud-nebulous-serverless-python-gcf?utm_source=codelabs&utm_medium=et&utm_campaign=CDR_wes_aap-serverless_nebservgcf_sms_201020&utm_content=-)
Cloud Run (Docker)|[codelab](https://codelabs.developers.google.com/codelabs/cloud-nebulous-serverless-python-gcr2?utm_source=codelabs&utm_medium=et&utm_campaign=CDR_wes_aap-serverless_nebservgcr2_sms_201020&utm_content=-)|[codelab](https://codelabs.developers.google.com/codelabs/cloud-nebulous-serverless-python-gcr3?utm_source=codelabs&utm_medium=et&utm_campaign=CDR_wes_aap-serverless_nebservgcr3_sms_201020&utm_content=-)
Cloud Run (Buildpacks)| _N/A_ |[codelab](https://codelabs.developers.google.com/codelabs/cloud-nebulous-serverless-python-gcrbp?utm_source=codelabs&utm_medium=et&utm_campaign=CDR_wes_aap-serverless_nebservgcrbp_sms_201020&utm_content=-)

Admittedly, there may _seem_ to be a bit of "cheating" due to the duplicity of Python 2 and 3, especially since the application is compatible across both language versions without modification or use of compatibility libraries. However there are significant differences between both App Engine runtimes beyond the version language differences. For local Flask or Cloud Run deployments, there are either little or no updates to go from 2.x to 3.x. Neither Cloud Functions nor Cloud Buildpacks support Python 2.


### Python versions

Python **== 2.7** or **>= 3.6**


### Inspiration and implementation

This code sample was inspired by a [user's suboptimal experience](https://www.mail-archive.com/google-appengine@googlegroups.com/msg94549.html) trying to create a simple App Engine app using a Cloud API. It was also inspired by a [colleague's blog post](https://dev.to/googlecloud/portable-code-migrating-across-google-cloud-s-serverless-platforms-2ifk) showing a similar Node.js example "drifting" between GCP serverless platforms.

This app shows developers how to use the [Cloud Translation API](https://cloud.google.com/translate), the API for [Google Translate](https://translate.google.com), and one of GCP's [AI/ML "building block" APIs](https://web.archive.org/web/20210308144225/https://cloud.google.com/products/ai/building-blocks). Such APIs are backed by pre-trained machine learning models, allowing developers with little or no background in AI/ML to leverage machine learning with only API calls. The application implements a mini Google Translate "MVP" (minimally-viable product) web service.


### Hosting options

Aside from local deployment, this app is deployable to these serverless compute platforms:

- [Google App Engine](https://cloud.google.com/appengine) (Standard)
    - Standard source code application deployments (app-hosting in the cloud; "PaaS")
- [Google Cloud Functions](https://cloud.google.com/functions)
    - Instead of an entire app, this is for cloud-based functions or microservices ("FaaS")
- [Google Cloud Run](https://cloud.run)
    - Fully-managed serverless container-hosting in the cloud ("CaaS") service

The purpose of this app is to show users how to deploy the same app to each platform and give developers hands-on experience with each. It also shows users how similar the platforms are to each other that one can "shift" between then typically with just minor configuration changes. A fourth product, [App Engine Flexible](https://cloud.google.com/appengine/docs/flexible), which sits somewhere between App Engine Standard and Cloud Run, is out-of-scope for this sample app.

The app uses the [Flask](https://flask.palletsprojects.com) micro web framework. When deploying locally, the [Flask development server](https://flask.palletsprojects.com/en/master/server) &mdash; also see [its docs](https://flask.palletsprojects.com/server) &mdash; is used. As an application, you're likely to deploy to either App Engine or Cloud Run, depending on whether your app is containerized. Since this "app" only has a single purpose/function, it is also reasonable to deploy it to Cloud Functions.

App Engine is for users who wish to deploy a traditional web stack (LAMP, MEAN, etc.) application direct from source without knowledge of containers, Docker, or `Dockerfile`s. Cloud Run is similar but for applications that are explicitly containerized, freeing you from language, library, or binary restrictions. Cloud Functions is for deploying simple microservices like ours, and its Python runtime sends Flask request objects directly to deployed functions.

When running on App Engine or Cloud Functions, this sample app uses the default web server that comes with those services (`gunicorn`). For Cloud Run, developers must start their own web server; this sample app again chooses Flask's development server (but can be configured to your server of choice; `gunicorn` can be enabled if uncommented in the configuration.


### Service account credentials ("local-only")

The credentials JSON file &mdash; call it anything you like, but we're using the name `credentials.json` &mdash; is only used when running locally to specify the service account used to talk to Cloud APIs. Developers are prompted to download it after [creating a service account key-pair](https://console.cloud.google.com/iam-admin/serviceaccounts/create). Check out the documentation for [service accounts](https://cloud.google.com/docs/authentication/getting-started) and the [service account public/private key/pairs](https://cloud.google.com/translate/docs/setup#service_account_and_private_key).

Why just locally? For simplicity, this sample app uses [default service accounts](https://cloud.google.com/iam/docs/service-accounts#default) when deploying to the cloud, so neither the service account key-pair created for local deployment nor its `credentials.json` will be used in those cases. In other words, if not deploying/testing locally, you don't have to create a service account key.

However, while we suggest you "delete" `credentials.json` and not use it when deploying to the cloud ("finding credentials automatically"), you can disregard that advice and opt to use that service account key-pair ("passing credentials manually") if desired as long as you point to those credentials. Read more about these options in the [documentation](https://cloud.google.com/docs/authentication/production).


### Cost

While many Google APIs can be used without fees, use of GCP products &amp; APIs is _not_ free. Certain products do offer an ["Always Free" tier](https://cloud.google.com/free/docs/gcp-free-tier#free-tier-usage-limits) which you have to exceed in order to be billed. For our purposes, while the Translation API does not explicitly list a free quota on that page, its pricing information page (link below) indicates a certain number of [translated characters](https://cloud.google.com/translate/pricing#charged-characters) as a free monthly quota applied as a credit, so long as you stay within that limit, you should not incur any additional charges. When enabling services, you may be asked for an active billing account which requires a financial instrument such as a credit card. Reference relevant pricing information before doing so.

While Cloud Functions and Cloud Run share a similar Always Free tier and pricing model, App Engine is slightly different. Here are each product's corresponding pricing pages for you to learn more as well as link to our pricing calculator:

- [App Engine](https://cloud.google.com/appengine/pricing)
- [Cloud Functions](https://cloud.google.com/functions/pricing)
- [Cloud Run](https://cloud.google.com/run/pricing)
- [Cloud Translation](https://cloud.google.com/translate/pricing)
- [GCP pricing calculator](https://cloud.google.com/products/calculator)

Furthermore, deploying to GCP serverless platforms incur [minor build and storage costs](https://cloud.google.com/appengine/pricing#pricing-for-related-google-cloud-products). [Cloud Build](https://cloud.google.com/build/pricing) has its own free quota as does [Cloud Storage](https://cloud.google.com/storage/pricing#cloud-storage-always-free). For greater transparency, Cloud Build builds your application image which is then sent to the [Cloud Container Registry](https://cloud.google.com/container-registry/pricing), or [Artifact Registry](https://cloud.google.com/artifact-registry/pricing), its successor; storage of that image uses up some of that (Cloud Storage) quota as does network egress when transferring that image to the service you're deploying to. However you may live in region that does not have such a free tier, so be aware of your storage usage to minimize potential costs. (You may look at what storage you're using and how much, including deleting build artifacts via [your Cloud Storage browser](https://console.cloud.google.com/storage/browser).)


### Enable Cloud services used

Once you have a billing account, you can enable the services/APIs for each product used. Go to the Cloud console pages for each respective Cloud product used and enable the service:

1. [App Engine](https://console.cloud.google.com/appengine)
1. [Cloud Functions](https://console.cloud.google.com/functions)
1. [Cloud Run](https://console.cloud.google.com/run)
1. [Cloud Translation](https://console.cloud.google.com/apis/api/translate.googleapis.com)

Alternatively, you use the [`gcloud` CLI (command-line interface)](https://cloud.google.com/sdk/gcloud) available from the [Cloud SDK](https://cloud.google.com/sdk). Review the [Cloud SDK install instructions](https://cloud.google.com/sdk/docs/quickstart) if needed. New users should also reference the [`gcloud` cheatsheet](https://cloud.google.com/sdk/docs/cheatsheet).

Enable all 4 services with this one `gcloud` command: `gcloud services enable translate.googleapis.com run.googleapis.com cloudfunctions.googleapis.com appengine.googleapis.com`


### The application itself

The app consists of a simple web page prompting the user for a phrase to translate from English to Spanish. The translated results along with the original phrase are presented along with an empty form for a follow-up translation if desired. While the majority of this app's deployments are in Python 3, there are still many users working on upgrading from Python 2, so some of those deployments are available to help with migration planning. This is what the app looks like after completing one translation (Cloud Run version):

![app screenshot](https://user-images.githubusercontent.com/1102504/133918482-fc66d512-aeb7-4982-bcd2-75794cd21349.png)


## Deployments and their files

These are the files provided in this repo and the deployments they're applicable to:

![repository files](https://user-images.githubusercontent.com/1102504/119735453-2f3af500-be31-11eb-9115-3fdeb22ec31c.png)

> NOTES:
>- * &mdash; `requirements.txt` is used for local and App Engine (2.x) package installations and not required in deployments themselves unlike all others
>- `main.py` and `templates/index.html` comprise the entire application and are always required
>- `noxfile.py` and `test_translate.py` are for testing only; see [Testing section](#testing) below
>- All `.*ignore` and `.git*` files/folders are administrative and not listed in table above or deployments below
>- Files applicable only to a specific language version are annotated above

Below are the required settings and instructions for all documented deployments. The "**TL:DR;**" section at the top of each configuration summarizes the key files (see above) while the table beneath spells out the details. No administrative files are listed.


## **Local Flask server (Python 2)**

- **TL;DR:** application files (`main.py` &amp; `requirements.txt`) plus `credentials.json`

File | Description
--- | ---
`main.py`|**use as-is** from repo
`credentials.json`|**create** (if necessary) **and use** per instructions below
`app.yaml`|_unused_ (delete or leave as-is)
`appengine_config.py`|_unused_ (delete or leave as-is; only for Python 2 App Engine)
`requirements.txt`|**use as-is** to install packages locally (see below) but _unused_ thereafter
`lib`|_unused_ (delete or leave as-is if it exists)
`Dockerfile`|_unused_ (delete or leave as-is)
`Procfile`|_unused_ (delete or leave as-is)

1. **Create service account key**, download key file as `credentials.json` in working directory, and set `GOOGLE_APPLICATION_CREDENTIALS` environment variable pointing to it (more [above](#service-account-credentials-local-only) and [here](https://cloud.google.com/docs/authentication/production#manually))
1. **Run** `pip install -U pip -r requirements.txt` to install/update packages locally (or `pip2`)
1. **Run** `python main.py` to run on local Flask server (or `python2`)


## **Local Flask server (Python 3)**

- **TL;DR:** app files plus `credentials.json` (identical to Python 2 deployment)

File | Description
--- | ---
`main.py`|**use as-is** from repo
`credentials.json`|**create** (if necessary) **and use** per instructions below
`app.yaml`|_unused_ (delete or leave as-is)
`appengine_config.py`|_unused_ (delete or leave as-is; only for Python 2 App Engine)
`requirements.txt`|**use as-is** to install packages locally (see below) but _unused_ thereafter
`lib`|_unused_ (delete or leave as-is if it exists)
`Dockerfile`|_unused_ (delete or leave as-is)
`Procfile`|_unused_ (delete or leave as-is)

1. **Reuse** existing `credentials.json` or create new one per Python 2 instructions above
1. **Run** `pip install -U pip -r requirements.txt` to install/update packages locally (or `pip3`)
    - While you can reuse `credentials.json` from Python 2, you must still install the packages for Python 3.
1. **Run** `python main.py` to run on local Flask server (or `python3`)


## **App Engine (Python 2)**

- **TL;DR:** app files plus `app.yaml`, `appengine_config.py`, and `lib`

File | Description
--- | ---
`main.py`|**use as-is** from repo
`credentials.json`|**delete** (or rename) if it exists (default credentials used in the cloud)
`app.yaml`|**use as-is** from repo (ensure `#runtime:python39` commented out)
`appengine_config.py`|**use as-is** from repo
`requirements.txt`|**use as-is** to install packages locally (see below) but _unused_ thereafter
`lib`|**create folder** per instructions below
`Dockerfile`|_unused_ (delete or leave as-is)
`Procfile`|_unused_ (delete or leave as-is)

1. **Delete** `credentials.json` (see above)
1. **Run** `pip install -t lib -r requirements.txt` to populate `lib` folder (or `pip2`)
1. **Run** `gcloud app deploy` to deploy to Python 2 App Engine


## **App Engine (Python 3)**

- **TL;DR:** app files plus `app.yaml`

File | Description
--- | ---
`main.py`|**use as-is** from repo
`credentials.json`|**delete** (or rename) if it exists (default credentials used in the cloud)
`app.yaml`|**uncomment** `runtime:python39` (or Python 3.7 or 3.8); **delete** all other lines
`appengine_config.py`|_unused_ (delete or leave as-is; only for Python 2 App Engine)
`requirements.txt`|**use as-is** from repo
`lib`|**delete** (or rename) this folder if it exists (not used with Python 3 App Engine)
`Dockerfile`|_unused_ (delete or leave as-is)
`Procfile`|_unused_ (delete or leave as-is)

1. **Edit** `app.yaml` and **delete** `credentials.json` and `lib` (see above)
1. **Run** `gcloud app deploy` to deploy to Python 3 App Engine


## **Cloud Functions (Python 3)**

- **TL;DR:** app files

File | Description
--- | ---
`main.py`|**use as-is** from repo
`credentials.json`|**delete** (or rename) if it exists (default credentials used in the cloud)
`app.yaml`|_unused_ (delete or leave as-is; only for App Engine)
`appengine_config.py`|_unused_ (delete or leave as-is; only for Python 2 App Engine)
`requirements.txt`|**use as-is** from repo
`lib`|**delete** (or rename) this folder if it exists (not used with Cloud Functions)
`Dockerfile`|_unused_ (delete or leave as-is)
`Procfile`|_unused_ (delete or leave as-is)

1. **Delete** `credentials.json` and `lib` (see above)
1. **Run** `gcloud functions deploy translate --runtime python39 --trigger-http --allow-unauthenticated` to deploy to Cloud Functions (or Python 3.7 or 3.8)
    - That command creates &amp; deploys a new HTTP-triggered Cloud Function (name must match what's in `main.py`)
1. There is no support for Python 2 with Cloud Functions


## **Cloud Run (Python 2 via Docker)**

- **TL;DR:** app files plus `Dockerfile`

File | Description
--- | ---
`main.py`|**use as-is** from repo
`credentials.json`|**delete** (or rename) if it exists (default credentials used in the cloud)
`app.yaml`|_unused_ (delete or leave as-is; only for App Engine)
`appengine_config.py`|_unused_ (delete or leave as-is; only for Python 2 App Engine)
`requirements.txt`|**uncomment** `grpcio==1.39.0`
`lib`|**delete** (or rename) this folder if it exists (not used with Cloud Run)
`Dockerfile`|**use as-is** from repo (ensure `#FROM python:3-slim` commented out)
`Procfile`|_unused_ (delete or leave as-is)

1. **Delete** `credentials.json` and `lib` (see above)
1. **Edit** `requirements.txt` to specify final version of `grpcio` supporting Python 2
1. **Run** `gcloud run deploy translate --allow-unauthenticated --platform managed` to deploy to Cloud Run; optionally add `--region REGION` for non-interactive deploy
    - The above command wraps `docker build` and `docker push`, deploying the image to [Cloud Artifact Registry](https://cloud.google.com/artifact-registry), and finally `docker run` to deploy the service, all in one convenient command.
1. You can also use this shortcut to deploy to Cloud Run:
    [![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run)
1. By default, App Engine &amp; Cloud Functions launch production servers; with Cloud Run, the Flask development server is used for prototyping. For production, bundle and deploy a production server like `gunicorn`:
    1. **Uncomment** `gunicorn` from `requirements.txt` (commented out for App Engine &amp; Cloud Functions)
    1. **Uncomment** the `ENTRYPOINT` entry for `gunicorn` replacing the default entry in `Dockerfile`
    1. Re-use the same deploy command


## **Cloud Run (Python 3 via Docker)**

- **TL;DR:** app files plus `Dockerfile` (nearly identical to Python 2 deployment)

File | Description
--- | ---
`main.py`|**use as-is** from repo
`credentials.json`|**delete** (or rename) if it exists (default credentials used in the cloud)
`app.yaml`|_unused_ (delete or leave as-is; only for App Engine)
`appengine_config.py`|_unused_ (delete or leave as-is; only for Python 2 App Engine)
`requirements.txt`|**use as-is** from repo
`lib`|**delete** (or rename) this folder if it exists (not used with Cloud Run)
`Dockerfile`|**replace** `FROM python:2-slim` with `FROM python:3-slim` (commented out) but **keep all other lines**
`Procfile`|_unused_ (delete or leave as-is)

1. **Edit** `Dockerfile` and **delete** `credentials.json` and `lib` (see above)
1. **Run** `gcloud run deploy translate --allow-unauthenticated --platform managed` to deploy to Cloud Run; optionally add `--region REGION` for non-interactive deploy
1. The shortcut "button" above can be customized for Python 3 if you make the `Dockerfile` update above and commit it to your fork/clone.
1. By default, App Engine &amp; Cloud Functions launch production servers; with Cloud Run, the Flask development server is used for prototyping. For production, bundle and deploy a production server like `gunicorn`:
    1. **Uncomment** `gunicorn` from `requirements.txt` (commented out for App Engine &amp; Cloud Functions)
    1. **Uncomment** the `ENTRYPOINT` entry for `gunicorn` replacing the default entry in `Dockerfile`
    1. Re-use the same deploy command


## **Cloud Run (Python 3 via Cloud Buildpacks)**

- **TL;DR:** app files plus [`Procfile`](https://devcenter.heroku.com/articles/procfile)

File | Description
--- | ---
`main.py`|**use as-is** from repo
`credentials.json`|**delete** (or rename) if it exists (default credentials used in the cloud)
`app.yaml`|_unused_ (delete or leave as-is; only for App Engine)
`appengine_config.py`|_unused_ (delete or leave as-is; only for Python 2 App Engine)
`requirements.txt`|**use as-is** from repo
`lib`|**delete** (or rename) this folder if it exists (not used with Cloud Run)
`Dockerfile`|**delete** (or rename) this file (_required_)
`Procfile`|**use as-is** from repo

1. **Delete** `Dockerfile`, `credentials.json`, and `lib` (see above)
1. There is no support for Python 2 with Cloud Buildpacks (2.x developers must use Docker)
1. **Run** `gcloud run deploy translate --allow-unauthenticated --platform managed` to deploy to Cloud Run; optionally add `--region REGION` for non-interactive deploy
1. By default, App Engine &amp; Cloud Functions launch production servers; with Cloud Run, the Flask development server is used for prototyping. For production, bundle and deploy a production server like `gunicorn`:
    1. **Uncomment** `gunicorn` from `requirements.txt` (commented out for App Engine &amp; Cloud Functions)
    1. **Uncomment** the `web:` entry for `gunicorn` replacing the default entry in `Procfile`
    1. Re-use the same deploy command


## References

1. Google Cloud serverless product pages
    - App Engine
        - [App Engine home page](https://cloud.google.com/appengine)
        - [App Engine documentation](https://cloud.google.com/appengine/docs)
        - [Python 3 App Engine quickstart](https://cloud.google.com/appengine/docs/standard/python3/quickstart)
        - [Python 3 App Engine (Standard) runtime](https://cloud.google.com/appengine/docs/standard/python3/runtime)
        - [Python 2 App Engine (Standard) runtime](https://cloud.google.com/appengine/docs/standard/python/runtime)
        - [Default service accounts for App Engine](https://cloud.google.com/appengine/docs/standard/python3/service-account)
    - Cloud Functions
        - [Cloud Functions home page](https://cloud.google.com/functions)
        - [Cloud Functions documentation](https://cloud.google.com/functions/docs)
        - [Python Cloud Functions quickstart](https://cloud.google.com/functions/docs/quickstart-python)
        - [Default service accounts for Cloud Functions](https://cloud.google.com/functions/docs/concepts/iam#access_control_for_service_accounts)
    - Cloud Run
        - [Cloud Run home page](https://cloud.run)
        - [Cloud Run documentation](https://cloud.google.com/run/docs)
        - [Python Cloud Run quickstart](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python)
        - [Default service accounts for Cloud Run](https://cloud.google.com/run/docs/securing/service-identity)

1. App Engine migration between runtimes/platforms
    - [Differences between Python 2 &amp; 3 App Engine (Standard) runtimes](https://cloud.google.com/appengine/docs/standard/runtimes)
    - [Python 2 to 3 App Engine (Standard) migration guide](http://cloud.google.com/appengine/docs/standard/python/migrate-to-python3)
    - [App Engine (Standard) to Cloud Run codelab tutorial](http://g.co/codelabs/pae-migrate-rundocker) (Docker)
    - [App Engine (Standard) to Cloud Run codelab tutorial](http://g.co/codelabs/pae-migrate-runbldpks) (Cloud Buildpacks)

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
    - [Flask](https://flask.palletsprojects.com)
    - [Docker](https://docker.com)
    - [`Dockerfile` documentation](https://docs.docker.com/engine/reference/builder)
    - [`Dockerfile` best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices)
    - [`Procfile` documentation](https://devcenter.heroku.com/articles/procfile)
    - [CNCF Buildpacks open spec](https://buildpacks.io)


## Testing

Testing is driven by [`nox`](http://nox.thea.codes) which uses [`pytest`](https://pytest.org/) for testing and [`flake8`](https://flake8.pycqa.org) for linting, installing both in virtual environments along with application dependencies, `flask` and `google-cloud-translate`, and finally, `blinker`, a signaling framework integrated into Flask. To run the lint and unit tests (testing `GET` and `POST` requests), install `nox` (with the expected `pip install -U nox`) and run it from the command line in the application folder and ensuring the `noxfile.py` file is present. Expected output:
```
$ nox
nox > Running session tests-2.7
nox > Creating virtual environment (virtualenv) using python2.7 in .nox/tests-2-7
nox > python -m pip install pytest blinker flask google-cloud-translate
nox > pytest
============================================ test session starts =============================================
platform darwin -- Python 2.7.16, pytest-4.6.11, py-1.10.0, pluggy-0.13.1
rootdir: /private/tmp/cloud-nebulous-serverless-python
collected 2 items

test_translate.py ..                                                                                   [100%]

============================================== warnings summary ==============================================
.nox/tests-2-7/lib/python2.7/site-packages/google/cloud/translate_v3/__init__.py:32
  /private/tmp/cloud-nebulous-serverless-python/.nox/tests-2-7/lib/python2.7/site-packages/google/cloud/translate_v3/__init__.py:32: DeprecationWarning: A future version of this library will drop support for Python 2.7. More details about Python 2 support for Google Cloud Client Libraries can be found at https://cloud.google.com/python/docs/python2-sunset/
    warnings.warn(message, DeprecationWarning)

-- Docs: https://docs.pytest.org/en/latest/warnings.html
==================================== 2 passed, 1 warnings in 1.02 seconds ====================================
nox > Session tests-2.7 was successful.
nox > Running session tests-3.6
nox > Creating virtual environment (virtualenv) using python3.6 in .nox/tests-3-6
nox > python -m pip install pytest blinker flask google-cloud-translate
nox > pytest
============================================ test session starts =============================================
platform darwin -- Python 3.6.8, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /private/tmp/cloud-nebulous-serverless-python
collected 2 items

test_translate.py ..                                                                                   [100%]

============================================= 2 passed in 1.22s ==============================================
nox > Session tests-3.6 was successful.
nox > Running session tests-3.9
nox > Creating virtual environment (virtualenv) using python3.9 in .nox/tests-3-9
nox > python -m pip install pytest blinker flask google-cloud-translate
nox > pytest
============================================ test session starts =============================================
platform darwin -- Python 3.9.1, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /private/tmp/cloud-nebulous-serverless-python
collected 2 items

test_translate.py ..                                                                                   [100%]

============================================= 2 passed in 1.04s ==============================================
nox > Session tests-3.9 was successful.
nox > Running session lint-2.7
nox > Creating virtual environment (virtualenv) using python2.7 in .nox/lint-2-7
nox > python -m pip install flake8
nox > flake8 --show-source --builtin=gettext --max-complexity=20 --exclude=.nox,.cache,env,lib,generated_pb2,*_pb2.py,*_pb2_grpc.py --ignore=E121,E123,E126,E203,E226,E24,E266,E501,E704,W503,W504,I202 --max-line-length=88 .
nox > Session lint-2.7 was successful.
nox > Running session lint-3.6
nox > Creating virtual environment (virtualenv) using python3.6 in .nox/lint-3-6
nox > python -m pip install flake8
nox > flake8 --show-source --builtin=gettext --max-complexity=20 --exclude=.nox,.cache,env,lib,generated_pb2,*_pb2.py,*_pb2_grpc.py --ignore=E121,E123,E126,E203,E226,E24,E266,E501,E704,W503,W504,I202 --max-line-length=88 .
nox > Session lint-3.6 was successful.
nox > Running session lint-3.9
nox > Creating virtual environment (virtualenv) using python3.9 in .nox/lint-3-9
nox > python -m pip install flake8
nox > flake8 --show-source --builtin=gettext --max-complexity=20 --exclude=.nox,.cache,env,lib,generated_pb2,*_pb2.py,*_pb2_grpc.py --ignore=E121,E123,E126,E203,E226,E24,E266,E501,E704,W503,W504,I202 --max-line-length=88 .
nox > Session lint-3.9 was successful.
nox > Ran multiple sessions:
nox > * tests-2.7: success
nox > * tests-3.6: success
nox > * tests-3.9: success
nox > * lint-2.7: success
nox > * lint-3.6: success
nox > * lint-3.9: success
```
