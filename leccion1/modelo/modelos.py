from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy import create_engine

engine = create_engine("sqlite:///:memory:")
Base = declarative_base()

class Author(Base):
  __tablename__ = "author"

  id=Column(Integer, Sequence("author_id_seq"), primary_key=True)
  firstname = Column(String)
  lastname = Column(String)
  books = relationship("Book",order_by="Book.id",back_populates="author")  

  def __repr__(self):
    return "{} {}".format(self.firstname,self.lastname)

class Book(Base):
  __tablename__ = "book"
  id=Column(Integer, Sequence("book_id_seq"), primary_key=True)
  isbn = Column(String)
  title = Column(String)
  description = Column(String)
  author_id = Column(String)
  author = relationship("Author",back_populates="books")
  def __repr__(self):
    return "{}".format(self.title)


Base.metadata.create_all(engine)
