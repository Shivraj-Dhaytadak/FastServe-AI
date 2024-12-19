from pydantic import BaseModel,Json
from typing import List

class Translate(BaseModel):
    text: str
    language : str 
    class Config:
        from_attributes=True

class TranslateResponse(Translate):
    translated : str 
    class Config:
        from_attributes=True

class Coder(BaseModel):
    prompt:str
    tokens:int
    class Config:
        from_attributes=True

class CoderResponse(BaseModel):
    response: Json
    class Config:
        from_attributes=True

class CoderOutput(BaseModel):
    code : str
    explanation:str
