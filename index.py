import datetime

def calculate_year(name, age):
    current_year = datetime.datetime.now().year
    if age <= 0:
        raise ValueError("ასაკი არ შეიძლება იყოს  ნეგატიური რიცხვი ან  0.")
    elif not isinstance(age, int):
        raise TypeError("ასაკი  უნდა იყოს მთელი რიცხვი.")
    else:
        years_to_100 = 100 - age
        year_of_100 = current_year + years_to_100
        message = f"გამარჯობა {name}! შენ გახდები 100 წლის ამ {year_of_100}."
        return message

try:
    name = input("შეიყანეთ თქვენი სახელი: ")
    age = int(input("შეიყვანეთ თქვენი ასაკი: "))
    print(calculate_year(name, age))
except ValueError as ve:
    print("შეცდომა: " + str(ve))
except TypeError as te:
    print("შეცდომა: " + str(te))
except Exception as e:
    print("შეცდომა: " + str(e))
