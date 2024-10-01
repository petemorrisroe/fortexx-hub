import strawberry
from typing import List
from .api.models import Article as ArticleModel
from .cosmos_db import get_articles, get_article_by_id

@strawberry.experimental.pydantic.type(model=ArticleModel, all_fields=True)
class Article:
    pass

@strawberry.type
class Query:
    articles: List[Article] = strawberry.field(resolver=get_articles)
    article: Article = strawberry.field(resolver=get_article_by_id)

schema = strawberry.Schema(query=Query)
