import re
import string
import nltk

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download required resources (runs only once if missing)
try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

try:
    nltk.data.find("corpora/wordnet")
except LookupError:
    nltk.download("wordnet")

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words("english"))


class NLPService:
    def __init__(self) -> None:
        self.lemmatizer = lemmatizer
        self.stop_words = stop_words

    def clean(self, text: str) -> str:
        return clean_text(text)

    def tokenize(self, text: str) -> list[str]:
        return tokenize(text)

    def preprocess(self, text: str) -> str:
        return preprocess(text)

    def preprocess_dataset(self, dataset: list[dict[str, str]]) -> list[str]:
        return preprocess_dataset(dataset)


def clean_text(text):
    """
    Lowercase + remove punctuation + remove extra spaces
    """

    text = text.lower()

    text = re.sub(r"http\S+", "", text)

    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def tokenize(text):
    """
    Tokenize sentence
    """

    return nltk.word_tokenize(text)


def preprocess(text):
    """
    Full preprocessing pipeline
    """

    text = clean_text(text)

    tokens = tokenize(text)

    tokens = [

        lemmatizer.lemmatize(word)

        for word in tokens

        if word not in stop_words

    ]

    return " ".join(tokens)


def preprocess_dataset(dataset):
    """
    Preprocess all FAQ questions
    """

    processed = []

    for item in dataset:

        processed.append(

            preprocess(item["question"])

        )

    return processed