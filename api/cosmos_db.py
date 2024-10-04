from azure.cosmos import CosmosClient
import os

COSMOS_URL = os.getenv('COSMOS_URL')
COSMOS_KEY = os.getenv('COSMOS_KEY')

# Initialize CosmosClient with a dictionary containing the key
client = CosmosClient(COSMOS_URL, {'masterKey': COSMOS_KEY})

DATABASE_NAME = "fortexx"
CONTAINER_NAME = "article"

database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

def read_articles():
    return list(container.read_all_items())

def write_article(article):
    container.create_item(body=article)
