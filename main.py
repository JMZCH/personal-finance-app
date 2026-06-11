import json
from storage import save_data
from storage import load_data
from utils import validate_amount

#Este es el archivo principal del sistema de finanzas
user_name = "Jose"
edad = 23
initial_balance = 688
active_app = True

app_name = "MisFinanzas"
version = 1
currency = "USD"

total_income = 0.0
total_loss = 0.0
balance = 0.0

def add_transaction_entry(amount, transaction_type, description, creation_date):
    is_valid = validate_amount(amount)
    if not is_valid:
        print("El monto no puede ser cero.")
        return
    if amount < 0:
        print("El monto debe ser mayor a cero.")
        return
    if transaction_type == "gasto":
        amount = -amount
    transaction = {
            "amount": amount, 
            "description": description, 
            "type": transaction_type,
            "date": creation_date
            }
    transactions.append(transaction)
    if transaction_type == "ingreso":
        print("Ingreso registrado:", transaction)
    if transaction_type == "gasto":
        print("Gasto registrado:", transaction)
    return transaction

def show_transactions():
    for transaction in transactions:
        print(transaction)


def calculate_balance():
    total = 0
    for transaction in transactions:
        total = total + transaction["amount"]
    return total

def get_transaction_from_user():
    while True:
        try:
            amount = float(input("Ingresa el monto: "))
            break
        except ValueError:
            print("Eso no es un numero valido.")
            continue
    while True:        
        transaction_type = input("Ingresa el tipo de transaccion(ingreso/gasto): ").lower()
        if transaction_type not in ["ingreso", "gasto"]:
            print("Debe ser Ingreso o Gasto.")
            continue

        description = str(input("Ingrese una descripcion: "))
        creation_date = str(input("Ingrese la fecha: "))
        add_transaction_entry(amount, transaction_type, description, creation_date)
        break

def show_menu():
        while(True):
            print("1. Agregar transaccion")
            print("2. Ver transacciones")
            print("3. Ver Balance")
            print("4. Salir")
            try:
                selected_option = int(input("Ingrese la opcion: "))
            except ValueError:
                print("No es un caracter valido.")
                continue       
            if selected_option == 1:
                get_transaction_from_user()
            elif selected_option == 2:
                show_transactions()
            elif selected_option == 3:
                balance = calculate_balance()
                print("Balance actual:", balance, currency)
            elif selected_option == 4:
                save_data(transactions)
                break
            else:
                print("No es una opcion.")
                continue

#Inicio del programa
transactions = load_data()

print(f"Bienvenido a {app_name}, {user_name}")
print(f"Tu saldo inicial es: {initial_balance} {currency}")

print("Total de registros:", len(transactions))

show_menu()