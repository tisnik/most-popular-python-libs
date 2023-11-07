from fastapi import FastAPI
from fastapi import HTTPException

from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker


def connect_to_db():
    url = URL.create(
        drivername="postgresql",
        username="tester",
        password="123qwe",
        host="localhost",
        database="test1",
        port=5432
    )
    print("url", url)

    engine = create_engine(url)
    print("engine", engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    print("session", session)

    return engine, session


engine, session = connect_to_db()


from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Record(Base):
    __tablename__ = "records"

    id = Column(Integer, primary_key=True)
    text = Column(String)


# inicializace
Base.metadata.create_all(engine)

app = FastAPI()


@app.post("/create")
async def create_operation(text: str):
    record = Record(text=text)
    session.add(record)
    session.commit()
    return {"created": record.id}

@app.get("/")
async def read_operation():
    record_query = session.query(Record)
    return {"list": record_query.all()}

@app.put("/update/{id}")
async def update_operation(id: int, text: str = ""):
    record_query = session.query(Record).filter(Record.id==id)
    record = record_query.first()
    record.text = text
    session.add(record)
    session.commit()

@app.delete("/delete/{id}")
async def delete_operation(id: int):
    record = session.query(Record).filter(Record.id==id).first()
    session.delete(record)
    session.commit()
    return {"todo deleted": record.id}
