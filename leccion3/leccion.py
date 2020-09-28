from leccion1.modelo.modelos import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists

Session = sessionmaker(bind=engine)
session = Session()

print(10*"#","Leccion3",10*"#")

print(10*"#","Query #1")
for an_author, a_book in session.query(Author,Book).\
filter(Author.id==Book.author_id).\
filter(Book.isbn=="98496465").\
all():
  print(an_author)
  print(a_book)


print(10*"#","Query #2")
print(session.query(Author).join(Book).\
filter(Book.isbn == "98496465").all())


print(10*"#","Query  #3")
print(session.query(Author).join(Book, Author.id==Book.author_id).all())

print(10*"#","Query  #4")
print(session.query(Author).join(Author.books).all())

print(10*"#","Query  #5")
print(session.query(Author).join(Book, Author.books).all())

print(10*"#","Query  #6")
print(session.query(Author).join("books").all())

print(10*"#","Query  #7")
stmt = exists().where(Book.author_id==Author.id)
for name, in session.query(Author.firstname).filter(stmt):
  print(name)

print(10*"#","Query  #8")
for name, in session.query(Author.firstname).filter(Author.books.any()):
  print(name)

print(10*"#","Query  #9")
for name, in session.query(Author.firstname).filter(Author.books.any(Author.lastname.like("%Row%"))):
  print(name)

print(10*"#","Query  #10")
print(session.query(Book).filter(~Book.author.has(Author.firstname=="Joanne")).all())

print(10*"#","Query  #11")
print(session.query(Author).join(Book).filter(Book.isbn=="98496465"))

print(10*"#","Query  #12")
print(session.query(Author).join(Book).filter(Author.books.any()).all())

print(10*"#","Query  #13")
print(session.query(Author.firstname,Author.lastname).count())


print(30*"#")