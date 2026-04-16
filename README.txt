Introducción
El presente diagrama de clases UML representa el diseño estructural de un sistema de gestión para una clínica veterinaria. Su propósito es modelar las entidades principales que intervienen en el funcionamiento del sistema, así como las relaciones existentes entre ellas. Entre los elementos representados se encuentran las personas que interactúan con la clínica, las mascotas, las consultas médicas, los tratamientos, la facturación y los métodos de pago.
Este modelo aplica conceptos fundamentales de la programación orientada a objetos, tales como la herencia, la abstracción, la asociación, la agregación, la composición y el polimorfismo. Gracias a ello, el sistema logra una estructura organizada, reutilizable y fácil de mantener.

Descripción de las clases
1. Clase Persona
La clase Persona es una clase abstracta, lo que significa que no puede ser instanciada directamente, sino que sirve como base para otras clases más específicas. Esta clase agrupa los atributos y comportamientos comunes de las personas que participan en el sistema.
Atributos:
•	nombre
•	documento
Método:
•	mostrar_rol()
A partir de esta clase se derivan las clases Cliente, Recepcionista y Veterinario.

2. Clase Cliente
La clase Cliente representa a la persona propietaria de una o varias mascotas registradas en la clínica.
Atributos:
•	telefono
•	mascotas[]
Métodos:
•	mostrar_rol()
•	agregar_mascota()
•	mostrar_mascota()
Esta clase hereda de Persona, por lo que comparte sus atributos generales, pero añade características propias relacionadas con la gestión de mascotas.



3. Clase Recepcionista
La clase Recepcionista representa al personal encargado de realizar procesos administrativos, principalmente el registro de clientes.
Métodos:
•	mostrar_rol()
•	registrar_cliente()
También hereda de Persona, compartiendo así los atributos generales de identificación.

4. Clase Veterinario
La clase Veterinario representa al profesional responsable de atender médicamente a las mascotas.
Atributo:
•	especialidad
Métodos:
•	mostrar_rol()
•	atender_mascota()
Esta clase hereda de Persona y amplía su funcionalidad con información y acciones propias del área clínica.
5. Clase Mascota
La clase Mascota representa al animal que recibe atención veterinaria dentro del sistema.
Atributos:
•	nombre
•	especie
•	edad
•	peso

Método:
•	mostrar_info()
Cada mascota está asociada a un cliente y puede participar en una o varias consultas.

6. Clase Consulta
La clase Consulta es una de las más importantes del sistema, ya que permite registrar la atención médica brindada a una mascota.
Atributos:
•	mascota
•	veterinario
•	motivo
•	diagnostico
•	tratamientos[]
Métodos:
•	crear_tratamiento()
•	mostrar_resumen()
•	calcular_costo_consulta()
Esta clase vincula directamente a la mascota con el veterinario, y además permite incluir uno o varios tratamientos derivados del diagnóstico realizado.
7. Clase Tratamiento
La clase Tratamiento representa el procedimiento o cuidado indicado durante una consulta veterinaria.
Atributos:
•	nombre
•	costo
•	duración_días

Método:
•	mostrar_tratamiento()
Cada tratamiento forma parte de una consulta específica.

8. Clase Hospitalización
La clase hospitalización es importante, ya que permite ingresar el registro de la mascota y los días hospitalizados.
Atributos:
•	mascota
•	veterinario
•	días
•	motivo
•	costo_días 
•	tratamientos[]
Métodos:
•	agregar_tratamiento()
•	mostrar_resumen()
•	calcular_costo_hospitalizacion()
•	pagar_hospitalizacion()

Esta clase se vincula directamente con factura, y además permite incluir uno o varios tratamientos derivados del diagnóstico realizado (composición).

9. Clase Factura
La clase Factura representa el documento generado para cobrar los servicios prestados en una consulta.

Atributos:
•	consulta
•	subtotal
•	impuesto
•	total
Métodos:
•	calcular_total()
•	pagar(MetodoPago)
La factura se genera a partir de una consulta y/o una hospitalización, además permite calcular el valor final a pagar, además de registrar el método de pago utilizado.

10. Clase MetodoPago
La clase MetodoPago es una clase abstracta que define el comportamiento general de cualquier forma de pago implementada en el sistema.
Método:
•	procesar_pago(monto)
De esta clase derivan los distintos tipos de pago disponibles.

11. Clase PagoEfectivo
Representa el pago realizado en efectivo.
Método:
•	procesar_pago(monto)
Hereda de MetodoPago.

