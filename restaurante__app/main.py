# ==========================================================
# SCRIPT PRINCIPAL: Punto de Entrada al Sistema
# ----------------------------------------------------------
# Archivo ejecutable encargado de arrancar el programa.
# ==========================================================

# Importaciones explícitas desde los respectivos paquetes modulares
from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

def ejecutar_aplicacion():
    # 1. Instanciación del restaurante
    gestion_restaurante = Restaurante("Gourmet Tradicional")

    # 2. Carga de Productos de prueba
    plato_A = Producto("P001", "Ceviche de Camarón", 8.50, "Plato Fuerte")
    plato_B = Producto("P002", "Empanada de Viento", 1.50, "Entrada")
    plato_C = Producto("P003", "Chicha Morada (Jarra)", 3.50, "Bebida")

    # 3. Registro de Clientes de prueba
    usuario_A = Cliente("1755443322", "Mariela García", "mariela.garcia@mail.com")
    usuario_B = Cliente("0604433221", "Juan Carlos Andrade", "jcandrade@mail.com")

    # 4. Registrar los datos en el servicio central
    gestion_restaurante.incorporar_item_menu(plato_A)
    gestion_restaurante.incorporar_item_menu(plato_B)
    gestion_restaurante.incorporar_item_menu(plato_C)

    gestion_restaurante.enrolar_nuevo_cliente(usuario_A)
    gestion_restaurante.enrolar_nuevo_cliente(usuario_B)

    # 5. Salida en consola
    print("=====================================================================")
    print(f"       SISTEMA DE GESTIÓN GASTRONÓMICA: {gestion_restaurante.nombre_establecimiento.upper()}       ")
    print("=====================================================================")
    print("\n>>> OFERTA DE PLATOS Y BEBIDAS DISPONIBLES:")
    print("---------------------------------------------------------------------")
    gestion_restaurante.desplegar_carta_gastronomica()

    print("\n>>> COMPENDIO DE CLIENTES ENROLADOS:")
    print("---------------------------------------------------------------------")
    gestion_restaurante.desplegar_lista_comensales()
    print("=====================================================================\n")

if __name__ == "__main__":
    ejecutar_aplicacion()