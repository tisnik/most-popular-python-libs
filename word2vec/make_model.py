import string
import nltk
from nltk.corpus import brown
from gensim.models import Word2Vec

nltk.download('brown', quiet=True)
nltk.download('punkt', quiet=True)

# načtení korusu
document = brown.sents()

# filtrace slov, které nezačínají písmenem
data = []
for sent in document:
    new_sent = []
    for word in sent:
        cleaned = word.lower()
        if cleaned and cleaned[0] not in string.punctuation:
            new_sent.append(cleaned)
    if new_sent:
        data.append(new_sent)

# korpus byl vyčištěn
print(f"Corpus size: {len(data)} sentences")

# trénink modelu
model = Word2Vec(
    sentences=data,
    vector_size=200,
    window=5,
    min_count=3,
    workers=16,
    sg=1,
    epochs=50,
)

# informace o modelu
print(f"Vocabulary size: {len(model.wv)} words")

# uložení modelu pro další použití
model.save("word2vec_brown.model")
