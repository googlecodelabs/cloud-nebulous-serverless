# Nebulous serverless Cloud Translation API app

## Python (2 and 3) version

While the majority of this app's deployments are in Python 3, there are still users upgrading from Python 2, so our Python 2 code is meant to help with migration &amp; planning. Admittedly, there may _seem_ to be a bit of "cheating" due to the duplicity of Python 2 and 3, especially since the application is compatible across both language versions without modification or use of compatibility libraries. However there are significant differences between Python 2 and 3 deployment requirements irregardless of language differences. Additional notes:

- For local or Cloud Run deployments, there are little/no updates to go from Python 2 to 3.
- Neither Cloud Functions nor Cloud Run with Cloud Buildpacks support Python 2.
- There is also an [equivalent Node.js version](../nodejs) of this app.


## Codelab links

Deployment | Python 2 | Python 3
--- | --- | ---
Local/hosted Flask|[codelab](https://codelabs.developers.google.com/codelabs/cloud-nebulous-serverless-python-flask?utm_source=codelabs&utm_medium=et&utm_campaign=CDR_wes_aap-serverless_nebservflask_sms_201020&utm_content=-)|_same as Python 2_
App Engine|[codelab](https://codelabs.developers.google.com/codelabs/cloud-nebulous-serverless-python-gae2?utm_source=codelabs&utm_medium=et&utm_campaign=CDR_wes_aap-serverless_nebservgae2_sms_201020&utm_content=-)|[codelab](https://codelabs.developers.google.com/codelabs/cloud-nebulous-serverless-python-gae3?utm_source=codelabs&utm_medium=et&utm_campaign=CDR_wes_aap-serverless_nebservgae3_sms_201020&utm_content=-)
Cloud Functions| _N/A_ |[codelab](https://codelabs.developers.google.com/codelabs/cloud-nebulous-serverless-python-gcf?utm_source=codelabs&utm_medium=et&utm_campaign=CDR_wes_aap-serverless_nebservgcf_sms_201020&utm_content=-)
Cloud Run (Docker)|[codelab](https://codelabs.developers.google.com/codelabs/cloud-nebulous-serverless-python-gcr2?utm_source=codelabs&utm_medium=et&utm_campaign=CDR_wes_aap-serverless_nebservgcr2_sms_201020&utm_content=-)|[codelab](https://codelabs.developers.google.com/codelabs/cloud-nebulous-serverless-python-gcr3?utm_source=codelabs&utm_medium=et&utm_campaign=CDR_wes_aap-serverless_nebservgcr3_sms_201020&utm_content=-)
Cloud Run (Buildpacks)| _N/A_ |[codelab](https://codelabs.developers.google.com/codelabs/cloud-nebulous-serverless-python-gcrbp?utm_source=codelabs&utm_medium=et&utm_campaign=CDR_wes_aap-serverless_nebservgcrbp_sms_201020&utm_content=-)


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

> NOTE: Serverless deployments (as configured here) use [default service accounts](https://cloud.google.com/iam/docs/service-accounts#default) which provide a broad set of permissions to assist you in getting a working prototype. When preparing to launch to production, the Google Cloud team recommends the best practice of "least privileges," and instead use [user-managed service accounts](https://cloud.google.com/iam/docs/service-accounts#user-managed) with the minimal set of permissions allowing your app to function properly.


## **Local Flask server (Python 2)**

**TL;DR:** application files (`main.py` &amp; `requirements.txt`)

File | Description
--- | ---
`main.py`|**use as-is** from repo
`app.yaml`|_unused_ (delete or leave as-is)
`appengine_config.py`|_unused_ (delete or leave as-is; only for Python 2 App Engine)
`requirements.txt`|**use as-is** to install packages locally (see below) but _unused_ thereafter
`lib`|_unused_ (delete or leave as-is if it exists)
`Dockerfile`|_unused_ (delete or leave as-is)
`Procfile`|_unused_ (delete or leave as-is)

Instructions:

1. **Run** `pip install -U pip -r requirements.txt` to install/update packages locally (or `pip2`)
1. **Run** `gcloud auth application-default login` to set your credentials
1. **Run** `python main.py` to run on local Flask server (or `python2`)


## **Local Flask server (Python 3)**

**TL;DR:** app files (identical to Python 2 deployment)

File | Description
--- | ---
`main.py`|**use as-is** from repo
`app.yaml`|_unused_ (delete or leave as-is)
`appengine_config.py`|_unused_ (delete or leave as-is; only for Python 2 App Engine)
`requirements.txt`|**use as-is** to install packages locally (see below) but _unused_ thereafter
`lib`|_unused_ (delete or leave as-is if it exists)
`Dockerfile`|_unused_ (delete or leave as-is)
`Procfile`|_unused_ (delete or leave as-is)

Instructions:

1. **Run** `pip install -U pip -r requirements.txt` to install/update packages locally (or `pip3`)
1. **Run** `gcloud auth application-default login` to set your credentials
1. **Run** `python main.py` to run on local Flask server (or `python3`)


## **App Engine (Python 2)**

**TL;DR:** app files plus `app.yaml`, `appengine_config.py`, and `lib`

File | Description
--- | ---
`main.py`|**use as-is** from repo
`app.yaml`|**use as-is** from repo (ensure `#runtime:python39` commented out)
`appengine_config.py`|**use as-is** from repo
`requirements.txt`|**use as-is** to install packages locally (see below) but _unused_ thereafter
`lib`|**create folder** per instructions below
`Dockerfile`|_unused_ (delete or leave as-is)
`Procfile`|_unused_ (delete or leave as-is)

Instructions:

1. **Run** `pip install -t lib -r requirements.txt` to populate `lib` folder (or `pip2`)
1. **Run** `gcloud app deploy` to deploy to Python 2 App Engine


## **App Engine (Python 3)**

**TL;DR:** app files plus `app.yaml`

File | Description
--- | ---
`main.py`|**use as-is** from repo
`app.yaml`|**uncomment** `runtime:python39` (or Python 3.7 or 3.8); **delete** all other lines
`appengine_config.py`|_unused_ (delete or leave as-is; only for Python 2 App Engine)
`requirements.txt`|**use as-is** from repo
`lib`|**delete** (or rename) this folder if it exists (not used with Python 3 App Engine)
`Dockerfile`|_unused_ (delete or leave as-is)
`Procfile`|_unused_ (delete or leave as-is)

Instructions:

1. **Edit** `app.yaml` (see above); optionally **delete** `lib` and `appengine_config.py` (unused)
1. **Run** `gcloud app deploy` to deploy to Python 3 App Engine


## **Cloud Functions (Python 3)**

**TL;DR:** app files

File | Description
--- | ---
`main.py`|**use as-is** from repo
`app.yaml`|_unused_ (delete or leave as-is; only for App Engine)
`appengine_config.py`|_unused_ (delete or leave as-is; only for Python 2 App Engine)
`requirements.txt`|**use as-is** from repo
`lib`|**delete** (or rename) this folder if it exists (not used with Cloud Functions)
`Dockerfile`|_unused_ (delete or leave as-is)
`Procfile`|_unused_ (delete or leave as-is)

Instructions:

1. (optionally) **Delete** `app.yaml`, `lib` and `appengine_config.py` (unused)
1. **Run** `gcloud functions deploy translate --runtime python39 --trigger-http --allow-unauthenticated` to deploy to Cloud Functions (or Python 3.7 or 3.8)
    - That command creates &amp; deploys a new HTTP-triggered Cloud Function (name must match what's in `main.py`)
1. There is no support for Python 2 with Cloud Functions


## **Cloud Run (Python 2 via Docker)**

**TL;DR:** app files plus `Dockerfile`

File | Description
--- | ---
`main.py`|**use as-is** from repo
`app.yaml`|_unused_ (delete or leave as-is; only for App Engine)
`appengine_config.py`|_unused_ (delete or leave as-is; only for Python 2 App Engine)
`requirements.txt`|**uncomment** `grpcio==1.39.0`
`lib`|**delete** (or rename) this folder if it exists (not used with Cloud Run)
`Dockerfile`|**use as-is** from repo (ensure `#FROM python:3-slim` commented out)
`Procfile`|_unused_ (delete or leave as-is)

Instructions:

1. (optionally) **Delete** `app.yaml`, `lib` and `appengine_config.py` (unused)
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

**TL;DR:** app files plus `Dockerfile` (nearly identical to Python 2 deployment)

File | Description
--- | ---
`main.py`|**use as-is** from repo
`app.yaml`|_unused_ (delete or leave as-is; only for App Engine)
`appengine_config.py`|_unused_ (delete or leave as-is; only for Python 2 App Engine)
`requirements.txt`|**use as-is** from repo
`lib`|**delete** (or rename) this folder if it exists (not used with Cloud Run)
`Dockerfile`|**replace** `FROM python:2-slim` with `FROM python:3-slim` (commented out) but **keep all other lines**
`Procfile`|_unused_ (delete or leave as-is)

Instructions:

1. (optionally) **Delete** `app.yaml`, `lib` and `appengine_config.py` (unused)
1. **Edit** `Dockerfile` (see above)
1. **Run** `gcloud run deploy translate --allow-unauthenticated --platform managed` to deploy to Cloud Run; optionally add `--region REGION` for non-interactive deploy
1. The shortcut "button" above can be customized for Python 3 if you make the `Dockerfile` update above and commit it to your fork/clone.
1. By default, App Engine &amp; Cloud Functions launch production servers; with Cloud Run, the Flask development server is used for prototyping. For production, bundle and deploy a production server like `gunicorn`:
    1. **Uncomment** `gunicorn` from `requirements.txt` (commented out for App Engine &amp; Cloud Functions)
    1. **Uncomment** the `ENTRYPOINT` entry for `gunicorn` replacing the default entry in `Dockerfile`
    1. Re-use the same deploy command


## **Cloud Run (Python 3 via Cloud Buildpacks)**

**TL;DR:** app files plus [`Procfile`](https://devcenter.heroku.com/articles/procfile)

File | Description
--- | ---
`main.py`|**use as-is** from repo
`app.yaml`|_unused_ (delete or leave as-is; only for App Engine)
`appengine_config.py`|_unused_ (delete or leave as-is; only for Python 2 App Engine)
`requirements.txt`|**use as-is** from repo
`lib`|**delete** (or rename) this folder if it exists (not used with Cloud Run)
`Dockerfile`|**delete** (or rename) this file (_required_)
`Procfile`|**use as-is** from repo

Instructions:

1. **Delete** `Dockerfile` (or rename it)
1. (optionally) **Delete** `app.yaml`, `lib` and `appengine_config.py` (unused)
1. There is no support for Python 2 with Cloud Buildpacks (2.x developers must use Docker)
1. **Run** `gcloud run deploy translate --allow-unauthenticated --platform managed` to deploy to Cloud Run; optionally add `--region REGION` for non-interactive deploy
1. By default, App Engine &amp; Cloud Functions launch production servers; with Cloud Run, the Flask development server is used for prototyping. For production, bundle and deploy a production server like `gunicorn`:
    1. **Uncomment** `gunicorn` from `requirements.txt` (commented out for App Engine &amp; Cloud Functions)
    1. **Uncomment** the `web:` entry for `gunicorn` replacing the default entry in `Procfile`
    1. Re-use the same deploy command


## References

These are relevant links only to the app in this folder (for all others, see the [README one level up](../README.md):

- [Python 3 App Engine quickstart](https://cloud.google.com/appengine/docs/standard/python3/quickstart)
- [Python 3 App Engine (standard environment) runtime](https://cloud.google.com/appengine/docs/standard/python3/runtime)
- [Python 2 App Engine (standard environment) runtime](https://cloud.google.com/appengine/docs/standard/python/runtime)
- [Python Cloud Functions quickstart](https://cloud.google.com/functions/docs/quickstart-python)
- [Python Cloud Run quickstart](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python)
- [Differences between Python 2 &amp; 3 App Engine (standard environment) runtimes](https://cloud.google.com/appengine/docs/standard/runtimes)
- [Python 2 to 3 App Engine (standard environment) migration guide](http://cloud.google.com/appengine/docs/standard/python/migrate-to-python3)
- [App Engine (standard environment) to Cloud Run codelab tutorial](http://g.co/codelabs/pae-migrate-rundocker) (Docker)
- [App Engine (standard environment) to Cloud Run codelab tutorial](http://g.co/codelabs/pae-migrate-runbldpks) (Cloud Buildpacks)
- [Flask](https://flask.palletsprojects.com)


## Testing

Testing is driven by [`nox`](http://nox.thea.codes) which uses [`pytest`](https://pytest.org) for testing and [`flake8`](https://flake8.pycqa.org) for linting, installing both in virtual environments along with application dependencies, `flask` and `google-cloud-translate`, and finally, `blinker`, a signaling framework integrated into Flask. To run the lint and unit tests (testing `GET` and `POST` requests), install `nox` (with the expected `pip install -U nox`) and run it from the command line in the application folder and ensuring `noxfile.py` is present.

### Expected output

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
