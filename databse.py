
import mysql.connector
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://root:manager@localhost:3306/bci')

sessionlocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

Base = declarative_base()




