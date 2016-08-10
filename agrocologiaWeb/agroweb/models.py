from django.db import models
   
class Roles(models.Model):
    
    nombre= models.CharField(max_length=100)
    comprar=models.CharField(max_length=100)
    vender=models.CharField(max_length=100)
    solicitud=models.CharField(max_length=100)
    contestar_solicitud=models.CharField(max_length=100)
    cambiar_estado=models.CharField(max_length=100)
    publicar_noticias=models.CharField(max_length=100)
    consultar_historial=models.CharField(max_length=100)
    
    
class Usuarios(models.Model):
       
    nombre= models.CharField(max_length=100)
    documeto=models.IntegerField()
    telefono=models.IntegerField()
    correo=models.EmailField()
    direccion=models.CharField(max_length=100)   
    placa_carro=models.CharField(max_length=10)
    ciudad=models.CharField(max_length=100)
    codigo_postal=models.IntegerField()
    password=models.CharField(max_length=100)
    
    rol=models.ForeignKey(Roles,on_delete=models.CASCADE)#llave foranea del rol
    
    
class Tipos_Productos(models.Model):
    
    nombre= models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    


class Ofertas(models.Model):
    
    tipo=models.CharField(max_length=100)
    valor_descuento=models.IntegerField()
    description=models.CharField(max_length=100)
    fecha_vencimiento=models.DateField()
    duracion=models.CharField(max_length=100)

class Productos(models.Model):
    
    nombre=models.CharField(max_length=100)
    precio=models.IntegerField()
    cantidad=models.IntegerField()
    propietario=models.CharField(max_length=100)
    
    oferta=models.ForeignKey(Ofertas, on_delete=models.CASCADE)
    tipo=models.ForeignKey(Tipos_Productos, on_delete=models.CASCADE)
 
 
    
class Imagen_Producto(models.Model):
    imagen=models.ImageField(upload_to='/imagenes')
    
    producto=models.ForeignKey(Productos, on_delete=models.CASCADE)
    
class Preguntas_Productos(models.Model):
    id_pregunta=models.IntegerField()
    id_producto=models.ForeignKey(Productos, on_delete=models.CASCADE)
    pregunta=models.CharField(max_length=100)
    respuesta=models.CharField(max_length=100)
    id_usuarioemitente=models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    id_usuario_destinatario=models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    
    
class Noticias(models.Model):
    titulo_noticia=models.CharField(max_length=100)
    contenido_noticia=models.CharField(max_length=500)
    
    propietario=models.ForeignKey(Usuarios, on_delete=models.CASCADE)


class Logs(models.Model):
    tipo=models.CharField(max_length=100)
    informacion=models.CharField(max_length=100)
    
    

class Solicitudes(models.Model):
    id_usuario_destinatario=models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    id_usuario_remitente=models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    


class Chat(models.Model):
    pregunta=models.CharField(max_length=200)
    respuesta=models.CharField(max_length=200)
    id_solicitud=models.ForeignKey(Solicitudes, on_delete=models.CASCADE)
    
class Carrito_Compra(models.Model):
    
    
    id_usuario=models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    id_producto=models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad=models.IntegerField()
    
class Factura(models.Model):
    valor_total=models.IntegerField()
    estado=models.CharField(max_length=200)
    direccion_envio=models.CharField(max_length=200)
    
    id_carrito=models.ForeignKey(Carrito_Compra, on_delete=models.CASCADE)
    id_transportador=models.ForeignKey(Usuarios, on_delete=models.CASCADE)