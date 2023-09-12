from pydantic import BaseModel,UUID4

class userdata(BaseModel):
    id_userdata=UUID4
    name=str
    lastname=str
    age=int
    nacionality=str
    email=str
    password=str
    nickname:str