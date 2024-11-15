from fastapi import FastAPI
from typing import List,Optional
from pydantic import BaseModel

app = FastAPI()
items = []

class item(BaseModel):
    id:Optional[int]=None
    name:str
    description:str
    
    
    class Config:
        orm_mode=True

@app.get('/')
def root():
    return {"message":"afdsflasd"}

@app.get('/item',response_model=List[item])
def item_get():
    return items

if __name__=='__main__':
    import uvicorn
    uvicorn.run()