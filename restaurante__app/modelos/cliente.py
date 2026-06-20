# ==========================================================
# COMPONENTE: Modelo de Cliente
# ----------------------------------------------------------
# Modela los datos de los comensales que realizan pedidos.
# ==========================================================

class Cliente:
    def __init__(self, identificacion, nombres_completos, correo_electronico):
        """
        Asigna las credenciales básicas del consumidor.
        """
        self.identificacion = identificacion
        self.nombres_completos = nombres_completos
        self.correo_electronico = correo_electronico

    def obtener_perfil(self):
        """
        Estructura de manera legible el perfil del usuario registrado.
        """
        return f"ID: {self.identificacion} | Nombre: {self.nombres_completos} | Email: {self.correo_electronico}"

    def __str__(self):
        """
        Retorna la identidad nominal cuando se interactúa de forma directa con el objeto.
        """
        return self.nombres_completos