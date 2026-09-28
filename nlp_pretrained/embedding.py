# Text ---> Machine understand numbers ---> (TF-IDF, GLOVE, GENSIM, FASTTEXT), Advance(huggingface
#transformer(All-MiniLM-L6-v2), google(generativeembedding, gemini embedding))

import sys
from typing import Any
import gensim.downloader as api
from src.exception import CustomException
from src.logger import get_logger

logger = get_logger(__name__)

model = None
MODEL_NAME = "glove-wiki-gigaword-50"


def _get_model() -> str | Any:
    global model
    if model is None:
        logger.info(f"Loading pretrained Model for Embeddings: {MODEL_NAME}")
        model = api.load(MODEL_NAME)
        logger.info(f"Embeddings Loaded , Vocabulary size: {len(model.index_to_key)}")
    return model


def most_similar_words(word: str, topn: int = 5) -> list | None:
    try:
        model = _get_model()
        word = word.lower()
        if word not in model:
            logger.info(f" '{word}' was not found in voucabulary.")
            return []

        results = model.most_similar(word, topn=topn)
        logger.info(f"Most Similar to '{word}' : '{results}'")
        return results

    except Exception as e:
        raise CustomException(e, sys)


def word_similarity(word1: str, word2: str) -> float:
    try:
        model = _get_model()
        score = float(model.similarity(word1.lower(), word2.lower()))
        logger.info(f"Similarity('{word1}', '{word2}') = {score:.3f}")
        return score

    except Exception as e:
        raise CustomException(e, sys)