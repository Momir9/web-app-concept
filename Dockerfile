#Build stage
FROM python:3.14-alpine AS build

WORKDIR /app

COPY requirements.txt .

#Install the Python packages into /install to copy in the runtime stage
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

#Runtime stage
FROM python:3.14-alpine

#Copying installed packages from the build stage
COPY --from=build /install /usr/local
COPY app/ .

# Install runtime dependencies (curl for healthcheck)
RUN apk add --no-cache curl

#Healthcheck, terminate the app if unsuccessful
HEALTHCHECK --interval=30s --start-period=3s --retries=3 \
    CMD curl -f http://localhost:3000/health || exit 1

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]