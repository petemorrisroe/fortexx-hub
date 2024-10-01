import strawberry
from typing import List
from database import get_articles, get_article, create_article, update_article, delete_article
from api.models import Article

@strawberry.type
class Query:
    @strawberry.field
    def articles(self, skip: int = 0, limit: int = 10) -> List[Article]:
        return get_articles(skip, limit)

    @strawberry.field
    def article(self, id: str) -> Article:
        return get_article(id)

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_article(self, article: Article) -> bool:
        create_article(article.dict())
        return True

    @strawberry.mutation
    def update_article(self, id: str, article: Article) -> bool:
        update_article(id, article.dict())
        return True

    @strawberry.mutation
    def delete_article(self, id: str) -> bool:
        delete_article(id)
        return True

schema = strawberry.Schema(query=Query, mutation=Mutation)
