from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello word"}

#portas de entrada diferentes 127.0.0.1:8000/teste1
@app.get("/teste")
async def funcaoteste():
    return{"teste":True,"numaleatorio": random.randint(0,1000)}