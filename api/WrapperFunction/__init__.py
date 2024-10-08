import fastapi

app = fastapi.FastAPI()

@app.get("/test")
async def test_endpoint():
    return {"message": "I'm alive"}
    