from django.db import models
   
class Roles(models.Model):
    id_rol=models.IntegerField()
    
    nombre= models.CharField(max_length=100)
    comprar=models.CharField(max_length=100)
    vender=models.CharField(max_length=100)
    solicitud=models.CharField(max_length=100)
    contestar_solicitud=models.CharField(max_length=100)
    cambiar_estado=models.CharField(max_length=100)
    publicar_noticias=models.CharField(max_length=100)
    consultar_historial=models.CharField(max_length=100)
    
    
class Usuarios(models.Model):
    id_question=models.CharField(max_length=100)
       
    nombre= models.CharField(max_length=100)
    documeto=models.IntegerField()
    telefono=models.IntegerField()
    correo=models.EmailField()
    direccion=models.CharField(max_length=100)   
    placa_carro=models.CharField(max_length=10)
    ciudad=models.CharField(max_length=100)
    codigo_postal=models.IntegerField()
    password=models.CharField(max_length=100)
    
    id_rol=models.ForeignKey(Roles,on_delete=models.CASCADE)#llave foranea del rol
    
    
class Tipos_Productos(models.Model):
    id_tipo=models.IntegerField()
    
    nombre= models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    
# id_producto=models.ForeignKey(Productos, on_delete=models.CASCADE)
# PROBLEMA NO ENCUENTRA la tabla productos por que no se ha creado


class Ofertas(models.Model):
    id_oferta=models.IntegerField()
    
    tipo=models.CharField(max_length=100)
    valor_descuento=models.IntegerField()
    description=models.CharField(max_length=100)
    fecha_vencimiento=models.DateField()
    duracion=models.CharField(max_length=100)

class Productos(models.Model):
    id_producto=models.IntegerField()
    
    nombre=models.CharField(max_length=100)
    precio=models.IntegerField()
    cantidad=models.IntegerField()
    propietario=models.CharField(max_length=100)
    
    id_oferta=models.ForeignKey(Ofertas, on_delete=models.CASCADE)
    id_tipo=models.ForeignKey(Tipos_Productos, on_delete=models.CASCADE)
 
 
    
class Imagen_Producto(models.Model):
    id_imagen=models.IntegerField()
    imagen=models.ImageField(upload_to='/imagenes')
    
    id_producto=models.ForeignKey(Productos, on_delete=models.CASCADE)
    
#class preguntas_productos(models.Model):
#    id_pregunta=models.IntegerField()
#    id_producto=models.ForeignKey(Productos, on_delete=models.CASCADE)
#    pregunta=models.CharField(max_length=100)
#    respuesta=models.CharField(max_length=100)
#   id_usuario_remitente=
#    id_usuario_destinatario=
