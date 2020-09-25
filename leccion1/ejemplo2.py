from leccion1.modelo.modelos import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import aliased

Session=sessionmaker(bind=engine)
session=Session()
print(30*"#")
session.add_all([Author(firstname="Gabril",lastname="Garcia")
,Author(firstname="Paulo",lastname="Cohelo")
,Author(firstname="John",lastname="Tolkie")])

session.commit()

print(5*"#","Query #1")
for instance in session.query(Author).order_by(Author.id):
  print(instance.firstname,instance.lastname)

print(5*"#","Query #2")
for firstname, lastname in session.query(Author.firstname,Author.lastname):
  print(firstname,lastname)

print(5*"#","Query #3")
for row in session.query(Author,Author.firstname).all():
  print(row.firstname)

print(5*"#","Query #4")
for row in session.query(Author.firstname.label("firstname_label")).all():
  print(row.firstname_label)

print(5*"#","Query #5")
author_alias = aliased(Author,name="author_alias")

for row in session.query(author_alias, author_alias.firstname).all():
  print(row.author_alias)

print(5*"#","Query #6")
for an_author in session.query(Author).order_by(Author.id)[1:3]:
  print(an_author)

print(5*"#","Query #7")
name, = session.query(Author).filter_by(firstname="Joanne")
print(name)

print(5*"#","Query #8")
name, = session.query(Author).filter(Author.lastname=="Rowling")
print(name)

print(5*"#","Query #9")
for an_author in session.query(Author).\
filter(Author.firstname=="Joanne").\
filter(Author.lastname=="Rowling"):
  print(an_author)

print(5*"#","Query #10")
print(session.query(Author).filter(Author.firstname=='Joanne').count())
