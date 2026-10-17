import json
from chat_data import ChatData

with open("data/smartphones.json") as smartphones:
    smartphones_data = json.load(smartphones)

all_smartphone_object = []
for phone in smartphones_data["smartphones"]:
    phone_obj = ChatData(
        phone["brand"],
        phone["model"],
        phone["release_year"], phone["display_type"],
        phone["storage_options_gb"],
        phone["main_camera_mp"],
        phone["ultra_wide_camera_mp"],
        phone["telephoto_camera_mp"],
        phone["front_camera_mp"],
        phone["battery_mah"],
        phone["chipset"],
        phone["notes"]
        )
    all_smartphone_object.append(phone_obj)

user_answer = input("Hello. How can I help you today?\n").lower()

chat_is_on = True
while chat_is_on:
    user_answer = input("Type 'COMPARE' start comparing smartphone models or 'PHONE' to see smartphone specs\n").lower()
    if user_answer == "exit":
        print("Goodbye!")
        chat_is_on = False
    elif user_answer == "compare":
        model_one = input("Enter the first model to compare. Ex. Galaxy S26 Ultra\n").lower()
        model_two = input("Enter the second model to compare. Ex iPhone 17 Pro Max\n").lower()

        found_model_one = None
        found_model_two = None
        for phone in all_smartphone_object:
            if phone.model.lower() == model_one:
                found_model_one = phone
            if phone.model.lower() == model_two:
                found_model_two = phone
        if found_model_one and found_model_two:
            print(f"""
            --- COMPARISON ---
            {found_model_one.brand} {found_model_one.model} vs {found_model_two.brand} {found_model_two.model}
            Release Year:     {found_model_one.release_year} vs {found_model_two.release_year}
            Display:          {found_model_one.display_type} vs {found_model_two.display_type}
            Battery:          {found_model_one.battery_mah}mAh vs {found_model_two.battery_mah}mAh
            Main Camera:      {found_model_one.main_camera_mp}MP vs {found_model_two.main_camera_mp}MP
            Ultra Wide:       {found_model_one.ultra_wide_camera_mp}MP vs {found_model_two.ultra_wide_camera_mp}MP
            Telephoto:        {found_model_one.telephoto_camera_mp}MP vs {found_model_two.telephoto_camera_mp}MP
            Front Camera:     {found_model_one.front_camera_mp}MP vs {found_model_two.front_camera_mp}MP
            Storage Options:  {found_model_one.storage_options_gb}GB vs {found_model_two.storage_options_gb}GB
            Chipset:          {found_model_one.chipset} vs {found_model_two.chipset}
            Notes:            {found_model_one.notes}
            {found_model_two.notes}
""")
            chat_is_on = False
        else:
            print("Model not found!")

    elif user_answer == "phone":
        model_user = input("Write the model name. Ex. iPhone 17 Pro Max\n").lower()
        found_phone = None
        for phones in all_smartphone_object:
            if phones.model.lower() == model_user:
                found_phone = phones
                break

        if found_phone:
            print(f"""
            --- SPECS ---
            {found_phone.brand} {found_phone.model}
            Release Year:    {found_phone.release_year}
            Display:         {found_phone.display_type}
            Battery:         {found_phone.battery_mah}mAh
            Main Camera:     {found_phone.main_camera_mp}MP
            Ultra Wide:      {found_phone.ultra_wide_camera_mp}MP
            Telephoto:       {found_phone.telephoto_camera_mp}MP
            Front Camera:    {found_phone.front_camera_mp}MP
            Storage Options: {found_phone.storage_options_gb}GB
            Chipset:         {found_phone.chipset}
            Notes:           {found_phone.notes}
""")
            chat_is_on = False
        else:
            print("Model not found. Try again!")
    else:
        print("Not sure I understand what you mean.")
