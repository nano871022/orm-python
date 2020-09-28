from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Sequence, ForeignKey, Table, Text
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship

engine = create_engine("sqlite:///:memory:")
Base = declarative_base()

class Author(Base):
  __tablename__ = "author"

  id=Column(Integer, Sequence("author_id_seq"), primary_key=True)
  firstname = Column(String)
  lastname = Column(String)
  books = relationship("Book",order_by="Book.id",back_populates="author", cascade="all, delete, delete-orphan")  

  def __repr__(self):
    return "{} {}".format(self.firstname,self.lastname)

book_categories = Table(
  "book_categories",
  Base.metadata,
  Column("book_id",ForeignKey("book.id"), primary_key=True),
  Column("category_id", ForeignKey("book_category.id"), primary_key=True))
    

class Book(Base):
  __tablename__ = "book"
  id=Column(Integer, Sequence("book_id_seq"), primary_key=True)
  isbn = Column(String)
  title = Column(String)
  description = Column(String)
  author_id = Column(Integer, ForeignKey("author.id"))
  author = relationship("Author",back_populates="books")
  categories = relationship("BookCategory", secondary=book_categories,back_populates="books")

  def __repr__(self):
    return "{}".format(self.title)

class BookCategory(Base):
  __tablename__ = "book_category"
  id = Column(Integer, Sequence("book_category_id_seq"), primary_key=True)
  name = Column(String)
  books = relationship("Book",secondary=book_categories, back_populates="categories")

  def __repr__(self):
    return "{}".format(self.name)


Base.metadata.create_all(engine)
