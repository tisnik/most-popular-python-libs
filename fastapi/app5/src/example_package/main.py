from fastapi import FastAPI, HTTPException


class Storage:
    def __init__(self):
        self._items = {}
        self._id = 0

    def create(self, text):
        self._id += 1
        self._items[self._id] = text
        return self._id

    def read(self):
        return self._items

    def update(self, id, text):
        self._items[id] = text

    def delete(self, id):
        del self._items[id]


storage = Storage()

app = FastAPI()


@app.post("/create")
async def create_operation(text: str):
    id = storage.create(text)
    return {"created": id}


@app.get("/")
async def read_operation():
    return {"list": storage.read()}


@app.put("/update/{id}")
async def update_operation(id: int, text: str = ""):
    try:
        storage.update(id, text)
        return {"updated": id, "new text": text}
    except Exception:
        raise HTTPException(status_code=404, detail="Item not found")


@app.delete("/delete/{id}")
async def delete_operation(id: int):
    try:
        storage.delete(id)
        return {"deleted": id}
    except Exception:
        raise HTTPException(status_code=404, detail="Item not found")
