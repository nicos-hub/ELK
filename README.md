# ELK

These Python scripts let you interact with an Elasticsearch instance  

## Prerequisites
Scripts use python package elastichsearch, it can be installed with  
```
$ python -m pip install elasticsearch
```

## Connection
### ElasticConnectionUser.py
Establish a connection to Elasticsearch using username and password  
Settings needed:  
* line 25: Elastic HOST and PORT  
* line 26: path to Elastic certificate  
* line 27: Elastic USER and PASSWORD  

### ElasticConnectionAPI.py
Establish a connection to Elasticsearch using API key  
Settings needed:  
* line 26: Elastic HOST and PORT  
* line 27: Elastic API key  
* line 28: path to Elastic certificate  

API KEY can be generate fron Kibana Dev Tools by sending the following request (Set your own API_NAME and INDEX_NAME):  
```
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
```