from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
 
from models import *
 
engine = create_engine('sqlite:///discoveries.db')
Base.metadata.bind = engine
 
DBSession = sessionmaker(bind=engine)
session = DBSession()

newCategory = Categories(name = 'Classical Mechanics')
session.add(newCategory)
session.commit()

newCategory = Categories(name = 'Quantum Mechanics')
session.add(newCategory)
session.commit()

newCategory = Categories(name = 'Optics')
session.add(newCategory)
session.commit()

newCategory = Categories(name = 'Relativity')
session.add(newCategory)
session.commit()

newCategory = Categories(name = 'Electromagnetism')
session.add(newCategory)
session.commit()

newCategory = Categories(name = 'Nuclear Physics')
session.add(newCategory)
session.commit()

print "Added items!"