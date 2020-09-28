from leccion1.modelo.modelos import *
from sqlalchemy.orm import sessionmaker

print(10*"#","Ejercicios leccion 2",10*"#")
Session = sessionmaker(bind=engine)
session = Session()

j_rowling = Author(firstname="Joanne2",lastname="Rowling")
print(j_rowling.books)

j_rowling.books = [
                  Book(isbn="98496465",
                  title="Harray poter y pira filosofal",
                  description="la vida de popoter"),
                  Book(isbn="4894654",
                  title="Harray poter ycamara secreta",
                  description="la vida de popoter voldemor")
                  ]
print(j_rowling.books[1])
print(j_rowling.books[1].title)

session.add(j_rowling)
session.commit()

j_rowling = session.query(Author).filter_by(firstname="Joanne2").one()
print(j_rowling.books)
print(30*"#")