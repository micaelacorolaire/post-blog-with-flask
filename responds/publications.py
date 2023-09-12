from pydantic import BaseModel,Field
class publications(BaseModel):
    id_publications:str=Field(...,min_length=1)
    title:str=Field(...,min_length=5,max_length=50)
    content:str=Field(...,min_length=500,max_length=1000)
    pub_date:str=Field(...,min_length=5,max_length=25)
    author:str=Field(...,min_length=1)