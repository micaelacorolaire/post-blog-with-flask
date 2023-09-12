from sqlalchemy import Column,Integer,String,ForeignKey,UUID4
from models.base import BaseModel
from sqlalchemy import relationship

class userdata(BaseModel):
    __tablename__='userdata'
    __args__={'schema':'public'}
    id_user=Column(str,primary_key=True,null=False)
    name=Column(str,null=False)
    lastname=Column(str,null=False)
    age=Column(int,null=False)
    nickname=Column(str,null=False)
    userdata=(relationship('login',backpopulates=[id_login]))
