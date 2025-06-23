FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app
#
#RUN apt-get update \
#    && apt-get install -y gcc libpq-dev curl netcat \
#    && apt-get clean

COPY requirements/base.txt .
RUN pip install --no-cache-dir -r base.txt

COPY . .

#COPY ./entrypoint.sh /entrypoint.sh
#RUN chmod +x /entrypoint.sh

#ENTRYPOINT ["/entrypoint.sh"]
