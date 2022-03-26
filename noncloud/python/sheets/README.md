# Nebulous serverless Google Sheets API app

## Python 3 version (Python 2 compatible)

This sample is offered in Python 3, but the code itself is Python 2-compatible. Instructions on running it under 2.x will leverage the resources of the [Cloud API Python sample](https://github.com/googlecodelabs/cloud-nebulous-serverless/tree/main/cloud/python) which provides a more complete experiencce as it has all configuration available to support 2.x deployments.

> NOTES:
> - For local or Cloud Run deployments, there are little/no updates to go from Python 2 to 3.
> - Neither Cloud Functions nor Cloud Run with Cloud Buildpacks support Python 2.


## Deployments and their files

File | Description
--- | ---
[`main.py`](main.py) | main application file
[`templates/index.html`](templates/index.html) | application HTML template
[`requirements.txt`](requirements.txt) | 3rd-party package requirements file
[`app.yaml`](app.yaml) | App Engine configuration file (only for App Engine deployments)
[`.gcloudignore`](.gcloudignore) | files to exclude deploying to the cloud (administrative)
[`noxfile.py`](noxfile.py) |  unit tests `nox` tool setup file
[`test_sheets.py`](test_sheets.py) |  unit tests (`pytest`)
[`Procfile`](Procfile) |  "Entrypoint" directive [Procfile](https://devcenter.heroku.com/articles/procfile) to start app (only for Cloud Run deployments using Cloud Buildpacks)
`README.md` | this file (administrative)

Below are the required settings and instructions for all documented deployments. The "**TL:DR;**" section at the top of each configuration summarizes the key files (see above) while the table beneath spells out the details. No administrative files are listed.


## **Local [Flask](https://flask.palletsprojects.com) server (Python 2 or 3)**

**TL;DR:** application files (`main.py` &amp; `requirements.txt`)

1. **Login using [Application Default Credentials](https://cloud.google.com/docs/authentication/production#automatically)**: run the `gcloud auth application-default login` command and ensure you do **not** set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable; also see the [command ference](https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login).
1. (2.x only) **Uncomment/enable** the line for `google-auth` in `requirements.txt`
1. **Run** `pip install -U pip -r requirements.txt` to install/update packages locally (or `pip2` for Python 2 or `pip3` for Python 3 explicitly)
1. **Run** `python main.py` to run on local Flask server (`python2` or `python3` to be explicit)

**Troubleshooting**: if you're on a VM running `pip install`, you may get an error like this:

```
ERROR: Could not install packages due to an OSError: [Errno 13] Permission denied: 'PKG-INFO'
Consider using the `--user` option or check the permissions.
```

_Solution_: If this is the case:
- **Update** the line for `flask` in `requirements.txt` to: `flask<2.0dev`


## **App Engine (Python 3)**

**TL;DR:** app files plus `app.yaml`

1. **Run** `gcloud app deploy`


## **App Engine (Python 2)**

**TL;DR:** app files plus `app.yaml`, `appengine_config.py`, and `lib`

1. **Copy** the [Cloud API Python 2 `app.yaml` file](/cloud/python/app.yaml)
1. **Copy** the [Cloud API Python 2 `appengine_config.py` file](/cloud/python/appengine_config.py)
1. **Uncomment/enable** the line for `google-auth` in `requirements.txt`
1. **Uncomment** "<1.12.0" on the line for `google-api-python-client` in `requirements.txt`
1. **Run** `pip install -t lib -r requirements.txt` to populate `lib` folder (or `pip2`)
1. **Run** `gcloud app deploy`


## **Cloud Functions (Python 3)**

**TL;DR:** app files

1. **Run** `gcloud functions deploy students --runtime python39 --trigger-http --allow-unauthenticated` to deploy to Cloud Functions (or Python 3.7 or 3.8)

- Cloud Functions does not support Python 2.
- The Cloud Function name must match the function's name in `main.py` else you need to use [`--entry-point`](https://cloud.google.com/functions/docs/deploying/filesystem).


## **Cloud Run (Python 3 via Cloud Buildpacks)**

**TL;DR:** app files plus [`Procfile`](https://devcenter.heroku.com/articles/procfile)

1. **Run** `gcloud run deploy students --allow-unauthenticated --platform managed` to deploy to Cloud Run; optionally add `--source . --region REGION` for non-interactive deploy

- There is no support for Python 2 with Cloud Buildpacks (2.x developers must use Docker)

> **NOTE:** This sample uses the Flask development server by default for prototyping; for production, bundle and deploy a production server like `gunicorn`:
>    1. **Uncomment** `gunicorn` from `requirements.txt` (commented out for App Engine &amp; Cloud Functions)
>    1. **Uncomment** `ENTRYPOINT` entry for `gunicorn` in `Dockerfile` replacing default entry
>    1. Re-use the same deploy command above


## **Cloud Run (Python 3 via Docker)**

**TL;DR:** app files plus `Dockerfile` (nearly identical to Python 2 deployment)

1. **Copy** the [Cloud API Python `Dockerfile` file](/cloud/python/Dockerfile)
1. **Edit** `Dockerfile` and switch the `FROM` entry to the `python:3-slim` base image
1. **Run** `gcloud run deploy students --allow-unauthenticated --platform managed` to deploy to Cloud Run; optionally add `--source . --region REGION` for non-interactive deploy

- The `gunicorn` sidebar above also applies here.


## **Cloud Run (Python 2 via Docker)**

**TL;DR:** app files plus `Dockerfile`

1. **Copy** the [Cloud API Python `Dockerfile` file](/cloud/python/Dockerfile)
1. **Run** `gcloud run deploy students --allow-unauthenticated --platform managed` to deploy to Cloud Run; optionally add `--source . --region REGION` for non-interactive deploy

- The `gunicorn` sidebar above also applies here.


## Resources

These are relevant links only to the app in this folder (for all others, see the [README one level up](../README.md):

### Google Sheets API and platform client library

- [Google Sheets API home page](https://developers.google.com/sheets)
- [Google Sheets API Python QuickStart](https://developers.google.com/sheets/api/quickstart/python) (origin of the student spreadsheet)
- [Google Sheets API intro codelab](http://g.co/codelabs/sheets) (Node.js)
- [Google Sheets API videos](https://developers.google.com/sheets/api/videos) (Python or [Apps Script](https://developers.google.com/apps-script) [JavaScript])
- [Google Workspace APIs home page](https://developers.google.com/gsuite)
- [Google APIs client library for Python](https://github.com/googleapis/google-api-python-client)


### Google Cloud serverless platforms

- [Google Cloud serverless home page](https://cloud.google.com/serverless)
- [Cloud Functions home page](https://cloud.google.com/functions)
- [Cloud Functions Python quickstart](https://cloud.google.com/functions/docs/quickstart-python)
- [Cloud Run home page](https://cloud.run)
- [Cloud Run Python quickstart](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python)
- [App Engine home page](https://cloud.google.com/appengine)
- [App Engine Python 3 quickstart](https://cloud.google.com/appengine/docs/standard/python3/quickstart)
- [App Engine (standard environment) Python 3 runtime](https://cloud.google.com/appengine/docs/standard/python3/runtime)
- [App Engine (standard environment) Python 2 runtime](https://cloud.google.com/appengine/docs/standard/python/runtime)
- [Differences between Python 2 &amp; 3 App Engine (standard environment) runtimes](https://cloud.google.com/appengine/docs/standard/runtimes)
- [App Engine (standard environment) Python 2 to 3 migration guide](http://cloud.google.com/appengine/docs/standard/python/migrate-to-python3)
- [App Engine (standard environment) to Cloud Run codelab tutorial](http://g.co/codelabs/pae-migrate-rundocker) (via Docker)
- [App Engine (standard environment) to Cloud Run codelab tutorial](http://g.co/codelabs/pae-migrate-runbldpks) (no Docker/`Dockerfile` via Cloud Buildpacks)


## Testing

Testing is driven by [`nox`](http://nox.thea.codes) which uses [`pytest`](https://pytest.org) for testing and [`flake8`](https://flake8.pycqa.org) for linting, installing both in virtual environments along with application dependencies, `flask` and `google-api-python-client`, and finally, [`blinker`](https://pythonhosted.org/blinker), a signaling framework integrated into Flask. To run the lint and unit tests (testing `GET` and `POST` requests), install `nox` (with the expected `pip install -U nox`) and run it from the command line in the application folder and ensuring `noxfile.py` is present.


### Expected output

```
$ nox
nox > Running session tests-2.7
nox > Creating virtual environment (virtualenv) using python2.7 in .nox/tests-2-7
nox > python -m pip install pytest blinker flask google-auth google-api-python-client
nox > pytest
================================================== test session starts ==================================================
platform darwin -- Python 2.7.16, pytest-4.6.11, py-1.11.0, pluggy-0.13.1
rootdir: /tmp/noncloud/python/sheets
collected 1 item

test_sheets.py .                                                                                                  [100%]

=============================================== 1 passed in 1.84 seconds ================================================
nox > Session tests-2.7 was successful.
nox > Running session tests-3.8
nox > Creating virtual environment (virtualenv) using python3.8 in .nox/tests-3-8
nox > python -m pip install pytest blinker flask google-auth google-api-python-client
nox > pytest
================================================== test session starts ==================================================
platform darwin -- Python 3.8.2, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /tmp/noncloud/python/sheets
collected 1 item

test_sheets.py .                                                                                                  [100%]

=================================================== 1 passed in 1.04s ===================================================
nox > Session tests-3.8 was successful.
nox > Running session tests-3.9
nox > Creating virtual environment (virtualenv) using python3.9 in .nox/tests-3-9
nox > python -m pip install pytest blinker flask google-auth google-api-python-client
nox > pytest
================================================== test session starts ==================================================
platform darwin -- Python 3.9.1, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: /tmp/noncloud/python/sheets
collected 1 item

test_sheets.py .                                                                                                  [100%]

=================================================== 1 passed in 0.97s ===================================================
nox > Session tests-3.9 was successful.
nox > Running session lint-2.7
nox > Creating virtual environment (virtualenv) using python2.7 in .nox/lint-2-7
nox > python -m pip install flake8
nox > flake8 --show-source --builtin=gettext --max-complexity=20 --exclude=.nox,.cache,env,lib,generated_pb2,*_pb2.py,*_pb2_grpc.py --ignore=E121,E123,E126,E203,E226,E24,E266,E501,E704,W503,W504,I202 --max-line-length=88 .
nox > Session lint-2.7 was successful.
nox > Running session lint-3.8
nox > Creating virtual environment (virtualenv) using python3.8 in .nox/lint-3-8
nox > python -m pip install flake8
nox > flake8 --show-source --builtin=gettext --max-complexity=20 --exclude=.nox,.cache,env,lib,generated_pb2,*_pb2.py,*_pb2_grpc.py --ignore=E121,E123,E126,E203,E226,E24,E266,E501,E704,W503,W504,I202 --max-line-length=88 .
nox > Session lint-3.8 was successful.
nox > Running session lint-3.9
nox > Creating virtual environment (virtualenv) using python3.9 in .nox/lint-3-9
nox > python -m pip install flake8
nox > flake8 --show-source --builtin=gettext --max-complexity=20 --exclude=.nox,.cache,env,lib,generated_pb2,*_pb2.py,*_pb2_grpc.py --ignore=E121,E123,E126,E203,E226,E24,E266,E501,E704,W503,W504,I202 --max-line-length=88 .
nox > Session lint-3.9 was successful.
nox > Ran multiple sessions:
nox > * tests-2.7: success
nox > * tests-3.8: success
nox > * tests-3.9: success
nox > * lint-2.7: success
nox > * lint-3.8: success
nox > * lint-3.9: success
```
