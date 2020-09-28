from leccion1.modelo.modelos import *
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()
print(10*"#","leccion 4",10*"#")
authores = session.query(Author).filter(Author.firstname.like("Joanne2")).one()
print(authores)
session.delete(authores)
print(session.query(Author).filter(Author.firstname.like("Joanne2")).count())

print(session.query(Book).all())
print(30*"#")
