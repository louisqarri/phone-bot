from database import Phone, engine
from sqlalchemy import select
from sqlalchemy.orm import Session

class Brain():
    def __init__(self):
        with Session(engine) as session:
            self.all_phones = session.execute(select(Phone)).scalars().all()

    def find_phone(self, name):
        for phone in self.all_phones:
            if phone.model.lower() == name:                
                return phone
        return False

    def compare_phones(self, model_one, model_two):
        phone_one = self.find_phone(model_one)
        phone_two = self.find_phone(model_two)
        if phone_one and phone_two:
            return f"""
{phone_one.brand} {phone_one.model}  vs  {phone_two.brand} {phone_two.model}

Release year
{phone_one.release_year}  |  {phone_two.release_year}

Display
{phone_one.display_type}  |  {phone_two.display_type}

Battery
{phone_one.battery_mah} mAh  |  {phone_two.battery_mah} mAh

Main camera
{phone_one.main_camera_mp} MP  |  {phone_two.main_camera_mp} MP

Ultra wide camera
{phone_one.ultra_wide_camera_mp} MP  |  {phone_two.ultra_wide_camera_mp} MP

Telephoto camera
{phone_one.telephoto_camera_mp} MP  |  {phone_two.telephoto_camera_mp} MP

Front camera
{phone_one.front_camera_mp} MP  |  {phone_two.front_camera_mp} MP

Storage options
{phone_one.storage_options_gb} GB  |  {phone_two.storage_options_gb} GB

Chipset
{phone_one.chipset}  |  {phone_two.chipset}

Notes
{phone_one.model}: {phone_one.notes}
{phone_two.model}: {phone_two.notes}
"""
        else:
            return "Model not found!"

    def show_phone_specs(self, name):
        phone = self.find_phone(name)
        return f"""
{phone.brand} {phone.model}

Release year
{phone.release_year}

Display
{phone.display_type}

Battery
{phone.battery_mah} mAh

Main camera
{phone.main_camera_mp} MP

Ultra wide camera
{phone.ultra_wide_camera_mp} MP

Telephoto camera
{phone.telephoto_camera_mp} MP

Front camera
{phone.front_camera_mp} MP

Storage options
{phone.storage_options_gb} GB

Chipset
{phone.chipset}

Notes
{phone.notes}
"""
