# Nebulous Google Cloud serverless &amp; API sample application
### Run your own "Google Translate" locally, on App Engine, Cloud Functions, or Cloud Run

## Description

This is a "nebulous" sample app that demonstrates the flexibility of _where_ you can run your apps. With minor tweaks to the configuration, this app can be deployed eight different ways:

1. Local Flask server (Python 2)
1. Local Flask server (Python 3)
1. Google App Engine (Python 2)
1. Google App Engine (Python 3)
1. Google Cloud Functions (Python 3)
1. Google Cloud Run (Python 2 via Docker)
1. Google Cloud Run (Python 3 via Docker)
1. Google Cloud Run (Python 3 via Cloud Buildpacks)

Admittedly, there's a bit of "cheating" due to the duplicity of Python 2 and 3, esp. since the application is compatible across both without modification nor use of compatibility libraries. However, those familiar with the differences in App Engine across both runtimes have internalized a greater significance.


### App

This app shows developers how to use a Google Cloud service (API) from one of the serverless compute platforms. Specifically, the API demonstrated is the [Cloud Translation API](https://cloud.google.com/translate), the API for [Google Translate](https://translate.google.com) and one of Google Cloud's [AI/ML building block" APIs](https://cloud.google.com/products/ai/building-blocks). It implements a simplistic English-to-Spanish "Google Translate" website.

### Services

The app uses the [Flask](https://flask.palletsprojects.com) micro web framework. When deploying locally, Flask's development server is used. The app can also be configured for deployment to one of a pair of [Google Cloud serverless](https://cloud.google.com/serverless) application-hosting platforms, [App Engine](https://cloud.google.com/appengine) (Standard) or [Cloud Run](https://cloud.google.com/run). Since this "app" only has a single purpose/function, it is also reasonable to deploy it to [Cloud Functions](https://cloud.google.com/functions).

App Engine is for users who wish to deploy a traditional web stack-based (LAMP, MEAN, etc.) application direct from source without knowledge of containers, Docker, nor `Dockerfile`s. Cloud Run is similar but for applications that are explicitly containerized. You can deploy pre-existing containers or build-and-deploy direct from source as well, but without language, library, or binary restrictions. Cloud Functions is for deploying simple functions or microservices like this and automatically sends Flask request objects to the deployed function (see compatibility line in `main.py`.)

When running on App Engine or Cloud Functions, this sample app uses the default web server that comes with those services (`gunicorn`). For Cloud Run, developers must start their own web server; this sample app again chooses Flask's development server (but can be configured to your server of choice).


### Service account credentials ("local-only")

The credentials JSON file &mdash; call it anything you like, but we're using the name `credentials.json` &mdash; is only used when running locally to specify the service account used to talk to Cloud APIs. Developers are prompted to download it after [creating a service account key-pair](https://console.cloud.google.com/iam-admin/serviceaccounts/create). Check out the documentation for [service accounts](https://cloud.google.com/docs/authentication/getting-started) and the [service account public/private key/pairs](https://cloud.google.com/translate/docs/setup#service_account_and_private_key).

Why just locally? For simplicity, this sample app uses [default service accounts](https://cloud.google.com/iam/docs/service-accounts#default) when deploying to the cloud, so neither the service account key-pair created for local deployment nor its `credentials.json` will be used in those cases. In other words, if not deploying/testing locally, you don't have to create a service account key.

However, while we suggest you "delete" `credentials.json` and not use it when deploying to the cloud ("finding credentials automatically"), you can disregard that advice and opt to use that service account key-pair ("passing credentials manually") if desired as long as you point to those credentials. Read more about these options in the [documentation](https://cloud.google.com/docs/authentication/production).


### Cloud project ID

The `settings.py` file is to avoid publicly-exposing your `PROJECT_ID` if you're sharing or presenting the main application file `main.py`. Set your Cloud project ID to that variable. You can find it from the Cloud Console <https://console.cloud.google.com> on your "Project info" dashboard card, or click on the "snowman" triple dots to the left of your avatar in the upper-right of the Cloud Console. Do *not* use the project name or the project number, just the project ID.


### Cost

While many Google APIs can be used without fees, use of Google Cloud (Platform) products &amp; APIs is _not_ free. Certain Google Cloud Platform (GCP) products do offer an ["Always Free" tier](https://cloud.google.com/free/docs/gcp-free-tier#always-free) for which you have to exceed in order to incur billing. For the purposes of the codelab, while the Translation API does not explicitly list a free tier on that page, [its pricing information](https://cloud.google.com/translate/pricing) states each project gets a half-million character free quota applied as a credit, so each character translated by the API counts against that free tier, and so long as you stay within its limits in aggregate (within each month), you should not incur any additional charges. When enabling the Cloud Translation API, you may be asked for an active billing account, so reference that pricing information before doing so.


### Deployments

Below are the required settings and instructions to deploy this app for all available configurations. Note the application files `main.py` and `settings.py` are always required as is the package `requirements.txt` config file &mdash; none edited. The "**TL:DR;**" section at the top of each deployment type summarizes the configuration while the table beneath it spells out all the detail.


## **Local Flask server (Python 2)**

- **TL;DR:** application files plus `credentials.json`

File | Description
--- | ---
`settings.py`|**ensure** `PROJECT_ID` set correctly
`main.py`|**use as-is** from repo
`credentials.json`|JSON credentials file (described above)
`app.yaml`|_unused_ (delete or leave as-is)
`appengine_config.py`|_unused_ (delete or leave as-is)
`requirements.txt`|_unused_ (delete or leave as-is; packages should be installed locally however)
`lib`|**delete** (or rename) this folder if it exists (not used with Flask)
`Dockerfile`|_unused_ (delete or leave as-is)
`Procfile`|_unused_ (delete or leave as-is)

- **Run** `python main.py` to run on local Flask server (or `python2`)


## **Local Flask server (Python 3)**

- **TL;DR:** identical to Flask Python 2 deployment above (application is Python 2 &amp; 3-compatible)
- **Run** `python main.py` to run on local Flask server (or `python3`)


## **App Engine (Python 2)**

- **TL;DR:** app files plus `app.yaml`, `appengine_config.py`, and `lib`

File | Description
--- | ---
`settings.py`|**ensure** `PROJECT_ID` set correctly
`main.py`|**use as-is** from repo
`credentials.json`|**delete** (or rename) this file if it exists
`app.yaml`|**use as-is** from repo (ensure `#runtime:python38` commented out)
`appengine_config.py`|**use as-is** from repo
`requirements.txt`|**use as-is** from repo (used to install `lib` but _unused_ thereafter)
`lib`|**run command** `pip install -t lib -r requirements.txt` to populate
`Dockerfile`|_unused_ (delete or leave as-is)
`Procfile`|_unused_ (delete or leave as-is)

- **Run** `gcloud app deploy` to deploy to Python 2 App Engine


## **App Engine (Python 3)**

- **TL;DR:** app files plus `app.yaml` and `requirements.txt`

File | Description
--- | ---
`settings.py`|**ensure** `PROJECT_ID` set correctly
`main.py`|**use as-is** from repo
`credentials.json`|**delete** (or rename) this file
`app.yaml`|**uncomment** `runtime:python38` and **delete all other lines** (can also use 3.7 or 3.9)
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
`settings.py`|**ensure** `PROJECT_ID` set correctly
`main.py`|**use as-is** from repo
`credentials.json`|**delete** (or rename) this file
`app.yaml`|**delete** (or rename) this file (not used with Cloud Functions)
`appengine_config.py`|**delete** (or rename) this file (not used with Cloud Functions)
`requirements.txt`|**use as-is** from repo
`lib`|**delete** (or rename) this folder if it exists (not used with Cloud Functions)
`Dockerfile`|_unused_ (delete or leave as-is)
`Procfile`|_unused_ (delete or leave as-is)

- **Run** `gcloud functions deploy translate --runtime python38 --trigger-http --allow-unauthenticated` to deploy to Cloud Functions (can also use 3.7 or 3.9)
- The above command creates and deploys a brand new HTTP-triggered Cloud Function; name must match what's in `main.py`.


## **Cloud Run (Python 2 via Docker)**

- **TL;DR:** app files plus `requirements.txt` and `Dockerfile`

File | Description
--- | ---
`settings.py`|**ensure** `PROJECT_ID` set correctly
`main.py`|**use as-is** from repo
`credentials.json`|**delete** (or rename) this file
`app.yaml`|**delete** (or rename) this file (not used with Cloud Run)
`appengine_config.py`|**delete** (or rename) this file (not used with Cloud Run)
`requirements.txt`|**use as-is** from repo
`lib`|**delete** (or rename) this folder if it exists (not used with Cloud Run)
`Dockerfile`|**use as-is** from repo (ensure `#FROM python:3-slim` commented out)
`Procfile`|_unused_ (delete or leave as-is)

- **Run** `gcloud run deploy SVC_NAME --source .` to deploy to Cloud Run after you decide on a service name (`SVC_NAME`)
- The above command wraps `docker build` and `docker push`, deploying the image to [Cloud Artifact Registry](https://cloud.google.com/artifact-registry), and finally `docker run` to deploy the service, all in one convenient command.
- Can also use this clickable shortcut to deploy to Cloud Run:

[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run)


## **Cloud Run (Python 3 via Docker)**

- **TL;DR:** app files plus `requirements.txt` and `Dockerfile`

File | Description
--- | ---
`Dockerfile`|**replace** `FROM python:2-slim` with `FROM python:3-slim` (commented out) &amp; **keep all other lines**

- All other files the same as Cloud Run Python 2 via Docker above
- **Run** `gcloud run deploy SVC_NAME --source .` to deploy to Cloud Run after you decide on a service name (`SVC_NAME`)
- The shortcut deploy button can be made for Python 3 if you make the `Dockerfile` update above and commit it to your fork/clone.


## **Cloud Run (Python 3 via Cloud Buildpacks)**

- **TL;DR:** app files plus `requirements.txt`

File | Description
--- | ---
`Dockerfile`|**delete** (or rename) this file (containers/Docker/`Dockerfile` knowledge unnecessary)
`Procfile`|**use as-is** from repo

- All files identical to Docker deployments except _with_ [`Procfile`](https://devcenter.heroku.com/articles/procfile) and _no_ `Dockerfile`
- There is no support for Python 2 with Cloud Buildpacks; 2.x developers must use Docker
- **Run** `gcloud run deploy SVC_NAME --source .` to deploy to Cloud Run after you decide on a service name (`SVC_NAME`)


## References

1. Google Cloud and other Google product pages
    - App Engine
        - [App Engine home page](https://cloud.google.com/appengine)
        - [App Engine documentation](https://cloud.google.com/appengine/docs)
        - [Python App Engine quickstart](https://cloud.google.com/appengine/docs/standard/python3/quickstart)
        - [Default service accounts for App Engine](https://cloud.google.com/appengine/docs/standard/python3/service-account)
        - [Python 2 App Engine (Standard) runtime](https://cloud.google.com/appengine/docs/standard/python/runtime)
        - [Python 3 App Engine (Standard) runtime](https://cloud.google.com/appengine/docs/standard/python3/runtime)
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
        - [Cloud Buildpacks announcement](https://cloud.google.com/blog/products/containers-kubernetes/google-cloud-now-supports-buildpacks)
        - [Cloud Buildpacks repo](https://github.com/GoogleCloudPlatform/buildpacks)
        - [Cloud Artifact Registry home page](https://cloud.google.com/artifact-registry)
        - [Cloud Artifact Registry documentation](https://cloud.google.com/artifact-registry/docs)
    - AI/ML APIs
        - [Cloud Translation home page](https://cloud.google.com/translate)
        - [Cloud Translation documentation](https://cloud.google.com/translate/docs)
        - [Translation API pricing page](https://cloud.google.com/translate/pricing)
        - [All Cloud AI/ML "building block" APIs](https://cloud.google.com/products/ai/building-blocks)
        - [Google ML Kit (Cloud AI/ML APIs subset for mobile)](https://developers.google.com/ml-kit)
        - [Google ML Kit Translation API](https://developers.google.com/ml-kit/language/translation)
    - Other documentation
        - [Google Cloud Python support](https://cloud.google.com/python)
        - [Google Cloud client libraries](https://cloud.google.com/apis/docs/cloud-client-libraries)
        - [Google Cloud "Always Free" tier](https://cloud.google.com/free/docs/gcp-free-tier#always-free)
        - [All Google Cloud documentation](https://cloud.google.com/docs)

1. App Engine migration between runtimes/platforms
    - [Differences between Python 2 &amp; 3 App Engine (Standard) runtimes](https://cloud.google.com/appengine/docs/standard/runtimes)
    - [Python 2 to 3 App Engine (Standard) migration guide](http://cloud.google.com/appengine/docs/standard/python/migrate-to-python3)
    - [App Engine (Standard) to Cloud Run codelab tutorial](http://g.co/codelabs/pae-migrate-rundocker) (Docker)
    - [App Engine (Standard) to Cloud Run codelab tutorial](http://g.co/codelabs/pae-migrate-runbldpks)

1. External links
    - [Flask](https://flask.palletsprojects.com)
    - [Docker](https://docker.com)
    - [`Dockerfile` documentation](https://docs.docker.com/engine/reference/builder)
    - [`Dockerfile` best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices)
    - [CNCF Buildpacks open spec](https://buildpacks.io)
