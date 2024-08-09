################################################################################
# Script name: ElasticConnectionAPI.py
# Author: Nicolas Dolisy
# Date: 2024/05/06
# Input or configuration :  line 26 configure Elastic HOST and PORT
#                           line 27 configure Elastic API key
#                           line 28 configure path to Elastic certificate
# Output: Cluster's info displayed in terminal
# Version: 1.0
# Comment: Establish a connection to Elasticsearch using API key
# Release notes:
################################################################################

from elasticsearch import Elasticsearch
import logging

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to establish a connection to Elasticsearch using username and password
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
     
# Funtion to get and print cluster's information
def get_cluster_info(es_connection):
    if es_connection:
        try:
            info = es_connection.info()
            logger.info(f" Cluster's name: {info['cluster_name']}")
            logger.info(f" Elasticsearch version: {info['version']['number']}")
        except Exception as err:
            logger.error(f" Error getting Elasticsearch information: {err}")

# Connection to Elasticsearch
es_connection = connect_to_elasticsearch()
# If connected get cluster information
if es_connection:
    get_cluster_info(es_connection)