# specify the parent base image which is the python version 3.7
FROM python:3.7

MAINTAINER rcuevass

# preventing python from writing out pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# preventing python from buffering stdin/stdout
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
    && apt-get -y install gcc make \
    && rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install --no-cache-dir --upgrade pip

# set work directory
WORKDIR /src/app

# copy requirements.txt
COPY ./requirements.txt /src/app/requirements.txt

# install project requirements
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

# Generate pickle file
WORKDIR /src/app/model/training
RUN python training.py

# set work directory
WORKDIR /src/app

# set app port
EXPOSE 8080

# set entry point
ENTRYPOINT [ "python" ]

# run app.py when the container launches
CMD [ "app.py","run","--host","0.0.0.0"]