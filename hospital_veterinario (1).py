# Importamos las librerias Abstractas

from abc import ABC, abstractmethod

"""----------------CLASE ABSTRACTA-----------"""

class Persona(ABC):
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento
    
    @abstractmethod
    def mostrar_rol(self):
        pass

"""---------------- HERENCIA -----------"""

class Cliente(Persona):
    def __init__(self, nombre, documento, telefono):
        super().__init__(nombre, documento)
        self.telefono = telefono
        self.mascota = []

    def mostrar_rol(self, rol):
        return f"El rol de este usuario es: {rol}"
    
    def agregar_mascota(self, mascota):
        self.mascota.append(mascota)
    
    def mostrar_mascotas(self):
        for mascota in self.mascota :
            return mascota

class Recepcionista(Persona):
    def __init__(self, nombre, documento):
        super().__init__(nombre, documento)
        self.cliente = []
        self.rol="Recepcionista"

    def mostrar_rol(self):
        return f"El rol de este usuario es: {self.rol}"
    
    def agregar_cliente(self, cliente):
        self.cliente.append(cliente)

class Veterinario(Persona):
    def __init__(self, nombre, documento, especialidad):
        super().__init__(nombre, documento)
        self.especialidad = especialidad
        self.rol="Veterinario"
    def mostrar_rol(self):
        return f"El rol de este usuario es: {self.rol}"
    
    def atender_mascota(self, mascota):
        return f"El veterinario {self.nombre} está atendiendo a la mascota {mascota}"
    
class Mascota:
    def __init__(self, nombre, especie, edad, peso):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.peso = peso

    def mostrar_info(self):
        return f"La mascota se llama: {self.nombre}\n especie: {self.especie}  \nedad de {self.edad} años \n peso de {self.peso} kg."
    
class Consulta:
    def __init__(self, mascota, veterinario, motivo, diagnostico):
        self.mascota = mascota
        self.veterinario = veterinario
        self.motivo = motivo
        self.diagnostico = diagnostico
        self.tratamientos = []

    def crear_tratamiento(self, tratamiento):
        self.tratamientos.append(tratamiento)

    def mostrar_resumen(self):
        info_tratamientos = ""
        for tratamiento in self.tratamientos:
            info_tratamientos += (
                f"Nombre: {tratamiento.nombre}, "
                f"Costo: {tratamiento.costo}, "
                f"Duracion: {tratamiento.duracion_dias} dias\n"
            )

        return (
            f"Mascota: {self.mascota.nombre}\n"
            f"Veterinario: {self.veterinario.nombre}\n"
            f"Especialidad: {self.veterinario.especialidad}\n"
            f"Motivo: {self.motivo}\n"
            f"Diagnostico: {self.diagnostico}\n"
            f"Tratamientos: \n{info_tratamientos}"
        )

    def calcular_costo_consulta(self):
        costo_base = 30000
        total_tratamientos = 0
               
        for tratamiento in self.tratamientos:
            total_tratamientos += tratamiento.costo
        
        return costo_base + total_tratamientos

class Tratamiento:
    def __init__(self, nombre, costo, duracion_dias):
        self.nombre = nombre
        self.costo = costo
        self.duracion_dias = duracion_dias

    def mostrar_tratamiento(self):
        return (
            f"Tratamiento: {self.nombre}\n"
            f"Costo: {self.costo}\n"
            f"Duracion: {self.duracion_dias} dias"
        )
    
class Hospitalizacion:
    def __init__(self, mascota, veterinario, dias, motivo):
        self.mascota = mascota
        self.veterinario = veterinario
        self.dias = dias
        self.motivo = motivo
        self.tratamientos = []
        self.costo_dia = 50000
        self.pagada = False

    def agregar_tratamiento(self, tratamiento):
        self.tratamientos.append(tratamiento)

    def mostrar_resumen(self):
        info_tratamientos = ""
        for tratamiento in self.tratamientos:
            info_tratamientos += (
                f"Nombre: {tratamiento.nombre}, "
                f"Costo: {tratamiento.costo}, "
                f"Duración: {tratamiento.duracion_dias} días\n"
            )

        return (
            f"--- HOSPITALIZACIÓN ---\n"
            f"Mascota: {self.mascota.nombre}\n"
            f"Especie: {self.mascota.especie}\n"
            f"Veterinario responsable: {self.veterinario.nombre}\n"
            f"Especialidad: {self.veterinario.especialidad}\n"
            f"Motivo: {self.motivo}\n"
            f"Días de hospitalización: {self.dias}\n"
            f"Tratamientos:\n{info_tratamientos}"
        )

    def calcular_costo_hospitalizacion(self):
        total_tratamientos = 0
        for tratamiento in self.tratamientos:
            total_tratamientos += tratamiento.costo

        return (self.dias * self.costo_dia) + total_tratamientos

    def pagar_hospitalizacion(self, metodo_pago):
        total = self.calcular_costo_hospitalizacion()
        self.pagada = True
        return metodo_pago.procesar_pago(total)


