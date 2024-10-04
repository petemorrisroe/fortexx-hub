import azure.functions as func

# from fasthtml import rt
from fasthtml.common import *
from cosmos_db import read_articles, write_article
from htmx import hx
import uvicorn

app, rt = fast_app()

@rt.get('/test')
async def test(req: HttpRequest) -> HttpResponse:
    return "API is working correctly"

@rt.get('/articles')
async def articles_list(req: HttpRequest) -> HttpResponse:
    articles = [{"title": "Sample Article", "category": "Tech"}]
    return json.dumps(articles)

@rt.post('/articles/add')
async def add_article(req: HttpRequest) -> HttpResponse:
    # Example logic to add an article, simplified for demonstration
    data = req.form
    return f"Article titled '{data.get('title')}' has been added."

if __name__ == "__main__":
    uvicorn.run("api.__init__:app", log_level="info")
