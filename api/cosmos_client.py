from azure.cosmos import CosmosClient, PartitionKey
import os

client = CosmosClient(os.getenv('COSMOS_URI'), credential=os.getenv('COSMOS_KEY'))
database = client.get_database_client('fortexx')
container = database.get_container_client('article')







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