from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "python flask web framework",
    "python programming language",
    "football sport game",
    "python flask tutorial"
]

query = input("Search: ")

# -------------------------
# Step 1: Combine query + documents
# -------------------------
all_texts = documents + [query]

# -------------------------
# Step 2: Convert text → TF-IDF vectors
# -------------------------
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(all_texts)

# -------------------------
# Step 3: Split query vector
# -------------------------
doc_vectors = tfidf_matrix[:-1]
query_vector = tfidf_matrix[-1]

# -------------------------
# Step 4: Cosine similarity
# -------------------------
scores = cosine_similarity(query_vector, doc_vectors)[0]

# -------------------------
# Step 5: Rank results
# -------------------------
results = list(zip(scores, documents))
results.sort(reverse=True)

print("\nResults:\n")

for score, doc in results:
    print(f"{score:.4f} | {doc}")