from sqlalchemy import Column,Integer,String,ForeignKey,UUID4
from models.base import BaseModel
from sqlalchemy import Relationship
from models.login import login
class publications(BaseModel):
    __tablename__='publications'
    __args__={'schema':'public'}
    id_publications=Column(str,primary_key=True)
    title=Column(str,null=False)
    content=Column(str,null=False)
    pub_date=Column(str,null=False)
    publications=(Relationship('login',backpopulates=[id_login]))