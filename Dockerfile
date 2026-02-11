#Alternatively use alpine, but would need to install curl separately
FROM python:3.14.3-slim

WORKDIR /app

COPY app/requirements.txt .
RUN pip install -r requirements.txt 

COPY app/ .

EXPOSE 3000

HEALTHCHECK --interval=30s --start-period=5s --retries=3 CMD curl http://localhost:3000/health

CMD ["python","main.py"]