from langchain_aws import BedrockEmbeddings

def get_embedding_function():
    embedding = BedrockEmbeddings()
    return embedding
