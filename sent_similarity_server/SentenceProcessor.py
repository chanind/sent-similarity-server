from __future__ import annotations

from typing import Any
import spacy
import numpy as np
import numpy.typing as npt
from numpy.linalg import norm
from sentence_transformers import SentenceTransformer
from ltp import StnSplit


SENT_TRANSFORMER_MODEL = "paraphrase-multilingual-MiniLM-L12-v2"


class SentenceProcessor:

    zh_zplitter: Any
    en_splitter: spacy.language.Language
    encoder: SentenceTransformer

    def __init__(self) -> None:
        self.zh_splitter = StnSplit()
        self.en_splitter = spacy.load("xx_sent_ud_sm")
        self.encoder = SentenceTransformer(SENT_TRANSFORMER_MODEL)

    def split_sentences(self, text: str) -> list[str]:
        if is_zh(text):
            return self.zh_splitter.split(text)
        else:
            return [sent.text for sent in self.en_splitter(text).sents]

    def encode_sentences(self, sentences: list[str]) -> npt.NDArray[np.float32]:
        encoded = self.encoder.encode(sentences)
        return encoded / norm(encoded, axis=1, keepdims=True)


def is_zh(text: str) -> bool:
    for ch in text:
        if "\u4e00" <= ch <= "\u9fff":
            return True
    return False
