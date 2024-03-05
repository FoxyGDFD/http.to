FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY . .

RUN chmod +x ./docker-entrypoint.sh && \
    pip install --upgrade pip && \
    pip install -r ./requirements.txt

CMD /app/docker-entrypoint.sh