import random 

response = {
    "hello":["Hi there!","Hello!","Hey!😊"],
    "how are you":["I'm good, thanks!","Doing great, and you?","All good"],
    "bye":["Goodbye!","See you later!","Bye👋"],

    "default":["I'm not understanding what are you saying?🤔"]

}

def simple_chatbot(user_input):
    user_input = user_input.lower()

    for key in response:
        if key in user_input:
            return random.choice(response[key])
    return random.choice(response["default"])    
