from leccion1.modelo.modelos import *
from sqlalchemy.orm import sessionmaker

author=Author(firstname="Joanne", lastname="Rowling")
print(author.firstname)
print(author.lastname)
print(author.id)

Session=sessionmaker(bind=engine)
session=Session()

session.add(author)
print(session.dirty)
found=session.query(Author).filter_by(firstname="Joanee").first()
print(author is found)
print(author)
print(author is session)
session.commit()
found=session.query(Author).filter_by(firstname="Joanee").first()
print(author.id)
session.add(Author(firstname="gabril",lastname="garcia"))
session.add(Author(firstname="paulo",lastname="cohelo"))
print(session.dirty)
session.rollback()
founds=session.query(Author).filter(Author.firstname.in_(["Joanne","gabriel"])).all()
print(founds)