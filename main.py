#Python
from typing import Optional
from enum import Enum

#Pydantic
from pydantic import BaseModel
from pydantic import Field

#FastAPI
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()

#Models

class HairColor(Enum):
    white= "white"
    brown ="brown"
    black = "black"
    blonde = "blonde"
    red = "red"

class Location(BaseModel):
    city: str =  Field(
        default=None, 
        min_length=1,
        max_length=20,
        example = "Gudalajara"
          )
    state: str =  Field(
        ..., 
        min_length=1,
        max_length=20,
        example = "Jalisco"
          )
    country: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example = "Mexico"
    )

class Person(BaseModel):
    first_name: str = Field(
        ..., 
        min_length=1,
        max_length=50,
        example = "Jacinto"
          )
    last_name: str = Field(
        ..., 
        min_length=1,
        max_length=50,
        example="Dionicio Patroclo"
          )
    age: int = Field(
        ...,
        gt=0,
        le=115,
        example=20
    )
    hair_color: Optional[HairColor] = Field(default=None, example="red")
    is_married: Optional[bool] = Field(default=None, example=False)

"""    class Config:
        schema_extra = {
            "example" : {
                "first_name": "JuanCa",
                "last_name": "Espinosa Jimenez",
                "age": 20,
                "hair_color": "black",
                "is_married": False
            }
        }"""


@app.get("/")
def home():
    return {"Hello": "World"}

#Request and Response Body

@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person

#validaciones: Query Parameters

@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None, 
        min_length=1, 
        max_length=50, 
        title="Person Name",
        description="This is the person name. It's between 1 and 50 characters",
        example="Furcio"
        ),
    age: str = Query(
        ...,
        title="Person Age",
        description="This is the Person age. It's required",
        example="19"
    )
):
    return {name: age}

#Validaciones: Path Parameters

@app.get("/person/details/{person_id}")
def show_person(
    person_id: int = Path(
        ..., 
        gt=0,
        title="Person ID",
        description="This is the ID Person. It's required",
        example=123
        )
):
    return {person_id: "It exists!"}

#Validaciones: Request Body

@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="Person ID",
        description="This is the person ID",
        gt=0,
        example=123
    ),
    person: Person = Body(...),
    #location: Location = Body(...)
):
    #results = person.dict()
    #results.update(location.dict())
    #return results
    return person