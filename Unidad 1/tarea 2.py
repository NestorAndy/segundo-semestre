from abc import ABC, abstractmethod

# Abstracción
class Empleado(ABC):
    def __init__(self, nombre, id_empleado):
        self._nombre = nombre
        self._id_empleado = id_empleado

    @abstractmethod
    def calcularSalario(self):
        pass

    @abstractmethod
    def mostrarInfo(self):
        pass

# Herencia y Encapsulación
class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, id_empleado, salario_mensual):
        super().__init__(nombre, id_empleado)
        self.__salario_mensual = salario_mensual

    def calcularSalario(self):
        return self.__salario_mensual

    def mostrarInfo(self):
        print(f"Empleado Tiempo Completo: {self._nombre}, ID: {self._id_empleado}, Salario Mensual: ${self.__salario_mensual:.2f}")

class EmpleadoMedioTiempo(Empleado):
    def __init__(self, nombre, id_empleado, salario_por_hora, horas_trabajadas):
        super().__init__(nombre, id_empleado)
        self.__salario_por_hora = salario_por_hora
        self.__horas_trabajadas = horas_trabajadas

    def calcularSalario(self):
        return self.__salario_por_hora * self.__horas_trabajadas

    def mostrarInfo(self):
        print(f"Empleado Medio Tiempo: {self._nombre}, ID: {self._id_empleado}, Salario por Hora: ${self.__salario_por_hora:.2f}, Horas Trabajadas: {self.__horas_trabajadas}")

# Polimorfismo
def mostrarEmpleadosYCalcularSalarios(empleados):
    for empleado in empleados:
        empleado.mostrarInfo()
        salario = empleado.calcularSalario()
        print(f"Salario Calculado: ${salario:.2f}")

# Uso
empleado1 = EmpleadoTiempoCompleto("Juan Pérez", 1, 3000)
empleado2 = EmpleadoMedioTiempo("Ana Gómez", 2, 20, 80)

empleados = [empleado1, empleado2]

mostrarEmpleadosYCalcularSalarios(empleados)
