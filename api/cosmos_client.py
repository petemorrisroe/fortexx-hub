from azure.cosmos.aio import CosmosClient
from azure.cosmos import PartitionKey
import os

URI = os.getenv("COSMOS_URI")
KEY = os.getenv("COSMOS_KEY")

cosmos_client = CosmosClient(URI, credential=KEY)
database_name = "my-database"
container_name = "articles"

async def get_container():
    database = await cosmos_client.create_database_if_not_exists(id=database_name)
    container = await database.create_container_if_not_exists(
        id=container_name, partition_key=PartitionKey(path="/id")
    )
    return container








# from azure.cosmos import CosmosClient
# import os


# # Now you can access your variables from the environment
# COSMOS_URL = os.getenv('COSMOS_URL')
# COSMOS_KEY = os.getenv('COSMOS_KEY')


# DATABASE_NAME = 'fortexx'
# CONTAINER_NAME = 'article'

# # Provide the key directly
# client = CosmosClient(COSMOS_URL, credential={'masterKey': COSMOS_KEY})
# database = client.get_database_client(DATABASE_NAME)
# container = database.get_container_client(CONTAINER_NAME)

# def read_articles():
#     return list(container.read_all_items())

# def write_article(article):
#     container.create_item(body=article)
