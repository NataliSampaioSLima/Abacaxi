from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello word"}

#portas de entrada diferentes
@app.get("/teste1")
async def funcaoteste():
    return{"teste":"Deu certo graças a Deus!"}