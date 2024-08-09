# ELK

## Connection
### ElasticConnectionUser.py
Establish a connection to Elasticsearch using username and password
Configuration needed:
    line 25 configure Elastic HOST and PORT
    line 26 configure path to Elastic certificate
    line 27 configure Elastic USER and PASSWORD

### ElasticConnectionAPI.py
Establish a connection to Elasticsearch using API key
    Configuration needed:
        line 26 configure Elastic HOST and PORT
        line 27 configure Elastic API key
        line 28 configure path to Elastic certificate

API KEY can be generate fron Kibana Dev Tools by sending the following request (Set your own API_NAME and INDEX_NAME):
'''
POST /_security/api_key
{
"name": "API_NAME",
"expiration": "365d",   
"role_descriptors": { 
    "role-a": {
    "cluster": ["all"],
    "indices": [
        {
        "names": ["INDEX_NAME"],
        "privileges": ["all"]
        }
    ]
    }
}
}
'''