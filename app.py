import json

with open ("documents.json","r") as file:
    documents = json.load(file)

query = input("Search query: ").lower() 
query_words = query.lower().split()
results_tf= []
results_df = []

for doc in documents:
    doc_words = doc["content"].lower().split()
    tf = 0
    for word in query_words:
        tf += doc_words.count(word)
    results_tf.append((tf, doc))

# Sort results by TF-IDF score in descending order
results_tf.sort(key=lambda x: x[0], reverse=True)

for score, doc in results_tf:
    print("ID:", doc["id"])
    print("Title:", doc["title"])
    print("Score:", score)
    print("------")

fquery_words = query.lower().split()

for query1 in query_words:
     df = 0
     for doc in documents:
        if query1 in doc["content"].lower().split():
            df += 1
     results_df.append((query1,df))
for i,o in results_df:
    print(f"DF({i}) = {o}/{len(documents)}")
    

         
