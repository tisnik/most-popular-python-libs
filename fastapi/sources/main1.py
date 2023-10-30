from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def origin():
    return {"message": "My first FastAPI app"}
