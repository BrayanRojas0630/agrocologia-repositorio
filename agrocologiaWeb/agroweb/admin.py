from django.contrib import admin
#Tabla Roles
from .models import Roles
admin.site.register(Roles)
#-------------------------------------------------------
#Tabla Usuarios
from .models import Usuarios
admin.site.register(Usuarios)
#-------------------------------------------------------
#Tabla Tipos_Productos
from .models import Tipos_Productos
admin.site.register(Tipos_Productos)
#-------------------------------------------------------
#Tabla Ofertas
from .models import Ofertas
admin.site.register(Ofertas)
#-------------------------------------------------------
#Tabla Productos
from .models import Productos
admin.site.register(Productos)
#-------------------------------------------------------
#Tabla Imagen_Producto
from .models import Imagen_Producto
admin.site.register(Imagen_Producto)
#-------------------------------------------------------
#Tabla Preguntas_Productos
from .models import Preguntas_Productos
admin.site.register(Preguntas_Productos)
#-------------------------------------------------------
#Tabla Noticias
from .models import Noticias
admin.site.register(Noticias)
#-------------------------------------------------------
#Tabla Logs
from .models import Logs
admin.site.register(Logs)
#-------------------------------------------------------
#Tabla Solicitudes
from .models import Solicitudes
admin.site.register(Solicitudes)
#-------------------------------------------------------
#Tabla Chat
from .models import Chat
admin.site.register(Chat)
#-------------------------------------------------------
#Tabla Carrito_Compra
from .models import Carrito_Compra
admin.site.register(Carrito_Compra)
#-------------------------------------------------------
#Tabla Factura
from .models import Factura
admin.site.register(Factura)
#-------------------------------------------------------
# Register your models here.
