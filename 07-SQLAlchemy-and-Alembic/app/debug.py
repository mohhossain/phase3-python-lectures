# 3.✅ CRUD practice
# To run the file run `python3 console.py` in the app directory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Pet

if __name__ == "__main__":
    # 3.1 ✅ Uncomment bellow to create the engine
    engine = create_engine("sqlite:///pet_app.db")
    Base.metadata.create_all(engine)
    # 3.2 ✅ Uncomment bellow to create sessions and bind o the engine
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.delete(Pet)

    # 3.3 ✅  -- Creating records
    # Create a pet and save it to the data base with session.add and session.commit

    new_pet = Pet(
        id=1, name="Spot", species="Dog", breed="Beagle", temperamnet="Freindly", owner_id = 3
    )
    
    

    session.commit()
    # session.close()
    # Filter pet by temperament with session.query and filter

    # 3.5 ✅ Update
    # Update the pets name and print the updated pet info

    # Update all the pets temperament to 'cool' and print the pets

    # 3.6 ✅  Delete
    # Delete one item by querying the first pet, deleting it and committing it

    # delete all the pets with session.query and .delete

    # optional Break point for debugging and testing
    import ipdb

    ipdb.set_trace()
