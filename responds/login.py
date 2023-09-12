from pydantic import BaseModel,Field

class login(BaseModel):
    id_login:str=Field(...,min_length=1)
    email:str=Field(...,min_length=1,max_length=320)
    password:str=Field(...,min_length=8,max_length=128)
    active:bool