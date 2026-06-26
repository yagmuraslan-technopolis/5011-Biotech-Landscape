from llama_index.readers.azstorage_blob import AzStorageBlobReader
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential

from uuid import uuid4
from openai import AzureOpenAI

from dotenv import load_dotenv
import os
from llama_index.core.node_parser import SentenceSplitter

from llama_index.core import Settings, VectorStoreIndex
from llama_index.embeddings.azure_inference import AzureAIEmbeddingsModel

load_dotenv()

connection_string=os.environ.get("AZURE_BLOB_CONNECTION_STRING")
container_name="new3"
AZURE_SEARCH_SERVICE=os.environ.get("AZURE_AI_SEARCH_ENDPOINT")
AZURE_SEARCH_API_KEY = os.environ.get("AZURE_AI_SEARCH_API_KEY")



credential = AzureKeyCredential(AZURE_SEARCH_API_KEY)


## Approach 1:

# Setup
reader = AzStorageBlobReader(
    connection_string=connection_string,
    container_name=container_name
)
documents = reader.load_data()

splitter = SentenceSplitter(chunk_size=1024, chunk_overlap=200)
nodes = splitter.get_nodes_from_documents(documents)



client = AzureOpenAI(
  api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version = "2023-05-15",
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
)

def get_embeddings(text, model="text-embedding-ada-002"): # model = "deployment_name"
    return client.embeddings.create(input = text, model=model).data[0].embedding


# Prepare documents for Azure AI Search
azure_docs = []

for node in nodes:
    embedding = get_embeddings(node.text)
    azure_docs.append({
        "parent_id": str(uuid4()),
        "title": node.metadata.get("file_name", "Untitled"),
        "locations": [],
        "chunk_id": str(uuid4()),
        "chunk": node.text,
        "text_vector": embedding
    })


# Upload to Azure AI Search
search_client = SearchClient(
    endpoint=AZURE_SEARCH_SERVICE,
    index_name="py-rag-tutorial-index",
    credential=AzureKeyCredential(AZURE_SEARCH_API_KEY)
)
result = search_client.upload_documents(documents=azure_docs)
for r in result:
    if not r.succeeded:
        print(f"Failed to upload doc ID {r.key}: {r.error_message}")
    else:
        print(f"Uploaded doc ID {r.key}") # TODO: Take into account waiting time.

print("upload complete")

"""
##Aproach 2:


embed_model = AzureAIEmbeddingsModel(
    endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    credential=credential,
)

Settings.embed_model = embed_model

reader = AzStorageBlobReader(
    connection_string=connection_string,
    container_name=container_name
)
documents = reader.load_data()
index = VectorStoreIndex.from_documents(documents)"""