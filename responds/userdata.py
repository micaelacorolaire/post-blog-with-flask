from pydantic import BaseModel,Field

class userdata(BaseModel):
    id_userdata:str=Field(...,min_length=1)
    name:str=Field(...,min_length=2,max_length=20)
    lastname:str=Field(...,min_length=1,max_length=30)
    age:int=Field(...,gt=18,lt=100)
    nacionality:str=Field(...,min_length=1)
    email:str=Field(...,min_length=1,max_length=320)
    password:str=Field(...,min_length=12,max_length=64)
    nickname:str=Field(...,min_length=1,max_length=10)
    