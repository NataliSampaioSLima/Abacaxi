from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/helloword")
async def root():
    return {"message": "Hello word"}


#portas de entrada diferentes 127.0.0.1:8000/funcsoteste
@app.get("/funcaoteste")

async def funcaoteste():
    return{"teste":True,"numaleatorio": random.randint(0,20000)}