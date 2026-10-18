import json
from sqlalchemy import select
from sqlalchemy.orm import Session
from database import Phone, engine, Base

with open("data/smartphones.json") as smartphones:
    smartphones_data = json.load(smartphones)

Base.metadata.create_all(engine)

with Session(engine) as session:
    for item in smartphones_data["smartphones"]:
        exists = session.execute(select(Phone).where(Phone.model == item["model"])).scalar()
        if exists:
            continue
        add_phone = Phone(
            brand=item["brand"],
            model=item["model"],
            release_year=item["release_year"],
            display_type=item["display_type"],
            battery_mah=item["battery_mah"],
            main_camera_mp=item["main_camera_mp"],
            ultra_wide_camera_mp=item["ultra_wide_camera_mp"],
            telephoto_camera_mp=item["telephoto_camera_mp"],
            front_camera_mp=item["front_camera_mp"],
            storage_options_gb=json.dumps(item["storage_options_gb"]),
            chipset=item["chipset"],
            notes=item["notes"],
        )
        session.add(add_phone)
    session.commit()
    