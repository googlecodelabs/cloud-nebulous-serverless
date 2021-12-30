# Nebulous serverless Cloud Translation API app

## Node.js version

The Node.js version of this app and its deployments are simpler than the Python equivalent, primarily due to the differences between Python 2 and 3, and also because Node.js is not an App Engine legacy runtime. As a result, there is a single Node.js codelab (self-paced, hands-on tutorial) for deploying this app while there are seven for Python.


## Deployments and their files

File | Description
--- | ---
`index.js`|main application file
`package.json`|3rd-party package requirements file
`app.yaml`|App Engine configuration file (only for App Engine deployments)
`credentials.json`|service account public/private key-pair (only for running locally)
`.gcloudignore`|files to exclude deploying to the cloud (administrative)
`README.md`|this file (administrative)

Below are the required settings and instructions for all (documented) deployments; administrative files are not discussed. The `app.yaml` and `credentials.json` files are only used for specific deployments and can be deleted for the others. More regarding `credentials.json`: if/when not provided in Google Cloud deployments, all compute platforms (including serverless) use [default service accounts](https://cloud.google.com/iam/docs/service-accounts#default) which provide a broad set of permissions to assist you in getting a working prototype. When preparing to launch to production, Google Cloud team recommends the best practice of "least privileges," and utilize [user-managed service accounts](https://cloud.google.com/iam/docs/service-accounts#user-managed) with the minimal set of permissions allowing your app to function properly.


## **Local Express server (Node 10, 17)**

**TL;DR:** application files (`index.js` &amp; `package.json`) plus `credentials.json`. Instructions:

1. **Create service account key**, download key file as `credentials.json` in working directory, and set `GOOGLE_APPLICATION_CREDENTIALS` environment variable pointing to it; more about this [here](https://cloud.google.com/docs/authentication/production#manually)
1. **Run** `npm install` (to install packages locally)
1. **Run** `npm start` to run locally


## **App Engine (Node 10, 12, 14, 16)**

**TL;DR:** application files plus `app.yaml`. You may (first) edit `app.yaml` to specify the desired Node version (default: Node 16). Instruction(s):

1. **Run** `gcloud app deploy` to deploy to App Engine


## **Cloud Functions (Node 10, 12, 14, 16)**

**TL;DR:** Uses only the application files. Instruction(s):

1. **Run** `gcloud functions deploy translate --runtime nodejs16 --entry-point app --trigger-http --allow-unauthenticated` to deploy to Cloud Functions (or Node 10, 12, 14)

The command creates &amp; deploys a new HTTP-triggered Cloud Function named `translate`. Cloud Functions is directed to call the application object, `app`, via `--entry-point`. During execution `translate()` is called by `app`. In the [Python version](../python), `--entry-point` is unnecessary because `translate()` *is* the application entry point.


## **Cloud Run (Node 10+ via Cloud Buildpacks)**

**TL;DR:** Uses only the application files. Instruction(s):

1. **Run** `gcloud run deploy translate --allow-unauthenticated --platform managed --source .` to deploy to Cloud Run; optionally add `--region REGION` for non-interactive deploy
    - A `Dockerfile` is optional, but if you wish to create one, place it in the top-level folder so the build system can access it. To get an idea of what to expect, check out the [Python version's `Dockerfile`](../python/Dockerfile).


## References

1. Google Cloud serverless product pages
    - App Engine
        - [App Engine home page](https://cloud.google.com/appengine)
        - [App Engine documentation](https://cloud.google.com/appengine/docs)
        - [Node.js App Engine quickstart](https://cloud.google.com/appengine/docs/standard/nodejs/quickstart)
        - [nodejs App Engine (Standard) runtime](https://cloud.google.com/appengine/docs/standard/nodejs/runtime)
        - [Default service accounts](https://cloud.google.com/appengine/docs/standard/nodejs/service-account)
    - Cloud Functions
        - [Cloud Functions home page](https://cloud.google.com/functions)
        - [Cloud Functions documentation](https://cloud.google.com/functions/docs)
        - [Node.js Cloud Functions quickstart](https://cloud.google.com/functions/docs/quickstart-nodejs)
        - [Default service accounts](https://cloud.google.com/functions/docs/concepts/iam#access_control_for_service_accounts)
    - Cloud Run
        - [Cloud Run home page](https://cloud.run)
        - [Cloud Run documentation](https://cloud.google.com/run/docs)
        - [Node.js Cloud Run quickstart](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/nodejs)
        - [Default service accounts ](https://cloud.google.com/run/docs/securing/service-identity)

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
    - [Cloud Translation Node.js client library (v3)](https://cloud.google.com/translate/docs/reference/libraries/v3/nodejs)
    - [Cloud Translation Node.js client library (v2)](https://cloud.google.com/translate/docs/reference/libraries/v2/nodejs)
    - [Translation API pricing page](https://cloud.google.com/translate/pricing)
    - [All Cloud AI/ML "building block" APIs](https://web.archive.org/web/20210308144225/https://cloud.google.com/products/ai/building-blocks)
    - [Google ML Kit (Cloud AI/ML API subset for mobile)](https://developers.google.com/ml-kit)
    - [Google ML Kit Translation API](https://developers.google.com/ml-kit/language/translation)

1. Other Google Cloud documentation
    - [Google Cloud Node.js support](https://cloud.google.com/nodejs)
    - [Google Cloud client libraries](https://cloud.google.com/apis/docs/cloud-client-libraries)
    - [Google Cloud "Always Free" tier](https://cloud.google.com/free/docs/gcp-free-tier#free-tier-usage-limits)
    - [All Google Cloud documentation](https://cloud.google.com/docs)

1. External links
    - [Express.js](https://expressjs.com)
    - [CNCF Buildpacks open spec](https://buildpacks.io)


## Testing

Testing is driven by [`mocha`](https://mochajs.org) which uses [`supertest`](https://github.com/visionmedia/supertest) for testing and [`eslint`](https://eslint.org) for linting, installing both in virtual environments along with application dependencies, `express`, `nunjucks`, and `@google-cloud/translate`. To run the unit tests (testing `GET` and `POST` requests), run `npm install` followed by `npm test`).


### Expected output

```
$ npm test

> cloud-nebulous-serverless-nodejs@0.0.1 test
> mocha test/test_neb.js

Listening on port 8080


  Our application
    ✔ GET / should result in HTML w/"translate" in the body
    ✔ POST / should have translated "hello world" correctly (140ms)
DONE


  2 passing (170ms)
```

### Troubleshooting

When running the test, there's a situation which resulting in the test hanging like this:

```
$ npm test

> cloud-nebulous-serverless-nodejs@0.0.1 test
> mocha test/test_neb.js

Listening on port 8080


  Our application
    ✔ GET / should result in HTML w/"translate" in the body
    1) POST / should have translated "hello world" correctly
DONE


  1 passing (2s)
  1 failing

  1) Our application
       POST / should have translated "hello world" correctly:
     Error: Timeout of 2000ms exceeded. For async tests and hooks, ensure "done()" is called; if returning a Promise, ensure it resolves. (/tmp/cloud-nebulous-serverless/cloud/nodejs/test/test_neb.js)
      at listOnTimeout (node:internal/timers:557:17)
      at processTimers (node:internal/timers:500:7)

```
*(hangs here)*

If this happens to you, it is because you missed doing one of the following:

- Created a public/private keypair and downloaded the key file as `credentials.json` in working directory
- Set your application default credentials (`GOOGLE_APPLICATION_CREDENTIALS` environment variable) to point to `credentials.json`
