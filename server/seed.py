#!/usr/bin/env python3

from app import app
from models import db, Plant

with app.app_context():

    Plant.query.delete()

    aloe = Plant(
        id=1,
        name="Aloe",
        image="./images/aloe.jpg",
        price=11.50,
    )

    zz_plant = Plant(
        id=2,
        name="ZZ Plant",
        image="./images/zz-plant.jpg",
        price=25.98,
    )

    orchid = Plant(
        id=3,
        name="Orchid",
        image="https://cdn.shopify.com/s/files/1/0507/3754/5401/files/P2162_LOL_preset_ftd-mx-hero-sv-new.jpg?v=1689848923&width=768",
        price=39.99,
    )

    db.session.add_all([aloe, zz_plant, orchid])
    db.session.commit()
