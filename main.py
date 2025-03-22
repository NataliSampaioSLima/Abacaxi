from fastapi import FastAPI

app = FastAPI()

@app.get("/helloword")
async def root():
    return {"message": "Hello word"}

#portas de entrada diferentes
@app.get("/funcaoteste")
async def funcaoteste():
    return{"teste":"Deu certo graças a Deus!"}