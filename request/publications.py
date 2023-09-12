from pydantic import BaseModel,UUID4

class publications(BaseModel):
    id_publications=UUID4
    title=str
    content=str
    pub_date=str
    author=str