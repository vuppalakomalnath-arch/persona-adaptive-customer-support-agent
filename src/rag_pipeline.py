import os

from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)


def load_documents():

    documents = []

    data_path = "data"

    for file in os.listdir(data_path):

        file_path = os.path.join(data_path, file)

        if file.endswith(".txt"):

            loader = TextLoader(file_path)

            documents.extend(loader.load())

        elif file.endswith(".pdf"):

            loader = PyPDFLoader(file_path)

            documents.extend(loader.load())

    return documents


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    return splitter.split_documents(documents)


def get_embedding_model():

    return HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )


def create_vector_db(chunks):

    embeddings = get_embedding_model()

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

    return vectordb


def retrieve(query):

    embeddings = get_embedding_model()

    vectordb = Chroma(
        persist_directory="chroma_db",
        embedding_function=embeddings
    )

    results = vectordb.similarity_search_with_score(
        query,
        k=3
    )

    return results


if __name__ == "__main__":

    docs = load_documents()

    print(f"Documents Loaded: {len(docs)}")

    chunks = split_documents(docs)

    print(f"Chunks Created: {len(chunks)}")

    create_vector_db(chunks)

    print("Vector Database Created")

    results = retrieve(
        "How do I reset my password?"
    )

    print("\nRetrieved Results:\n")

    for idx, doc in enumerate(results, start=1):

        print(f"\nResult {idx}")

        print(doc.page_content)

        print("-" * 60)