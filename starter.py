from llama_index.core import (VectorStoreIndex, SimpleDirectoryReader)
import logging
import sys  

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents) 


query_engine = index.as_query_engine()
response = query_engine.query("Why did the War actually start?")
print(response)



logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler(stream=sys.stdout))