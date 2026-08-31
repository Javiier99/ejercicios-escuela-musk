
from flask import Flask, jsonify, request

app = Flask(__name__)



employees = [
    {'id': 1, 'name': 'Jorge'},
    {'id': 2, 'name': 'Javier'},
    {'id': 3, 'name': 'Juan'}
]

def find_employee_by_id(employee_id):
    return next((e for e  in employees if e['id'] == employee_id), None)


def  employee_is_valid(employee):
    if not isinstance(employee, dict) or 'name' not in employee:
        return False

    for key in employee.keys():
        if key != 'name':
            return False

    return True


@app.route('/employees/<int:id>', methods=['DELETE'])
def eliminar_empleado(id):
    employee = find_employee_by_id(id)
    if employee is None:
        return jsonify({'Error' : "No tenemos ningún empleado con ese ID"}), 404
    employees.remove(employee)
    return jsonify("Empleado eliminado: ", employee ,"Empleados actuales: ", employees), 200



if __name__ == '__main__':
    app.run(debug=True)





