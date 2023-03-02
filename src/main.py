import lector
import Empleado

data2 = [
        ['John', '25', 'Male'],
        ['Mary', '28', 'Female'],
        ['Mike', '30', 'Male'],
    ]

def main():
    lector.write_to_csv('Empleados.csv', data2)

if __name__ == '__main__':
    main()