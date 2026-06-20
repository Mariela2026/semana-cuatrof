# ==========================================================
# SERVICIO: Operaciones de Gestión del Restaurante
# ----------------------------------------------------------
# Actúa como controlador para administrar la carta y los clientes.
# ==========================================================

class Restaurante:
    def __init__(self, nombre_establecimiento):
        """
        Establece el nombre del negocio e inicializa los almacenes de datos.
        """
        self.nombre_establecimiento = nombre_establecimiento
        self.catalogo_platos = []
        self.padron_clientes = []

    def incorporar_item_menu(self, nuevo_producto):
        """
        Añade un nuevo elemento a la oferta gastronómica.
        """
        self.catalogo_platos.append(nuevo_producto)

    def enrolar_nuevo_cliente(self, nuevo_cliente):
        """
        Almacena el registro de un nuevo comensal.
        """
        self.padron_clientes.append(nuevo_cliente)

    def desplegar_carta_gastronomica(self):
        """
        Imprime detalladamente todos los productos cargados.
        """
        if not self.catalogo_platos:
            print(" La carta se encuentra vacía temporalmente.")
        else:
            for item in self.catalogo_platos:
                print(item.obtener_detalle())

    def desplegar_lista_comensales(self):
        """
        Muestra la información de contacto de todos los clientes.
        """
        if not self.padron_clientes:
            print(" No existen comensales registrados en la jornada.")
        else:
            for usuario in self.padron_clientes:
                print(usuario.obtener_perfil())