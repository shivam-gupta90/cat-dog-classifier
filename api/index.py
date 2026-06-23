from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Cat Dog Classifier API is running"}