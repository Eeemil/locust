FROM python:3.6.6-alpine3.8

# Install dependencies
ADD requirements.txt /code/
WORKDIR /code/
RUN apk --no-cache add g++ \
        && pip install -r requirements.txt

# Install locust
ADD . /code/
RUN python setup.py egg_info \
        && pip install .

EXPOSE 8089 5557 5558

ENTRYPOINT ["/usr/local/bin/locust"]
