from azure.functions import AsgiFunction
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from cosmos_client import get_container
import strawberry
from strawberry.fastapi import GraphQLRouter

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    app.container = await get_container()

@app.get("/", response_class=HTMLResponse)
async def home():
    return "<h1>Welcome to the updated Azure Static Web App with FastAPI!</h1>"

@app.get("/api/test")
async def test_endpoint():
    return {"message": "I'm alive"}

class Article(BaseModel):
    id: str
    title: str
    content: str

@app.get("/api/articles")
async def get_articles():
    container = app.container
    query = "SELECT * FROM c"
    items = [item async for item in container.query_items(query, enable_cross_partition_query=True)]
    return items

@app.post("/api/articles")
async def add_article(article: Article):
    container = app.container
    await container.create_item(body=article.dict())
    return {"message": "Article created successfully"}

# Strawberry GraphQL integration
@strawberry.type
class Query:
    @strawberry.field
    async def hello(self, name: str) -> str:
        return f"Hello {name}!"

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

asgi_app = AsgiFunction(app)

# import strawberry
# from api.models import Article
# from cosmos_db import read_articles, write_article

# @strawberry.type
# class Query:
#     articles: list[Article] = strawberry.field(resolver=read_articles)

# @strawberry.type
# class Mutation:
#     @strawberry.mutation
#     def add_article(self, article: Article) -> str:
#         write_article(article.dict())
#         return "Article added"

# schema = strawberry.Schema(query=Query, mutation=Mutation)


