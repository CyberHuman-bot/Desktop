from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to APIdog!"}

@app.get("/dog/{name}")
def get_dog(name: str):
    return {"dog_name": name, "status": "happy"}

# Run the API with: uvicorn main:app --reload
