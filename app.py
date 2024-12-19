from fastapi import FastAPI,Depends,HTTPException,status
from sqlalchemy.orm import Session
import models
from database import sql_engine_connector,get_db
from schemas import *
from utils import generate_response_general_agent,generate_content_ollama



app = FastAPI()

models.Base.metadata.create_all(bind=sql_engine_connector)


@app.get('/',status_code=status.HTTP_200_OK)
async def server_status():
    return "Server Running ..."


@app.post('/translate' ,response_model=TranslateResponse, status_code=status.HTTP_201_CREATED)
async def translate_text_to_language(Translate : Translate ,db : Session = Depends(get_db)):
    response = generate_response_general_agent(message=Translate.text,language=Translate.language)
    TranslateDone = models.Translator(text=Translate.text,language=Translate.language,translated=response)
    db.add(TranslateDone)
    db.commit()
    db.refresh(TranslateDone)

    return TranslateDone


@app.post('/Coder',response_model=CoderResponse,status_code=status.HTTP_200_OK)
async def coder(Message:Coder):
    response = generate_content_ollama(**Message.__dict__)
    return response

