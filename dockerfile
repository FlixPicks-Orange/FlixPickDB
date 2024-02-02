FROM python:3
WORKDIR /home/Docker/back
COPY requirements.txt ./
RUN python -m pip install -r requirements.txt
COPY . .
EXPOSE 3000
CMD ["python", "./app.py"]
