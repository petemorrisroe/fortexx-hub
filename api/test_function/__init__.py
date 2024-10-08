import fastapi

app = fastapi.FastAPI()

@app.on_event("startup")
async def startup_event():
    print("Function App starting up...")
    
@app.get("/test")
async def test_endpoint():
    return {"message": "I'm alive"}
