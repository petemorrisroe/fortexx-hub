from pydantic import BaseModel

class Article(BaseModel):
    title: str
    category: str
    abstract: str
    body: str
    tags: list[str]
