#Modulo de almacenamietno de datos
import json

def save_data(transactions):
    with open("datos.json", "w") as file:
        json.dump(transactions, file)

def load_data():
    try:
        with open("datos.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    