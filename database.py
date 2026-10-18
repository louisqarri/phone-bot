from sqlalchemy import create_engine, Integer, String, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

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
