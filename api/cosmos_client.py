import os
from azure.cosmos.aio import CosmosClient
from azure.cosmos.exceptions import CosmosHttpResponseError

COSMOS_URL = os.getenv("COSMOS_URL")
COSMOS_KEY = os.getenv("COSMOS_KEY")
DATABASE_NAME = "fortexxe"
CONTAINER_NAME = "articles"

async def get_container():
    try:
        client = CosmosClient(COSMOS_URL, credential=COSMOS_KEY)
        database = await client.create_database_if_not_exists(DATABASE_NAME)
        container = await database.create_container_if_not_exists(id=CONTAINER_NAME, partition_key="/id")
        return container
    except CosmosHttpResponseError as e:
        print(f"Error connecting to Cosmos DB: {e.message}")
        raise







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
