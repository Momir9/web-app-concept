#!/bin/bash
docker build -t py-app:latest .
docker run -d -p 80:3000 --name py-container-app py-app:latest