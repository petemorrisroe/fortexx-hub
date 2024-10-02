import azure.functions as func
from fasthtml import HTMLTemplateResponse, rt
from fasthtml.common import *

from cosmos_db import read_articles, write_article
from htmx import hx

app, rt = fast_app()

@rt("/articles")
async def articles_list(req: func.HttpRequest) -> func.HttpResponse:
    articles = read_articles()
    return HTMLTemplateResponse("article_list.html", {"articles": articles})

@rt("/articles/add", methods=["GET", "POST"])
async def add_article(req: func.HttpRequest) -> func.HttpResponse:
    if req.method == "POST":
        data = req.form
        write_article(data)
        return hx.redirect("/articles")
    return HTMLTemplateResponse("article_form.html")

@rt.get('/test')
async def test_endpoint(req: HttpRequest) -> HttpResponse:
    return HttpResponse("Test successful! The API is working.", status_code=200)


