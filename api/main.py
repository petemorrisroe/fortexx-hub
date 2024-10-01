import strawberry
from api.models import Article
from cosmos_db import read_articles, write_article

@strawberry.type
class Query:
    articles: list[Article] = strawberry.field(resolver=read_articles)

@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_article(self, article: Article) -> str:
        write_article(article.dict())
        return "Article added"

schema = strawberry.Schema(query=Query, mutation=Mutation)
