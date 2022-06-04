from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class Repo_Report(Base):
    ...