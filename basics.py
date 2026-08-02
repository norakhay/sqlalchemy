from sqlalchemy.orm import Session
from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String

# engine = create_engine('sqlite:///mydatabase.db', echo=True)
engine = create_engine(
    'sqlite:///satutorialdatabase', echo=True)
meta = MetaData()
conn = engine.connect()
conn.execute(text("CREATE TABLE IF NOT EXISTS people (name str, age int)"))
conn.commit()
# session = Session(engine)
# session.execute(text('INSERT INTO people(name,age) VALUES ("Mike",30);'))
# session.commit()
people = Table(

    "people",
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('age', Integer)
)
meta.create_all(engine)
insert_statement = people.insert().values(name='mike', age=30)
result = conn.execute(insert_statement)
conn.commit()
