from __future__ import annotations
from typing import Any

from flask import Flask, request, abort
from flask_cors import CORS

from sent_similarity_server.SentenceProcessor import SentenceProcessor

app = Flask(__name__)
CORS(app)


processor = SentenceProcessor()


@app.errorhandler(400)
def handle_error(error: Any) -> Any:
    return error.description, 400


@app.route("/")
def index() -> dict[str, Any]:
    return {"name": "Sentence Similarity Server"}


@app.route("/split-sentences", methods=["POST"])
def split_sentences() -> dict[str, Any]:
    json_data = request.json
    if not json_data:
        abort(
            400,
            {
                "type": "invalid_params",
                "message": 'You must post a JSON body with a "texts" param',
            },
        )
    texts = json_data.get("texts")
    if texts is None or len(texts) == 0:
        abort(
            400,
            {
                "type": "invalid_params",
                "message": 'You must post a "texts" param',
            },
        )
    results = []
    for text in texts:
        results.append({"text": text, "sentences": processor.split_sentences(text)})
    return {"results": results}


@app.route("/encode-sentences", methods=["POST"])
def encode_sentences() -> dict[str, Any]:
    json_data = request.json
    if not json_data:
        abort(
            400,
            {
                "type": "invalid_params",
                "message": 'You must post a JSON body with a "sentences" param',
            },
        )
    sentences = json_data.get("sentences")
    if sentences is None or len(sentences) == 0:
        abort(
            400,
            {
                "type": "invalid_params",
                "message": 'You must post a "sentences" param',
            },
        )
    return {"results": {"embeddings": processor.encode_sentences(sentences).tolist()}}
