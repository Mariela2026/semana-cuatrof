Sistema Básico de Gestión de Restaurante (POO en Python)

## Datos del Estudiante
* **Nombre Completo:** Mariela García
* **Institución:** Universidad Estatal Amazónica (UEA)
* **Carrera:** Tecnologías de la Información
* **Asignatura:** Programación Orientada a Objetos (Semana 4)

## Descripción del Sistema
Este proyecto consiste en una aplicación de consola desarrollada en Python que simula la administración operativa de un restaurante de forma simplificada. El diseño del software está fundamentado bajo el paradigma de la Programación Orientada a Objetos (POO) y emplea una arquitectura modular completa. El sistema permite modelar los productos del menú (platos y bebidas), gestionar los perfiles de los clientes, y centralizar el control mediante un servicio lógico que procesa la persistencia en memoria y la visualización organizada de la información registrada.

## Estructura del Proyecto
El diseño del software se segmentó de manera estricta siguiendo las directrices planteadas por el docente para garantizar un desacoplamiento óptimo:

```text
restaurante_app/
├── modelos/
│   ├── producto.py       # Define la entidad Producto con sus atributos (ID, denominación, precio, tipo).
│   └── cliente.py        # Define la entidad Cliente con credenciales (cédula, nombre, email).
├── servicios/
│   └── restaurante.py    # Servicio centralizador que encapsula los métodos y colecciones del negocio.
└── main.py               # Punto de entrada primario encargado del arranque y flujos del sistema.

Reflexión: Importancia de la Modularización y Separación de Responsabilidades
La modularización de software y el principio de separación de responsabilidades (SoC) constituyen pilares esenciales en la ingeniería de software moderna. Dividir un sistema complejo en componentes o módulos aislados e independientes aporta las siguientes ventajas clave:

Mantenibilidad y Escalabilidad: Al asignar una única responsabilidad a cada archivo (por ejemplo, delegar la estructura de datos a modelos/ y el comportamiento operativo a servicios/), cualquier modificación futura o corrección de fallas se realiza de forma quirúrgica sin alterar de forma colateral el resto de componentes del código fuente.

Reutilización de Código: Las clases declaradas en submódulos específicos pueden ser requeridas por múltiples procesos de forma limpia a través de directivas de importación (from ... import ...), reduciendo significativamente la redundancia lógica.

Trabajo Colaborativo: Facilita que múltiples desarrolladores trabajen de manera simultánea sobre distintas secciones del proyecto sin generar conflictos de código significativos en los sistemas de control de versiones como GitHub.