from pydantic import BaseModel

class Movie(BaseModel):
    year:int
    time:float
    votes:int