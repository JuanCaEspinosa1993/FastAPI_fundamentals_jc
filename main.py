from fastapi import FastAPI

#Permite correr el proyecto
app = FastAPI()

#path operation. Es un decorador  de función
@app.get("/")
def home():
    return {"Hello": "World"}