12. Clase PagoTarjeta
Representa el pago realizado mediante tarjeta.

Método:
•	procesar_pago(monto)
Hereda de MetodoPago.

13. Clase PagoTransferencia
Representa el pago efectuado por transferencia bancaria.
Método:
•	procesar_pago(monto)
Hereda de MetodoPago.

Explicación de las relaciones del diagrama
Herencia
La herencia permite que una clase adquiera atributos y métodos de otra clase más general.
En el diagrama se presentan dos jerarquías de herencia:
1.	Herencia desde Persona:
•	Cliente
•	Recepcionista
•	Veterinario
2.	Herencia desde MetodoPago:
•	PagoEfectivo
•	PagoTarjeta
•	PagoTransferencia
Esto permite reutilizar código y definir comportamientos comunes en las clases abstractas, mientras que las clases hijas incorporan sus propias particularidades.


Asociación
La asociación representa una relación estructural entre dos clases que interactúan entre sí.
En el diagrama se identifican las siguientes asociaciones:
•	Mascota se relaciona con Consulta, ya que una mascota puede asistir a consultas veterinarias.
•	Veterinario se relaciona con Consulta, pues es quien realiza la atención.
•	Consulta se relaciona con Factura, porque de una consulta se deriva una factura.
•	Mascota se relaciona con Hospitalización, ya que una mascota puede asistir a consultas veterinarias.
•	Veterinario se relaciona con Hospitalización, pues es quien realiza la atención.
•	Hospitalización se relaciona con Factura, porque de una hospitalización se deriva una factura.
Estas asociaciones permiten modelar la interacción entre entidades del sistema.

Agregación
La agregación expresa una relación de tipo “todo-parte” donde las partes pueden existir independientemente del todo.
En el diagrama:
•	Cliente tiene una relación de agregación con Mascota.
Esto significa que un cliente posee mascotas registradas, pero las mascotas pueden seguir existiendo como entidades del sistema, aunque cambie la relación con el cliente.

Composición
La composición es una relación más fuerte que la agregación, en la que la existencia de la parte depende del todo.

En el diagrama:
•	Consulta tiene una relación de composición con Tratamiento.
Esto indica que los tratamientos están completamente ligados a una consulta específica, y no tendrían sentido de manera aislada dentro del modelo.
•	Hospitalización tiene una relación de composición con Tratamiento.
Esto indica que los tratamientos están completamente ligados a una Hospitalización específica, y no tendrían sentido de manera aislada dentro del modelo.

Dependencia
La dependencia indica que una clase utiliza a otra de manera puntual para ejecutar cierta operación.
En el caso del diagrama:
•	Factura depende de MetodoPago a través del método pagar(MetodoPago).
Esta relación permite que la factura pueda procesar pagos de distintas formas sin depender de una implementación concreta, favoreciendo así la flexibilidad del sistema.

Funcionamiento general del sistema
De acuerdo con el modelo propuesto, el flujo general del sistema sería el siguiente:
1.	Un recepcionista registra a un cliente.
2.	El cliente registra una o varias mascotas.
3.	Una mascota es atendida por un veterinario mediante una consulta.
4.	Durante la consulta se registra el motivo, el diagnóstico y los tratamientos necesarios.
5.	Con base en la consulta se genera una factura.
6.	Durante la hospitalización se registra el motivo, días y los tratamientos necesarios.
7.	Sí hay hospitalización se genera una factura.
8.	La factura calcula subtotal, impuesto y total.
9.	Finalmente, el pago se realiza mediante alguno de los métodos disponibles: efectivo, tarjeta o transferencia.

Conclusión
El diagrama UML presentado refleja una estructura clara y coherente para un sistema de gestión veterinaria. La organización de sus clases y relaciones permite representar adecuadamente los procesos principales de atención, control de mascotas, consultas médicas, hospitalizaciones y facturación.
Además, el uso de clases abstractas, herencia y polimorfismo demuestra una correcta aplicación de los principios de la programación orientada a objetos, lo que contribuye a que el sistema sea escalable, modular y fácil de mantener. En conjunto, este modelo constituye una base sólida para el desarrollo e implementación de una solución informática orientada al entorno veterinario.

Enlace GitHub: https://github.com/Jhoansebs100/PythonDev.git

Integrantes: Jerson Arley Roman, Jhoan Sebastián Perea Montañez, Iván Eliecer Beltrán González y Mauricio Coneo Romero.

