import json
import math

# Load documents
with open("documents.json", "r") as file:
    documents = json.load(file)

# Get query
query = input("Search query: ").lower()
query_words = query.split()

# Store final results
results = []

# Process each document
for doc in documents:

    doc_words = doc["content"].lower().split()
    score = 0

    print(f"\n===== Document {doc['id']} =====")

    # Process each query term
    for term in query_words:

        # --------------------
        # TF
        # --------------------
        tf = doc_words.count(term)

        # --------------------
        # DF
        # --------------------
        df = 0
        for d in documents:
            d_words = d["content"].lower().split()

            if term in d_words:
                df += 1

        # --------------------
        # IDF
        # --------------------
        if df > 0:
            idf = math.log(len(documents) / df)
        else:
            idf = 0

        # --------------------
        # TF-IDF
        # --------------------
        tf_idf = tf * idf

        # Add to document score
        score += tf_idf

        # Print calculations
        print(f"Term: {term}")
        print(f"TF = {tf}")
        print(f"DF = {df}")
        print(f"IDF = {idf:.4f}")
        print(f"TF-IDF = {tf_idf:.4f}")
        print()

    # Save final score for this document
    results.append((score, doc))

# Sort by score (highest first)
results.sort(key=lambda x: x[0], reverse=True)

print("\n==============================")
print("FINAL RANKING")
print("==============================")

for score, doc in results:
    print(f"Document ID : {doc['id']}")
    print(f"Title       : {doc['title']}")
    print(f"Score       : {score:.4f}")
    print("------------------------------")