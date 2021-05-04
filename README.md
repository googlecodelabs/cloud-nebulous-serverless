# Nebulous Google Cloud serverless &amp; API sample application
### Run your own mini-"Google Translate" service locally, on App Engine, Cloud Functions, or Cloud Run

## Description

This is the code repo for a set of codelab tutorials highlighting a single "nebulous" sample app. What makes this app unique is that it demonstrates the flexibility of _where_ you can run your apps as far as Google Cloud serverless compute platforms go. With minor configuration tweaks, this app can be deployed eight different ways:

1. Local Flask server (Python 2)
1. Local Flask server (Python 3)
1. Google App Engine (Python 2)
1. Google App Engine (Python 3)
1. Google Cloud Functions (Python 3)
1. Google Cloud Run (Python 2 via Docker)
1. Google Cloud Run (Python 3 via Docker)
1. Google Cloud Run (Python 3 via Cloud Buildpacks)

Admittedly, there's a bit of "cheating" due to the duplicity of Python 2 and 3, especially since the application is compatible across both without modification nor use of compatibility libraries. However, those familiar with the differences in App Engine across both runtimes have internalized a greater significance.


### App

This app shows developers how to use a Google Cloud service (API) from one of the serverless compute platforms, specifically the [Cloud Translation API](https://cloud.google.com/translate). It's the API for [Google Translate](https://translate.google.com) and one of Google Cloud's [AI/ML building block" APIs](https://cloud.google.com/products/ai/building-blocks) backed by pre-trained models so you don't have to build your own, allowing developers with little or no background in AI/ML to leverage machine learning with only API calls. The application implements a simplistic English-to-Spanish mini-"Google Translate" web service.


### Services

The app uses the [Flask](https://flask.palletsprojects.com) micro web framework. When deploying locally, the [Flask development server](https://flask.palletsprojects.com/en/master/server) &mdash; also see [its docs](https://flask.palletsprojects.com/server) &mdash; is used. The app can also be configured for deployment to one of a pair of [Google Cloud serverless](https://cloud.google.com/serverless) application-hosting platforms, [App Engine](https://cloud.google.com/appengine) (Standard) or [Cloud Run](https://cloud.google.com/run). Since this "app" only has a single purpose/function, it is also reasonable to deploy it to [Cloud Functions](https://cloud.google.com/functions).

App Engine is for users who wish to deploy a traditional web stack-based (LAMP, MEAN, etc.) application direct from source without knowledge of containers, Docker, nor `Dockerfile`s. Cloud Run is similar but for applications that are explicitly containerized. You can deploy pre-existing containers or build-and-deploy direct from source as well, but without language, library, or binary restrictions. Cloud Functions is for deploying simple functions or microservices like this and automatically sends Flask request objects to the deployed function (see compatibility line in `main.py`.)

When running on App Engine or Cloud Functions, this sample app uses the default web server that comes with those services (`gunicorn`). For Cloud Run, developers must start their own web server; this sample app again chooses Flask's development server (but can be configured to your server of choice).


### Service account credentials ("local-only")

The credentials JSON file &mdash; call it anything you like, but we're using the name `credentials.json` &mdash; is only used when running locally to specify the service account used to talk to Cloud APIs. Developers are prompted to download it after [creating a service account key-pair](https://console.cloud.google.com/iam-admin/serviceaccounts/create). Check out the documentation for [service accounts](https://cloud.google.com/docs/authentication/getting-started) and the [service account public/private key/pairs](https://cloud.google.com/translate/docs/setup#service_account_and_private_key).

Why just locally? For simplicity, this sample app uses [default service accounts](https://cloud.google.com/iam/docs/service-accounts#default) when deploying to the cloud, so neither the service account key-pair created for local deployment nor its `credentials.json` will be used in those cases. In other words, if not deploying/testing locally, you don't have to create a service account key.

However, while we suggest you "delete" `credentials.json` and not use it when deploying to the cloud ("finding credentials automatically"), you can disregard that advice and opt to use that service account key-pair ("passing credentials manually") if desired as long as you point to those credentials. Read more about these options in the [documentation](https://cloud.google.com/docs/authentication/production).


### Cost

While many Google APIs can be used without fees, use of Google Cloud (Platform) products &amp; APIs is _not_ free. Certain Google Cloud Platform (GCP) products do offer an ["Always Free" tier](https://cloud.google.com/free/docs/gcp-free-tier#free-tier-usage-limits) for which you have to exceed in order to be billed. For our purposes, while the Translation API does not explicitly list a free quota on that page, [its pricing information page](https://cloud.google.com/translate/pricing) indicates a certain number of [translated characters](https://cloud.google.com/translate/pricing#charged-characters) as a free monthly quota applied as a credit, so long as you stay within that limit, you should not incur any additional charges. When enabling any GCP services, you may be asked for an active billing account which requires a financial instrument such as a credit card. Reference all this pricing information before doing so.

Furthermore, deploying to Google Cloud serverless compute platforms incur [minor build and storage costs](https://cloud.google.com/appengine/pricing#pricing-for-related-google-cloud-products). [Cloud Build](https://cloud.google.com/build/pricing) has its own free quota as does [Cloud Storage](https://cloud.google.com/storage/pricing#cloud-storage-always-free). For greater transparency, Cloud Build builds your application image which is than sent to the [Cloud Container Registry](https://cloud.google.com/container-registry/pricing); storage of that image uses up some of that (Cloud Storage) quota as does network egress when transferring that image to the service you're deploying to. However, you may live in region that does not have such a free tier, so be aware of your storage usage to minimize potential costs. (You may look at what storage you're using and how much, including deleting build artifacts via [your Cloud Storage browser](https://console.cloud.google.com/storage/browser).)


### Deployments

As mentioned above, local "deployments" use the Flask development server while the [`gcloud` CLI](https://cloud.google.com/sdk/gcloud) (command-line interface) is used when deploying to the cloud. It is part of the [Cloud SDK](https://cloud.google.com/sdk) which you should [install](https://cloud.google.com/sdk/docs/quickstart). New users should also reference the [`gcloud` cheatsheet](https://cloud.google.com/sdk/docs/cheatsheet).

Below are the required settings and instructions to deploy this app for all available configurations. Note the application file `main.py` is always required (should be obvious). The "**TL:DR;**" section at the top of each deployment type summarizes the key files in each configuration while the table beneath spells it out the details. The `noxfile.py` and `test_translate.py` files are for testing only thus not listed &mdash; see the [Testing section](#testing) at the very bottom. None of the `.*ignore` administrative files are included in deployments either.


## **Local Flask server (Python 2)**

- **TL;DR:** application files plus `credentials.json`

File | Description
--- | ---
`main.py`|**use as-is** from repo
`credentials.json`|**create** (if necessary) **and use** per instructions below
`app.yaml`|_unused_ (delete or leave as-is)
`appengine_config.py`|_unused_ (delete or leave as-is)
`requirements.txt`|**use as-is** to install packages locally (see below) but _unused_ thereafter
`lib`|_unused_ (delete or leave as-is if it exists)
`Dockerfile`|_unused_ (delete or leave as-is)
`Procfile`|_unused_ (delete or leave as-is)

- **Create service account key**, download key file as `credentials.json` in working directory, and set `GOOGLE_APPLICATION_CREDENTIALS` environment variable pointing to it (more [above](#service-account-credentials-local-only) and [here](https://cloud.google.com/docs/authentication/production#manually))
- **Run** `pip install -U pip -r requirements.txt` to install/update packages locally (or `pip2`)
- **Run** `python main.py` to run on local Flask server (or `python2`)


## **Local Flask server (Python 3)**

- **TL;DR:** application files plus `credentials.json` (identical to Python 2 deployment)

File | Description
--- | ---
`main.py`|**use as-is** from repo
`credentials.json`|**create** (if necessary) **and use** per instructions below
`app.yaml`|_unused_ (delete or leave as-is)
`appengine_config.py`|_unused_ (delete or leave as-is)
`requirements.txt`|**use as-is** to install packages locally (see below) but _unused_ thereafter
`lib`|_unused_ (delete or leave as-is if it exists)
`Dockerfile`|_unused_ (delete or leave as-is)
`Procfile`|_unused_ (delete or leave as-is)

- **Reuse** existing `credentials.json` or create new one per Python 2 instructions above
- **Run** `pip install -U pip -r requirements.txt` to install/update packages locally (or `pip3`)
    - While you can reuse `credentials.json` from Python 2, you must still install the packages for Python 3.
- **Run** `python main.py` to run on local Flask server (or `python3`)


## **App Engine (Python 2)**

- **TL;DR:** app files plus `app.yaml`, `appengine_config.py`, and `lib`

File | Description
--- | ---
`main.py`|**use as-is** from repo
`credentials.json`|**delete** (or rename) if it exists
`app.yaml`|**use as-is** from repo (ensure `#runtime:python38` commented out)
`appengine_config.py`|**use as-is** from repo
`requirements.txt`|**use as-is** to install packages locally (see below) but _unused_ thereafter
`lib`|**create folder** per instructions below
`Dockerfile`|_unused_ (delete or leave as-is)
`Procfile`|_unused_ (delete or leave as-is)

- **Run** `pip install -t lib -r requirements.txt` to populate `lib` folder (or `pip2`)
- **Run** `gcloud app deploy` to deploy to Python 2 App Engine


## **App Engine (Python 3)**

- **TL;DR:** app files plus `app.yaml` and `requirements.txt`

File | Description
--- | ---
`main.py`|**use as-is** from repo
`credentials.json`|**delete** (or rename) if it exists
`app.yaml`|**uncomment** `runtime:python38` (can also use 3.7 or 3.9) and **delete all other lines**
`appengine_config.py`|**delete** (or rename) this file (not used with Python 3 App Engine)
`requirements.txt`|**use as-is** from repo
`lib`|**delete** (or rename) this folder if it exists (not used with Python 3 App Engine)
`Dockerfile`|_unused_ (delete or leave as-is)
`Procfile`|_unused_ (delete or leave as-is)

- **Run** `gcloud app deploy` to deploy to Python 3 App Engine


## **Cloud Functions (Python 3)**

- **TL;DR:** app files plus `requirements.txt`

File | Description
--- | ---
`main.py`|**use as-is** from repo
`credentials.json`|**delete** (or rename) if it exists
`app.yaml`|**delete** (or rename) this file (not used with Cloud Functions)
`appengine_config.py`|**delete** (or rename) this file (not used with Cloud Functions)
`requirements.txt`|**use as-is** from repo
`lib`|**delete** (or rename) this folder if it exists (not used with Cloud Functions)
`Dockerfile`|_unused_ (delete or leave as-is)
`Procfile`|_unused_ (delete or leave as-is)

- **Run** `gcloud functions deploy translate --runtime python38 --trigger-http --allow-unauthenticated` to deploy to Cloud Functions (can also use 3.7 or 3.9)
    - That command creates &amp; deploys a new HTTP-triggered Cloud Function (name must match what's in `main.py`)
- There is no support for Python 2 with Cloud Functions


## **Cloud Run (Python 2 via Docker)**

- **TL;DR:** app files plus `requirements.txt` and `Dockerfile`

File | Description
--- | ---
`main.py`|**use as-is** from repo
`credentials.json`|**delete** (or rename) if it exists
`app.yaml`|**delete** (or rename) this file (not used with Cloud Run)
`appengine_config.py`|**delete** (or rename) this file (not used with Cloud Run)
`requirements.txt`|**use as-is** from repo
`lib`|**delete** (or rename) this folder if it exists (not used with Cloud Run)
`Dockerfile`|**use as-is** from repo (ensure `#FROM python:3-slim` commented out)
`Procfile`|_unused_ (delete or leave as-is)

- **Run** `gcloud beta run deploy translate --allow-unauthenticated --platform managed --source .` to deploy to Cloud Run
    - The above command wraps `docker build` and `docker push`, deploying the image to [Cloud Artifact Registry](https://cloud.google.com/artifact-registry), and finally `docker run` to deploy the service, all in one convenient command.
- You can also use this shortcut to deploy to Cloud Run:

[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run)


## **Cloud Run (Python 3 via Docker)**

- **TL;DR:** app files plus `requirements.txt` and `Dockerfile` (identical to Python 2 deployment except for minor edit)

File | Description
--- | ---
`main.py`|**use as-is** from repo
`credentials.json`|**delete** (or rename) if it exists
`app.yaml`|**delete** (or rename) this file (not used with Cloud Run)
`appengine_config.py`|**delete** (or rename) this file (not used with Cloud Run)
`requirements.txt`|**use as-is** from repo
`lib`|**delete** (or rename) this folder if it exists (not used with Cloud Run)
`Dockerfile`|**replace** `FROM python:2-slim` with `FROM python:3-slim` (commented out) but **keep all other lines**
`Procfile`|_unused_ (delete or leave as-is)

- Same as Cloud Run Python 2 via Docker except `Dockerfile`
- **Run** `gcloud beta run deploy translate --allow-unauthenticated --platform managed --source .` to deploy to Cloud Run
- The shortcut can be customized for Python 3 if you make the `Dockerfile` update above and commit it to your fork/clone.


## **Cloud Run (Python 3 via Cloud Buildpacks)**

- **TL;DR:** app files plus `requirements.txt` and `Procfile`

File | Description
--- | ---
`main.py`|**use as-is** from repo
`credentials.json`|**delete** (or rename) if it exists
`app.yaml`|**delete** (or rename) this file (not used with Cloud Run)
`appengine_config.py`|**delete** (or rename) this file (not used with Cloud Run)
`requirements.txt`|**use as-is** from repo
`lib`|**delete** (or rename) this folder if it exists (not used with Cloud Run)
`Dockerfile`|**delete** (or rename) this file (containers/Docker/`Dockerfile` knowledge unnecessary)
`Procfile`|**use as-is** from repo

- Same as Cloud Run Python 2/3 via Docker except _no_ `Dockerfile` but _with_ [`Procfile`](https://devcenter.heroku.com/articles/procfile)
- There is no support for Python 2 with Cloud Buildpacks (2.x developers must use Docker)
- **Run** `gcloud beta run deploy translate --allow-unauthenticated --platform managed --source .` to deploy to Cloud Run


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
        - [Cloud Run home page](https://cloud.google.com/run)
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
    - [All Cloud AI/ML "building block" APIs](https://cloud.google.com/products/ai/building-blocks)
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
============================================== test session starts ==============================================
platform darwin -- Python 2.7.16, pytest-4.6.11, py-1.10.0, pluggy-0.13.1
rootdir: /tmp/cloud-nebulous-serverless-python
collected 2 items

test_translate.py ..                                                                                      [100%]

=============================================== warnings summary ================================================
.nox/tests-2-7/lib/python2.7/site-packages/google/cloud/translate_v3/__init__.py:32
  /tmp/cloud-nebulous-serverless-python/.nox/tests-2-7/lib/python2.7/site-packages/google/cloud/translate_v3/__init__.py:32: DeprecationWarning: A future version of this library will drop support for Python 2.7. More details about Python 2 support for Google Cloud Client Libraries can be found at https://cloud.google.com/python/docs/python2-sunset/
    warnings.warn(message, DeprecationWarning)

-- Docs: https://docs.pytest.org/en/latest/warnings.html
===================================== 2 passed, 1 warnings in 7.22 seconds ======================================
nox > Session tests-2.7 was successful.
nox > Running session tests-3.9
nox > Creating virtual environment (virtualenv) using python3.9 in .nox/tests-3-9
nox > python -m pip install pytest blinker flask google-cloud-translate
nox > pytest
============================================== test session starts ==============================================
platform darwin -- Python 3.9.1, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
rootdir: /tmp/cloud-nebulous-serverless-python
collected 2 items

test_translate.py ..                                                                                      [100%]

=============================================== 2 passed in 6.19s ===============================================
nox > Session tests-3.9 was successful.
nox > Running session lint-2.7
nox > Creating virtual environment (virtualenv) using python2.7 in .nox/lint-2-7
nox > python -m pip install flake8
nox > flake8 --show-source --builtin=gettext --max-complexity=20 --exclude=.nox,.cache,env,lib,generated_pb2,*_pb2.py,*_pb2_grpc.py --ignore=E121,E123,E126,E203,E226,E24,E266,E501,E704,W503,W504,I202 --max-line-length=88 .
nox > Session lint-2.7 was successful.
nox > Running session lint-3.9
nox > Creating virtual environment (virtualenv) using python3.9 in .nox/lint-3-9
nox > python -m pip install flake8
nox > flake8 --show-source --builtin=gettext --max-complexity=20 --exclude=.nox,.cache,env,lib,generated_pb2,*_pb2.py,*_pb2_grpc.py --ignore=E121,E123,E126,E203,E226,E24,E266,E501,E704,W503,W504,I202 --max-line-length=88 .
nox > Session lint-3.9 was successful.
nox > Ran multiple sessions:
nox > * tests-2.7: success
nox > * tests-3.9: success
nox > * lint-2.7: success
nox > * lint-3.9: success
$
```
