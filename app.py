import json

with open ("documents.json","r") as file:
    documents = json.load(file)

query = input("Search query: ").lower() 
query_words = query.lower().split()
results = []
for doc in documents:
    doc_words = doc["content"].lower().split()
    tf = 0
    for word in query_words:
        tf += doc_words.count(word)
    results.append((tf, doc))

# Sort results by TF-IDF score in descending order
results.sort(key=lambda x: x[0], reverse=True)

for score, doc in results:
    print("ID:", doc["id"])
    print("Title:", doc["title"])
    print("Score:", score)
    print("------")