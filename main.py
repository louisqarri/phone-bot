import json
from chat_brain import ChatBrain
brain = ChatBrain()

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
        response = brain.compare_phones(model_one, model_two)
        if response:
            print(response)
            chat_is_on = False
        else:
            print("Model not found!")        

    elif user_answer == "phone":
        model_user = input("Write the model name. Ex. iPhone 17 Pro Max\n").lower()
        phone = brain.find_phone(model_user)        
        if phone:
            response = brain.show_phone_specs(model_user)
            print(response)
            chat_is_on = False
        else:
            print("Model not found. Try again!")
    else:
        print("Not sure I understand what you mean.")
