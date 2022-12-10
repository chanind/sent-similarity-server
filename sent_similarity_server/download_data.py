import nltk

from sent_similarity_server.SentenceProcessor import SENT_TRANSFORMER_MODEL
from sentence_transformers import SentenceTransformer

if __name__ == "__main__":
    nltk.download("punkt")
    SentenceTransformer(SENT_TRANSFORMER_MODEL)
