import strawberry
from typing import List

@strawberry.type
class Article:
    id: str
    title: str
    abstract: str
    body: str

@strawberry.type
class Query:
    articles: List[Article]

    @strawberry.field
    def articles(self) -> List[Article]:
        items = container.read_all_items()
        return [Article(id=item["id"], title=item["title"], abstract=item["abstract"], body=item["body"]) for item in items]

schema = strawberry.Schema(query=Query)
