# ==========================================================
# COMPONENTE: Modelo de Producto
# ----------------------------------------------------------
# Define la estructura de los alimentos y bebidas del menú.
# ==========================================================

class Producto:
    def __init__(self, identificador, denominacion, valor_unitario, tipo):
        """
        Inicializa un artículo del menú con sus propiedades esenciales.
        """
        self.identificador = identificador
        self.denominacion = denominacion
        self.valor_unitario = valor_unitario
        self.tipo = tipo  # Ejemplo: 'Sopa', 'Segundo', 'Postre', 'Bebida'

    def obtener_detalle(self):
        """
        Retorna una cadena formateada con la descripción completa del ítem.
        """
        return f"[{self.identificador}] {self.denominacion} ({self.tipo}) - Costo: ${self.valor_unitario:.2f}"

    def __str__(self):
        """
        Representación textual simplificada del producto.
        """
        return f"{self.denominacion} [${self.valor_unitario:.2f}]"