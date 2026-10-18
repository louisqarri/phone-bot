from database import Phone, engine
from sqlalchemy import select
from sqlalchemy.orm import Session
import json

class ChatBrain():
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
            return (f"""
            --- COMPARISON ---
            {phone_one.brand} {phone_one.model} vs {phone_two.brand} {phone_two.model}
            Release Year:     {phone_one.release_year} vs {phone_two.release_year}
            Display:          {phone_one.display_type} vs {phone_two.display_type}
            Battery:          {phone_one.battery_mah}mAh vs {phone_two.battery_mah}mAh
            Main Camera:      {phone_one.main_camera_mp}MP vs {phone_two.main_camera_mp}MP
            Ultra Wide:       {phone_one.ultra_wide_camera_mp}MP vs {phone_two.ultra_wide_camera_mp}MP
            Telephoto:        {phone_one.telephoto_camera_mp}MP vs {phone_two.telephoto_camera_mp}MP
            Front Camera:     {phone_one.front_camera_mp}MP vs {phone_two.front_camera_mp}MP
            Storage Options:  {phone_one.storage_options_gb}GB vs {phone_two.storage_options_gb}GB
            Chipset:          {phone_one.chipset} vs {phone_two.chipset}
            Notes:            {phone_one.notes} vs {phone_two.notes}
""")
        else:
            return "Model not found!"

    def show_phone_specs(self, name):
        phone = self.find_phone(name)
        return f"""
        --- SPECS ---
        {phone.brand} {phone.model}
        Release Year:    {phone.release_year}
        Display:         {phone.display_type}
        Battery:         {phone.battery_mah}mAh
        Main Camera:     {phone.main_camera_mp}MP
        Ultra Wide:      {phone.ultra_wide_camera_mp}MP
        Telephoto:       {phone.telephoto_camera_mp}MP
        Front Camera:    {phone.front_camera_mp}MP
        Storage Options: {phone.storage_options_gb}GB
        Chipset:         {phone.chipset}
        Notes:           {phone.notes}
"""

    def get_user_reply(self, user_text):
        pass
        