"""---------------- CLASES FINANCIERAS  -----------"""

class MetodoPago(ABC):
    def __init__(self, monto):
        self.monto = monto

    @abstractmethod
    def procesar_pago(self, monto):
        pass

class PagoEfectivo(MetodoPago):
    def procesar_pago(self, monto):
        return f"Pago en efectivo procesado por {monto}."
    
class PagoTarjeta(MetodoPago):
    def procesar_pago(self, monto):
        return f"Pago con tarjeta procesado por {monto}."

class PagoTransferencia(MetodoPago):
    def procesar_pago(self, monto):
        return f"Pago con transferencia procesado por {monto}."
    
class Factura:
    def __init__(self, consulta):
        self.consulta = consulta
        self.subtotal = consulta.calcular_costo_consulta()
        self.impuesto = self.subtotal * 0.19
        self.total = self.subtotal + self.impuesto 

    
    def calcular_total(self):
        return f"El total de su Factura es de: ${self.total}"
    
    def pagar(self, metodo_pago):
        return metodo_pago.procesar_pago(self.total)

print("\n================ CONSULTA ================\n")
# Crear cliente
cliente1 = Cliente("Ana", "12345", "3001234567")

# Crear mascota
mascota1 = Mascota("Firulais", "Perro", 5, 12)
mascota2 = Mascota("Michi", "Gato", 1, 6)

# Asociar mascota al cliente
cliente1.agregar_mascota(mascota1)
cliente1.agregar_mascota(mascota2)

# Crear veterinario
veterinario1 = Veterinario("Carlos", "98765", "Medicina general")

# Crear consulta
consulta1 = Consulta(mascota1, veterinario1, "Fiebre", "Infeccion estomacal")

# Crear tratamientos
tratamiento1 = Tratamiento("Antibiotico", 20000, 5)
tratamiento2 = Tratamiento("Suero", 15000, 2)

# Agregar tratamientos a la consulta
consulta1.crear_tratamiento(tratamiento1)
consulta1.crear_tratamiento(tratamiento2)

# Mostrar resumen de la consulta
print(consulta1.mostrar_resumen())

# Crear factura
factura1 = Factura(consulta1)

# Mostrar total
print(factura1.calcular_total())

# Crear metodo de pago
pago1 = PagoEfectivo(factura1.total)

# Procesar pago
print(factura1.pagar(pago1))

print("\n================ HOSPITALIZACION ================\n")

# Crear hospitalizacion
hospitalizacion1 = Hospitalizacion(
    mascota2,
    veterinario1,
    3,
    "Observacion por infeccion y deshidratacion"
)

# Crear nuevos tratamientos para hospitalizacion
tratamiento3 = Tratamiento("Medicamento intravenoso", 25000, 3)
tratamiento4 = Tratamiento("Monitoreo constante", 10000, 3)

# Agregar tratamientos a la hospitalizacion
hospitalizacion1.agregar_tratamiento(tratamiento1)
hospitalizacion1.agregar_tratamiento(tratamiento3)
hospitalizacion1.agregar_tratamiento(tratamiento4)

# Mostrar resumen de la hospitalizacion
print(hospitalizacion1.mostrar_resumen())

# Mostrar costo total de la hospitalizacion
total_hospitalizacion = hospitalizacion1.calcular_costo_hospitalizacion()
print(f"Costo total de hospitalizacion: ${total_hospitalizacion}")

# Crear metodo de pago para la hospitalizacion
pago2 = PagoTarjeta(total_hospitalizacion)

# Procesar pago de la hospitalizacion
print(hospitalizacion1.pagar_hospitalizacion(pago2))