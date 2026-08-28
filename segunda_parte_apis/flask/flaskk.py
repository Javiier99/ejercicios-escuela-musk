import json
from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de empleados inicial
employees = [
    {'id': 1, 'name': 'Jorge'},
    {'id': 2, 'name': 'Javier'},
    {'id': 3, 'name': 'Juan'}
]
next_employee_id = 4


# --- Funciones Auxiliares ---

def find_employee_by_id(employee_id):
    """Busca un empleado por su ID."""
    return next((e for e in employees if e['id'] == employee_id), None)

def employee_is_valid(employee):
    """Valida que el diccionario tenga únicamente la clave 'name'."""
    if not isinstance(employee, dict) or 'name' not in employee:
        return False
    
    for key in employee.keys():
        if key != 'name':
            return False
            
    return True


# --- Rutas de la API ---

@app.route('/employees', methods=['GET'])
def get_all_employees():
    return jsonify(employees), 200

@app.route('/employees/<int:id>', methods=['GET'])
def get_employee_by_id(id):
    employee = find_employee_by_id(id)
    if employee is None:
        return jsonify({'error': 'Employee not found'}), 404
    return jsonify(employee), 200

@app.route('/employees', methods=['POST'])
def create_employee():
    global next_employee_id
    data = request.get_json()

    if not data or not employee_is_valid(data):
        return jsonify({'error': 'Invalid Employee'}), 400

    new_employee = {
        'id': next_employee_id,
        'name': data['name']
    }
    
    employees.append(new_employee)
    next_employee_id += 1
    
    return jsonify(new_employee), 201

@app.route('/employees/<int:id>', methods=['PUT'])
def update_employee(id):
    employee = find_employee_by_id(id)
    if employee is None:
        return jsonify({'error': 'Employee does not exist'}), 404

    data = request.get_json()
    if not data or not employee_is_valid(data):
        return jsonify({'error': 'Employee invalid'}), 400

    employee.update(data)
    return jsonify(employee), 200


if __name__ == '__main__':
    app.run(debug=True)