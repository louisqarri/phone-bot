import json
from sqlalchemy import create_engine, Integer, String, Float, Boolean, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

with open("data/smartphones.json") as smartphones:
    smartphones_data = json.load(smartphones)

class Base(DeclarativeBase):
    pass

class Phone(Base):
    __tablename__ = "phones"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    brand: Mapped[str] = mapped_column(String(250), nullable=False)
    model: Mapped[str] = mapped_column(String(250), nullable=False)
    release_year: Mapped[int] = mapped_column(Integer, nullable=False)
    display_type: Mapped[str] = mapped_column(String(250), nullable=False)
    battery_mah: Mapped[int] = mapped_column(Integer, nullable=False)
    main_camera_mp: Mapped[float] = mapped_column(Float, nullable=False)
    ultra_wide_camera_mp: Mapped[float | None] = mapped_column(Float, nullable=True)
    telephoto_camera_mp: Mapped[float | None] = mapped_column(Float, nullable=True)
    front_camera_mp: Mapped[float] = mapped_column(Float, nullable=False)
    storage_options_gb: Mapped[str] = mapped_column(String(250), nullable=False)
    chipset: Mapped[str] = mapped_column(String(250), nullable=False)
    notes: Mapped[str] = mapped_column(String(500), nullable=False)

engine = create_engine("sqlite:///smartphone-collection.db")
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
    