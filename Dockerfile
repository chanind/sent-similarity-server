FROM python:3.10

RUN pip install poetry

WORKDIR /code

COPY pyproject.toml /code/
COPY poetry.lock /code/
RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

COPY demo/server/requirements.txt /code/
RUN pip install -r requirements.txt

COPY . .

# switch to non-root user
RUN adduser --system --group app
USER app

RUN python -m demo.server.download_data

ENV PORT=8080
EXPOSE ${PORT}

CMD gunicorn --bind :$PORT --workers 1 --threads 1 --timeout 120 demo.server.app:app