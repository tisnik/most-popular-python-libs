from fastapi import FastAPI

app = FastAPI()


@app.post("/create")
async def create_operation(text: str):
    return {"created": text}


@app.get("/")
async def read_operation():
    return {"list": None}


@app.put("/update/{id}")
async def update_operation(id: int, text: str = ""):
    pass


@app.delete("/delete/{id}")
async def delete_operation(id: int):
    return {"deleted": id}
