import json
import math 

with open ("documents.json","r") as file:
    documents = json.load(file)

query = input("Search query: ").lower() 
query_words = query.lower().split()
idf = 0
tf_idf = 0
results_tf= []
results_df = []

for term in query_words:
     df = 0
     for doc in documents:
        if term in doc["content"].lower().split():
            df += 1
     if df != 0:
        idf = math.log(len(documents)/df)
     else:
         idf = 0
     
     for doc in documents:
         doc_words = doc["content"].lower().split()
         tf = 0
         for word in query_words:
             tf += doc_words.count(word)
     tf_idf = idf*tf
     results_df.append((term,df,idf,tf_idf))
for term,df,idf,tf_idf in results_df:
    print(f"Word = {term}\nDF({term}) = {df}\nIDF = {idf:.4f}\ntf-idf = {tf_idf}\n\n")
    

         
