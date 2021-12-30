# Nebulous Google Cloud serverless &amp; API sample applications
### Run the same apps locally, on App Engine, Cloud Functions, or Cloud Run

## Description

This is the repo for a set apps that demonstrate how to call Google APIs from the serverless platforms available from Google Cloud. Working wth Cloud APIs differs from non-Cloud Google APIs, so that is how the samples are organized (only [Cloud API sample apps](cloud) are available currently). The unique aspect of all of the sample apps is that they can be deployed locally or to any of the [Cloud serverless platforms](https://cloud.google.com/serverless) without any code changes... this is taken care of in configuration.


## Hosting options

Aside from running locally, the app can be deployed to any Cloud serverless platform:

- [App Engine](https://cloud.google.com/appengine) (Standard)
    - Standard source code application deployments (app-hosting in the cloud; "PaaS")
- [Cloud Functions](https://cloud.google.com/functions)
    - Instead of an entire app, this is for cloud-based functions or microservices ("FaaS")
- [Cloud Run](https://cloud.run)
    - Fully-managed serverless container-hosting in the cloud ("CaaS") service

_App Engine_ is for users who wish to deploy a traditional web stack (LAMP, MEAN, etc.) application direct from source without knowledge of containers, Docker, or `Dockerfile`s. _Cloud Run_ is similar but for applications that are explicitly containerized, freeing you from language, library, or binary restrictions. _Cloud Functions_ is for deploying simple microservices like ours, and its Python runtime sends Flask request objects directly to deployed functions.

When running on App Engine or Cloud Functions, this sample app uses the default web server that comes with those services (`gunicorn`). For Cloud Run, developers must start their own web server; this sample app again chooses Flask's development server (but can be configured to your server of choice; `gunicorn` can be enabled if uncommented in the configuration.

A "fourth" product, [App Engine Flexible](https://cloud.google.com/appengine/docs/flexible), which sits somewhere between App Engine Standard and Cloud Run, is out-of-scope for these sample apps at this time.


## Language/web framework options

These are the development languages, supported versions, deployments tested, and selected web frameworks (whose bundled development servers are used for local "deployments"):

Language | Versions | Deployment | Framework
--- | --- | --- | ---
Python|2.7|local, cloud|Flask
Python|3.6+|local, cloud|Flask
Node.js|10, 17|local|Express.js
Node.js|10, 12, 14, 16|cloud|Express.js

The Python apps use the [Flask](https://flask.palletsprojects.com) micro web framework. When deploying locally, the [Flask development server](https://flask.palletsprojects.com/en/master/server) &mdash; also see [its docs](https://flask.palletsprojects.com/server) &mdash; is used. As an application, you're likely to deploy to either App Engine or Cloud Run, depending on whether your app is containerized. Since this "app" only has a single purpose/function, it is also reasonable to deploy it to Cloud Functions. Similarly, [Express.js](https://expressjs.com) is the web framework chosen for the Node.js samples.


## Inspiration and implementation

These code samples were inspired by a [user's suboptimal experience](https://www.mail-archive.com/google-appengine@googlegroups.com/msg94549.html) trying to create a simple App Engine app using a Cloud API. This was followed-up with the realization that we don't have many examples showing users how to access non-Cloud Google APIs from serverless, hence *those* samples.


## Cost

While many Google APIs can be used without fees, use of GCP products &amp; APIs is _not_ free. Certain products do offer an ["Always Free" tier](https://cloud.google.com/free/docs/gcp-free-tier#free-tier-usage-limits) which you have to exceed in order to be billed. Reference any relevant pricing information linked below before doing so.

- [App Engine](https://cloud.google.com/appengine/pricing)
- [Cloud Functions](https://cloud.google.com/functions/pricing)
- [Cloud Run](https://cloud.google.com/run/pricing)
- [Cloud Translation](https://cloud.google.com/translate/pricing)
- [GCP general pricing](https://cloud.google.com/pricing)
- [GCP pricing calculator](https://cloud.google.com/products/calculator)

When enabling services, you may be asked for an active billing account which requires a financial instrument such as a credit card. Reference relevant pricing information before doing so. While Cloud Functions and Cloud Run share a similar Always Free tier and pricing model, App Engine is slightly different.

Furthermore, deploying to GCP serverless platforms incur [minor build and storage costs](https://cloud.google.com/appengine/pricing#pricing-for-related-google-cloud-products). [Cloud Build](https://cloud.google.com/build/pricing) has its own free quota as does [Cloud Storage](https://cloud.google.com/storage/pricing#cloud-storage-always-free). For greater transparency, Cloud Build builds your application image which is then sent to the [Cloud Container Registry](https://cloud.google.com/container-registry/pricing), or [Artifact Registry](https://cloud.google.com/artifact-registry/pricing), its successor; storage of that image uses up some of that (Cloud Storage) quota as does network egress when transferring that image to the service you're deploying to. However you may live in region that does not have such a free tier, so be aware of your storage usage to minimize potential costs. (You may look at what storage you're using and how much, including deleting build artifacts via [your Cloud Storage browser](https://console.cloud.google.com/storage/browser).)

More specific cost information for each sample is available in their respective README files.


## Testing

Each repo has its own testing battery. Refer to each sample app's folder to learn more about the implemented tests.
