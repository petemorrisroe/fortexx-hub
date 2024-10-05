from fasthtml.common import *
from .schema import schema
from .cosmos_client import container
from .models import Article
from pydantic import ValidationError

app, rt = fast_app()

@app.get('/api/articles')
def list_articles():
    items = container.read_all_items()
    return Div(*[Div(H3(item["title"]), P(item["abstract"])) for item in items])

@app.post('/api/articles')
def create_article(title: str, abstract: str, body: str):
    try:
        # Use Pydantic to validate the data
        article_data = ArticleModel(title=title, abstract=abstract, body=body)
        new_article = {
            "id": f"fx{len(container.read_all_items()) + 1}",
            "title": article_data.title,
            "abstract": article_data.abstract,
            "body": article_data.body
        }
        container.create_item(new_article)
        return Div(H3(new_article["title"]), P(new_article["abstract"]))
    except ValidationError as e:
        return Div(P(f"Error: {e}"))

@app.route('/graphql')
def graphql(request):
    return schema.execute_sync(request.body.decode())

if __name__ == '__main__':
    serve()




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


