# Web application concept

## Description

Web App Concept is a minimal containerised web application.
It uses FastAPI as the framework, which is performant for building APIs with little syntax.
This is complemented by Uvicorn ASGI server.

## How to build locally

1. git clone https://github.com/Momir9/web-app-concept.git
2. In the root folder find the script docker-build.sh and make it executable with _**chmod -x docker-build.sh**_ .
3. Start the script file with bash **_docker-build.sh_** , it will build the image and start the container
3. In your web browser, you may test the application through:

http://127.0.0.1/metrics  -  This will output the number of requests made by refreshing the page and/or through the HEALTHCHECK found in the Dockerfile
                          
http://127.0.0.1/health   -  This will output the following format {"status": "ok", "timestamp": "20251010T100000Z"}


## Github Actions
The workflow.yml contains a method to log onto GitHub Container Registry using the GITHUB_TOKEN

I have initially tried with both Classic and PAT (fine grain) generated tokens however I was receiving permission related errors in the Push stage.
Once I changed Workflow Permissions in the Action settings, the pipeline went through.


## Other observations

When using the python:3.14-slim image the build time was several seconds however the final image was 146MB, with multiple stages eventually down to ~135MB.
By switching to python:3:14-alpine , the build time was at around 20 seconds with the image being 68MB in size so I went along with that option.
