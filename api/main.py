from fastapi import FastAPI

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    return "<h1>Welcome to the Articles Application</h1>"

@app.get("/api/test")
async def test_endpoint():
    return {"message": "I'm alive"}

# @app.get("/api/test")
# async def test_endpoint():
#     return {"message": "I'm alive"}


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


