from sql_alchemy import session,engine,base
from inventory import Inventory,History

base.metadata.create_all(engine)
Session = session

def get_inventory():
    inventory_items = Session.query(Inventory).all()
    return inventory_items

def add_inventory_aggregation(make,model,year,color):
    new_inv = Inventory(make,model,year,True,color)
    new_inv.history = [
        History(history_type='new car'),
        History(history_type='new car')
    ]
    Session.add(new_inv)
    Session.commit()

def add_inventory(make,model,year,color):
    new_inv = Inventory(make,model,year,True,color)
    Session.add(new_inv)
    Session.commit()

def rent_inventory(inventory_id):
    inv_item = Session.query(Inventory).filter_by(id=inventory_id).first()
    inv_item.avaible = False
    Session.commit()

def return_inventory(inventory_id):
    inv_item = Session.query(Inventory).filter_by(id=inventory_id).first()
    inv_item.avaible = True
    Session.commit()

add_inventory('a','as',201,'aww')
