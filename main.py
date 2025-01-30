import json

#Menu
def menu():
    while True:
        print("\nMenu:")
        print("1. Introducir presupuesto")
        print("2. Ver todos los gastos")
        print("3. Añadir un gasto")
        print("4. Actualizar un gasto")
        print("5. Eliminar un gasto")
        print("6. Resumen de gastos")
        print("7. Gastos por mes o año actual")
        print("8. Aviso de gastos superiores al presupuesto")
        print("9. Añadir una categoría de gasto")
        print("10. Filtrar gastos por categoría")
        print("11. Salir")
        
        choice = input("Elige una opción: ")
        
        if choice == '1':
            set_budget()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            add_expense()
        elif choice == '4':
            update_expense()
        elif choice == '5':
            delete_expense()
        elif choice == '6':
            summary_expenses()
        elif choice == '7':
            expenses_by_month_or_year()
        elif choice == '8':
            warning_expenses()
        elif choice == '9':
            add_category()
        elif choice == '10':
            filter_expenses_by_category()
        elif choice == '11':
            break
        else:
            print("Opción no válida, por favor elige de nuevo.")

menu()


#Fundciones

#Introducir presupuesto
def set_budget():
    budget = input('Introduce el presupuesto: ')
    with open('budget.json', 'w') as file:
        json.dump(budget, file)
    print('Presupuesto guardado correctamente')
    
#Leer todos los gastos
def view_expenses():
    with open('expenses.json', 'r') as file:
        expenses = json.load(file)
        for expense in expenses:
            print(expense)
            
#Añadir un gasto
def add_expense():
    with open('expenses.json', 'r') as file:
        expenses = json.load(file)
    with open('categories.json', 'r') as file:
        categories = json.load(file)
    expense = {
        'id': len(expenses) + 1,
        'name': input('Introduce el nombre del gasto: '),
        'description': input('Introduce la descripcion: '),
        'amount': input('Introduce la cantidad: '),
        'category': input(f'Introduce la categoría del gasto {categories}: ')
    }
    expenses.append(expense)
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file, indent=4)
    print('Gasto añadido correctamente')
    
#Actualizar un gasto
def update_expense():
    with open('categories.json', 'r') as file:
        categories = json.load(file)
    with open('expenses.json', 'r') as file:
        expenses = json.load(file)
        id_actual = int(input('Introduce el id del gasto a actualizar: '))
        for expense in expenses:
            if expense['id'] == id_actual:
                expense['name'] = input('Introduce el nombre del gasto: ')
                expense['description'] = input('Introduce la descripcion: ')
                expense['amount'] = input('Introduce la cantidad: ')
                expense['category'] = input(f'Introduce la categoría: {categories}')
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file, indent=4)
    print(f'Gasto con id {id_actual} actualizado correctamente') 
        
#Eliminar un gasto
def delete_expense():
    with open('expenses.json', 'r') as file:
        expenses = json.load(file)
        id_actual = int(input('Introduce el id del gasto a eliminar: '))
        expenses = [expense for expense in expenses if expense['id'] != id_actual]
    with open('expenses.json', 'w') as file:
        json.dump(expenses, file, indent=4)
    print(f'Gasto con id {id_actual} eliminado correctamente')
    
#Resumen de gastos
def summary_expenses():
    with open('expenses.json', 'r') as file:
        expenses = json.load(file)
        total = sum([float(expense['amount']) for expense in expenses])
        print(f'El total de gastos es: {total}')

#Gastos por mes o año actual
def expenses_by_month_or_year():
    with open('expenses.json', 'r') as file:
        expenses = json.load(file)
        month = input('Introduce el mes a buscar: ')
        year = input('Introduce el año a buscar: ')
        total = sum([float(expense['amount']) for expense in expenses if expense['date'].split('-')[1] == month and expense['date'].split('-')[0] == year])
        print(f'El total de gastos para el mes {month} del año {year} es: {total}')
        
#Aviso de gastos superiores al presupuesto
def warning_expenses():
    with open('budget.json', 'r') as file:
        budget = json.load(file)
    with open('expenses.json', 'r') as file:
        expenses = json.load(file)
        total = sum([float(expense['amount']) for expense in expenses])
        if total > float(budget):
            print('¡Cuidado! Has superado el presupuesto')
        else:
            print('¡Enhorabuena! Sigues dentro del presupuesto')

# Añadir una categoría de gasto
def add_category():
    with open('categories.json', 'r') as file:
        categories = json.load(file)
        category = input('Introduce el nombre de la nueva categoría: ')
        if category not in categories:
            categories.append(category)
    with open('categories.json', 'w') as file:
        json.dump(categories, file, indent=4)
    print(f'Categoría {category} añadida correctamente')

# Filtrar gastos por categoría
def filter_expenses_by_category():
    with open('expenses.json', 'r') as file:
        expenses = json.load(file)
    category = input('Introduce la categoría a filtrar: ')
    filtered_expenses = [expense for expense in expenses if expense['category'] == category]
    for expense in filtered_expenses:
        print(expense)
    total = sum([float(expense['amount']) for expense in filtered_expenses])
    print(f'El total de gastos para la categoría {category} es: {total}')
