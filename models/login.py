from sqlalchemy import Column,Integer,String,ForeignKey,UUID4
from models.base import BaseModel

class login(BaseModel):
    __tablename__='login'
    __args__={'schema':'Public'}
    id_login=Column(str,primary_key=True,null=False)
    email=Column(str,null=False)
    password=Column(str,null=False)
    active=Column(bool,null=False)