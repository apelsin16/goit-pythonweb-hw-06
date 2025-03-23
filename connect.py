from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base

DATABASE_URL = "postgresql+psycopg2://postgres:567234@localhost:5432/postgres"

engine = create_engine(DATABASE_URL, echo=True)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

session = Session()
