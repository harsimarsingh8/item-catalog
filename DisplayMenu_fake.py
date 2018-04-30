#! /usr/bin/env python2

# SQLAlchemy uses to communicate with various types of DBAPIs and databases.

import os
import sys


from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker, relationship

from database_setup import Base, Restaurant, MenuItem, User

engine=create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
ession = DBSession()


# Added fake database in menu items for our website before login.


item1 = MenuItem(name='Quesadillas', description='yummy', price='270', image='https://budaorsinaplo.hu/wp-content/uploads/2017/09/kaja.jpg',
         categories='tortillas')
session.add(item1)
session.commit()

item2 = MenuItem(name='Ice-Cream Shakes', description='yummy', price='150', image='http://universal.wdwinfo.com/wp-content/uploads/2016/10/IMG_2451-1.jpg',
           categories='Drinks')
session.add(item2)
session.commit()

item3 = MenuItem(name='Burger', description='yummy', price='150', image='https://cdn.vox-cdn.com/uploads/chorus_image/image/57762101/clarks_burger_yelp.0.0.jpg',
           categories='burger')
session.add(item3)
session.commit()

item4 = MenuItem(name='chicken wraps', description='yummy', price='150', image='https://www.quornfoodservice.co.uk/wp-content/uploads/2010/03/quorn_coronation_wraps.jpg',
        categories='Drinks')
session.add(item4)
session.commit()

print ("items added successfully!")


restaurant1 = Restaurant(name='Uncle jacks', image='https://pbs.twimg.com/media/Cu7Z4toUIAAx5bI.jpg', description='Awesome place')
session.add(restaurant1)
session.commit()


restaurant2 = Restaurant(name='keventers', image='https://content4.jdmagicbox.com/comp/bangalore/k7/080pxx80.xx80.170407082326.i1k7/catalogue/keventers-new-bel-road-bangalore-milk-shake-retailers-1wjnylj.jpg', description='Awesome place')
session.add(restaurant2)
session.commit()


restaurant3 = Restaurant(name='Beer cafe', image='https://content1.jdmagicbox.com/comp/delhi/n2/011pxx11.xx11.140529115354.n3n2/catalogue/the-beer-cafe-nehru-place-delhi-fine-dining-restaurants-rs-1000-to-rs-2000-2l9mtno.jpg'
                       , description='Awesome place')
session.add(restaurant3)
session.commit()


restaurant4 = Restaurant(name='Starbucks', image='https://cdn.pixabay.com/photo/2016/02/20/05/10/starbucks-1211620_960_720.jpg', description='Awesome place')
session.add(restaurant4)
session.commit()


print ("Restaurants added successfully!")