FROM python:3.8.10
ENV PYTHONUNBUFFERED 1
WORKDIR /ecommerce
ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY requirements.txt /ecommerce/requirements.txt
RUN pip install -r requirements.txt
COPY . /ecommerce/