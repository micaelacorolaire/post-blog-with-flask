from pydantic import BaseModel,UUID4

class login(BaseModel):
    id_login=UUID4
    email=str
    password=str
    active=bool