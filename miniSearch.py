documents = [
    "python flask web framework",
    "python programming language",
    "football sport game"
]

query = input("Search query: ").lower().split()
print("Query terms:", query)
def score(doc):
    doc_term = doc.lower().split()
    total = 0
    for w in query:
        if w in doc_term:
            total += 1
    return total
results = sorted(documents,key=score,reverse=True)
print(results)