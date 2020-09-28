from leccion1.modelo.modelos import *
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
print(10*"#","leccion 5",10*"#")

an_author= session.query(Author).filter(Author.firstname=="Joanne").one()
print(an_author)
book = Book(
  isbn="98496465",
  title="harry popoter",
  description="vieda de popoter")

book.categories.append(BookCategory(name="Aventura"))
book.categories.append(BookCategory(name="Accion"))

book.author = an_author

print(session.query(Book).filter(Book.categories.any(name="Aventura")).all())

print(session.query(Book).filter(Book.author==an_author).filter(Book.categories.any(name="Aventura")).all())

print(30*"#")

