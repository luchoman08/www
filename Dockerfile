 FROM python:2.7
 ENV PYTHONUNBUFFERED 1
 RUN mkdir /webApps
 WORKDIR /webApps
 ADD . /webApps
 RUN pip install -r requirements.txt
