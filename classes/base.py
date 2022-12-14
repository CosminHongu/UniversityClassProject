from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://CAIA:delta1@localhost:5432/CAIA1')

#Creare conexiune noua la baza de date
Session = sessionmaker(bind=engine)

# In base se stocheaza tot ce tine de clase (metadata)
Base = declarative_base()