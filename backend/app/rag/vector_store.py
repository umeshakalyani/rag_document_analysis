import chromadb

client = chromadb.Client()

collection = client.create_collection(
    name="documents"
)

def store_embeddings(chunks, embeddings):

    for i, chunk in enumerate(chunks):

        collection.add(
            ids=[str(i)],
            documents=[chunk],
            embeddings=[embeddings[i].tolist()]
        )