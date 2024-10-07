from azure.functions import AsgiFunction
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from strawberry.fastapi import GraphQLRouter
from cosmos_client import get_container
import strawberry

app = FastAPI()

@app.on_event("startup")
async def startup_db_client():
    app.container = await get_container()

@app.get("/", response_class=HTMLResponse)
async def home():
    return "<h1>Welcome to the Articles Application</h1>"

@app.get("/api/test")
async def test_endpoint():
    return {"message": "I'm alive"}

# Article Model
class Article(BaseModel):
    id: str
    title: str
    content: str

# Endpoint to get all articles
@app.get("/api/articles")
async def get_articles():
    container = app.container
    query = "SELECT * FROM c"
    items = []
    async for item in container.query_items(query, enable_cross_partition_query=True):
        items.append(item)
    return items

# Endpoint to add a new article
@app.post("/api/articles")
async def add_article(article: Article):
    container = app.container
    try:
        await container.create_item(body=article.dict())
        return JSONResponse(status_code=201, content={"message": "Article created successfully"})
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

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


