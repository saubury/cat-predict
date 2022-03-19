FROM python:3.8

# do these on one line so changes trigger apt-get update
RUN apt-get update && \
    apt-get install -y python3-pip netcat python-dev python3-dev postgresql

RUN pip install --upgrade pip setuptools
RUN pip install dbt-postgres

RUN useradd -mU dbt_user
USER dbt_user

# I know you are not supposed to do this, it's not very docker-like
ENTRYPOINT ["tail", "-f", "/dev/null"]
