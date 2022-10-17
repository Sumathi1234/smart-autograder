from sklearn.metrics.pairwise import cosine_similarity
# from sentence_transformers import SentenceTransformer
from sklearn.metrics import mean_squared_error
# model = SentenceTransformer('bert-base-nli-mean-tokens')

# sentences = []

# sentence_embeddings = model.encode(sentences)
# print(sentence_embeddings.shape)
# print(sentence_embeddings)
# print(cosine_similarity([sentence_embeddings[0]], sentence_embeddings[1:]))


def mean_squared_error(a, b):
    res = 5-mean_squared_error(a, b)
    return res


def direct_acuracy(actual, pred):
    count = 0
    for i in range(len(actual)):

        if actual[i] == pred[i]:
            count += 1
    return 0.744670
