from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from strawberry.fastapi import GraphQLRouter
from jinja2 import Template
from pydantic import BaseModel
from .cosmos_client import get_container
import strawberry

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    app.container = await get_container()

@app.get("/", response_class=HTMLResponse)
async def home():
    template = Template("<h1>Welcome to Azure Static Web App with FastAPI!</h1>")
    return template.render()

@app.get("/api/test")
async def test_endpoint():
    return {"message": "I'm alive"}

# Strawberry GraphQL integration
@strawberry.type
class Query:
    @strawberry.field
    async def hello(self, name: str) -> str:
        return f"Hello {name}!"

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")





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


