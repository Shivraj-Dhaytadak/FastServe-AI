from sqlalchemy import Integer,String,Column
from database import Base



class Translator(Base):
    __tablename__ = 'Translations'

    id = Column(Integer,primary_key=True,nullable=False,index=True)
    text = Column(String,nullable=False)
    language = Column(String, nullable=False)
    translated = Column(String,nullable=False)

    