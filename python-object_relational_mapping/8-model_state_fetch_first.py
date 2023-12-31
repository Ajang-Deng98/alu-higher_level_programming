#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa
"""
<<<<<<< HEAD
<<<<<<< HEAD
Prints the first State object from the database hbtn_0e_6_usa
"""
=======
Writes out the first State object from the database hbtn_0e_6_usa
"""


>>>>>>> origin/main
=======
>>>>>>> 0c882bccf4493cdcf1f1e90e79e19d16f0ad32fa
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).first()
    if instance is None:
        print("Nothing")
    else:
        print(instance.id, instance.name, sep=": ")
