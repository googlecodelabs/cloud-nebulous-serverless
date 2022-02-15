# Nebulous serverless Google Maps Geocoding API app
### Python (2 and 3) version

This sample is offered in Python 3, but the code itself is Python 2-compatible. Instructions on running it under 2.x will leverage the resources of the [Cloud API Python sample](https:/tmp/github.com/googlecodelabs/cloud-nebulous-serverless/tree/main/cloud/python) which provides a more complete experiencce as it has all configuration available to support 2.x deployments. The app is tested against Python 2.7, 3.8, and 3.9; see [`Testing`](#testing) below for more information.


> NOTES:
> - For local or Cloud Run deployments, there are little/no updates to go from Python 2 to 3.
> - Neither Cloud Functions nor Cloud Run with Cloud Buildpacks support Python 2.


## Deployments and their files

File | Description
--- | ---
[`main.py`](main.py)|main application file
`settings.py`|settings file with API key (copy &amp; modify `settings-tmpl.py` template)
[`templates/index.html`](templates/index.html)|application HTML template
[`requirements.txt`](requirements.txt)|3rd-party package requirements file
[`app.yaml`](app.yaml)|App Engine configuration file (only for App Engine deployments)
[`.gcloudignore`](.gcloudignore)|files to exclude deploying to the cloud (administrative)
[`noxfile.py`](noxfile.py) |  unit tests `nox` tool setup file
[`test_mapsgeo.py`](test_mapsgeo.py) |  unit tests (`pytest`)
[`Procfile`](Procfile) |  "Entrypoint" directive [Procfile](https:/tmp/devcenter.heroku.com/articles/procfile) to start app (only for Cloud Run deployments using Cloud Buildpacks)
`README.md`|this file (administrative)

Below are the required settings and instructions for all documented deployments. The "**TL:DR;**" section at the top of each configuration summarizes the key files (see above) while the table beneath spells out the details. No administrative files are listed. Create your own `settings.py` file with the API your created in the Cloud console and take precautions to protect it, as outlined in [the Google Maps API key documentation](https://developers.google.com/maps/documentation/javascript/get-api-key).


## **Local [Flask](https://flask.palletsprojects.com) server (Python 2 or 3)**

**TL;DR:** application files (`main.py`, `templates/`, `requirements.txt`)

1. **Run** `pip install -U pip -r requirements.txt` to install/update packages locally (or `pip2` for Python 2 or `pip3` for Python 3 explicitly)
1. **Run** `python main.py` to run on local Flask server (`python2` or `python3` to be explicit)


## **App Engine (Python 3)**

**TL;DR:** app files plus `app.yaml`

1. **Run** `gcloud app deploy`


## **App Engine (Python 2)**

**TL;DR:** `app2.yaml` (instead of `app.yaml`), app files plus `appengine_config.py`, and `lib`, and other modifications

1. **Copy** the [Cloud API Python 2 `appengine_config.py` file](/blob/main/cloud/python/appengine_config.py)
1. **Uncomment/enable** `requests-toolbelt` in `requirements.txt`
1. **Run** `pip install -t lib -r requirements.txt` to populate `lib` folder (or `pip2`)
1. **Edit** `lib/googlemaps/client.py` by adding `import requests_toolbelt.adapters.appengine; requests_toolbelt.adapters.appengine.monkeypatch()` below `import requests` (as documented [here](https://cloud.google.com/appengine/docs/standard/python/issue-requests#requests))
1. **Run** `gcloud app deploy app2.yaml`


## **Cloud Functions (Python 3)**

**TL;DR:** app files

1. **Run** `gcloud functions deploy mapsgeo --runtime python39 --trigger-http --allow-unauthenticated` to deploy to Cloud Functions (or Python 3.7 or 3.8)

- Cloud Functions does not support Python 2.
- The Cloud Function name (here `mapsgeo`) must match the function's name in `main.py` else you need to use [`--entry-point`](https://cloud.google.com/functions/docs/deploying/filesystem).


## **Cloud Run (Python 3 via Cloud Buildpacks)**

**TL;DR:** app files plus [`Procfile`](https://devcenter.heroku.com/articles/procfile)

1. **Run** `gcloud run deploy mapsgeo --allow-unauthenticated --platform managed` to deploy to Cloud Run; optionally add `--source . --region REGION` for non-interactive deploy

- There is no support for Python 2 with Cloud Buildpacks (2.x developers must use Docker [see below])

> **NOTE:** This sample uses the Flask development server by default for prototyping; for production, bundle and deploy a production server like `gunicorn`:
>    1. **Uncomment** `gunicorn` from `requirements.txt` (commented out for App Engine &amp; Cloud Functions)
>    1. **Uncomment** `ENTRYPOINT` entry for `gunicorn` in `Dockerfile` replacing default entry
>    1. Re-use the same deploy command above


## **Cloud Run (Python 3 via Docker)**

**TL;DR:** app files plus `Dockerfile` (nearly identical to Python 2 deployment)

1. **Copy** the [Cloud API Python `Dockerfile` file](/blob/main/cloud/python/Dockerfile)
1. **Edit** `Dockerfile` and switch the `FROM` entry to the `python:3-slim` base image
1. **Run** `gcloud run deploy mapsgeo --allow-unauthenticated --platform managed` to deploy to Cloud Run; optionally add `--source . --region REGION` for non-interactive deploy

- The `gunicorn` sidebar above also applies here.


## **Cloud Run (Python 2 via Docker)**

**TL;DR:** app files plus `Dockerfile`

1. **Copy** the [Cloud API Python `Dockerfile` file](/blob/main/cloud/python/Dockerfile)
1. **Run** `gcloud run deploy mapsgeo --allow-unauthenticated --platform managed` to deploy to Cloud Run; optionally add `--source . --region REGION` for non-interactive deploy

- The `gunicorn` sidebar above also applies here.


## References

These are relevant links only to the app in this folder (for all others, see the [README one level up](../README.md):

- [Google Maps client library for Python](https://github.com/googlemaps/google-maps-services-python)
- [Google Maps API key documentation](https://developers.google.com/maps/documentation/javascript/get-api-key)
- [Python 3 App Engine quickstart](https://cloud.google.com/appengine/docs/standard/python3/quickstart)
- [Python 3 App Engine (standard environment) runtime](https://cloud.google.com/appengine/docs/standard/python3/runtime)
- [Python 2 App Engine (standard environment) runtime](https://cloud.google.com/appengine/docs/standard/python/runtime)
- [Python Cloud Functions quickstart](https://cloud.google.com/functions/docs/quickstart-python)
- [Python Cloud Run quickstart](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/python)
- [Differences between Python 2 &amp; 3 App Engine (standard environment) runtimes](https://cloud.google.com/appengine/docs/standard/runtimes)
- [Python 2 to 3 App Engine (standard environment) migration guide](http://cloud.google.com/appengine/docs/standard/python/migrate-to-python3)
- [App Engine (standard environment) to Cloud Run codelab tutorial](http://g.co/codelabs/pae-migrate-rundocker) (Docker)
- [App Engine (standard environment) to Cloud Run codelab tutorial](http://g.co/codelabs/pae-migrate-runbldpks) (Cloud Buildpacks)


## Testing

Testing is driven by [`nox`](http://nox.thea.codes) which uses [`pytest`](https://pytest.org) for testing and [`flake8`](https://flake8.pycqa.org) for linting, installing both in virtual environments along with application dependencies, `flask` and [`googlemaps`](https://github.com/googlemaps/google-maps-services-python) and finally, [`blinker`](https://pythonhosted.org/blinker), a signaling framework integrated into Flask. To run the lint and unit tests (testing `GET` and `POST` requests), install `nox` (with the expected `pip install -U nox`) and run it from the command line in the application folder and ensuring `noxfile.py` is present.

### Expected output

```
$ nox
nox > Running session tests-2.7
nox > Creating virtual environment (virtualenv) using python2.7 in .nox/tests-2-7
nox > python -m pip install pytest blinker flask googlemaps
nox > pytest
=============================================== test session starts ================================================
platform darwin -- Python 2.7.16, pytest-4.6.11, py-1.11.0, pluggy-0.13.1
rootdir: /tmp/noncloud/python/maps
collected 4 items

test_mapsgeo.py ....                                                                                         [100%]

============================================= 4 passed in 2.69 seconds =============================================
nox > Session tests-2.7 was successful.
nox > Running session tests-3.8
nox > Creating virtual environment (virtualenv) using python3.8 in .nox/tests-3-8
nox > python -m pip install pytest blinker flask googlemaps
nox > pytest
=============================================== test session starts ================================================
platform darwin -- Python 3.8.2, pytest-7.0.1, pluggy-1.0.0
rootdir: /tmp/noncloud/python/maps
collected 4 items

test_mapsgeo.py ....                                                                                         [100%]

================================================ 4 passed in 1.26s =================================================
nox > Session tests-3.8 was successful.
nox > Running session tests-3.9
nox > Creating virtual environment (virtualenv) using python3.9 in .nox/tests-3-9
nox > python -m pip install pytest blinker flask googlemaps
nox > pytest
=============================================== test session starts ================================================
platform darwin -- Python 3.9.9, pytest-7.0.1, pluggy-1.0.0
rootdir: /tmp/noncloud/python/maps
collected 4 items

test_mapsgeo.py ....                                                                                         [100%]

================================================ 4 passed in 1.05s =================================================
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
