################################################################################
# Script name: ElasticCreateIndex.py
# Author: Nicolas Dolisy
# Date: 2024/05/13
# Input or configuration :  line 41 configure Elastic host and port
#                           line 42 configure Elastic API key
#                           line 43 configure path to Elastic certificate
# Output: Create index in elastic and display index mapping on screen
# Version: 1.0
# Comment: 
# Release notes:
################################################################################

from elasticsearch import Elasticsearch
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Index name
index_name = 'index-test'

# Index mapping
mapping = {
    "mappings": {
        "properties": {
            "@timestamp": { "type": "date" },
            "text_field": {"type": "text"},
            "long_field1": {"type": "long"},
            "long_field2": {"type": "long"}
        }
    }
}

# Function to establish a connection to Elasticsearch using API
def connect_to_elasticsearch():
    try:
        # Elasticsearch configuration
        es_connection = Elasticsearch(
            ["https://HOST:PORT"],
            api_key="APIKEY",
            ca_certs="/PATH/TO/http_ca.crt",
            verify_certs=True  # False for an autosigned certifcate
        )
        
        if es_connection.ping():
            logger.info(" Connected to Elasticsearch")
            return es_connection
        else:
            logger.error(" Failed connection to Elasticsearch")
            return None
    except Exception as err:
        logger.error(f" Error during Elasticsearch connection: {err}")
        return None

# Connection to Elasticsearch
es_connection = connect_to_elasticsearch()
# If connected create index
if es_connection:
    if not es_connection.indices.exists(index=index_name):
        es_connection.indices.create(index=index_name, body=mapping)
        print(f"Index '{index_name}' creation successful")
    else:
        print(f"Index '{index_name}' already exists")

# Mapping check
index_mapping = es_connection.indices.get_mapping(index=index_name)
print("Index mapping :", index_mapping)