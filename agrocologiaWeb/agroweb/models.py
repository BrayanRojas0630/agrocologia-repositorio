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
    
    def __str__(self):
        return self.nombre
    
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
    
    def __str__(self):
        return self.nombre
    
class Tipos_Productos(models.Model):
    nombre= models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Ofertas(models.Model):
    
    tipo=models.CharField(max_length=100)
    valor_descuento=models.IntegerField()
    description=models.CharField(max_length=100)
    fecha_vencimiento=models.DateField()
    duracion=models.CharField(max_length=100)
    
    def __str__(self):
        return self.tipo
    
class Productos(models.Model):
    
    nombre=models.CharField(max_length=100)
    precio=models.IntegerField()
    cantidad=models.IntegerField()
    propietario=models.CharField(max_length=100)
    
    oferta=models.ForeignKey(Ofertas, on_delete=models.CASCADE)
    tipo=models.ForeignKey(Tipos_Productos, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.nombre
 
    
class Imagen_Producto(models.Model):
    imagen=models.ImageField(upload_to='/imagenes')
    
    producto=models.ForeignKey(Productos, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.imagen
    
class Preguntas_Productos(models.Model):
    
    producto=models.ForeignKey(Productos, on_delete=models.CASCADE)
    pregunta=models.CharField(max_length=100)
    respuesta=models.CharField(max_length=100)
    usuario_remitente=models.ForeignKey(Usuarios, related_name="usuario_remitente_preguntas_productos", on_delete=models.CASCADE)
    usuario_destinatario=models.ForeignKey(Usuarios, related_name="usuario_destinatario_preguntas_productos",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.pregunta
    
class Noticias(models.Model):
    titulo_noticia=models.CharField(max_length=100)
    contenido_noticia=models.CharField(max_length=500)
    
    propietario=models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo_noticia
    
class Logs(models.Model):
    tipo=models.CharField(max_length=100)
    informacion=models.CharField(max_length=100)
    
    def __str__(self):
        return self.tipo
    
class Solicitudes(models.Model):
    usuario_destinatario=models.ForeignKey(Usuarios, related_name="usuario_destinatario_solicitudes", on_delete=models.CASCADE)
    usuario_remitente=models.ForeignKey(Usuarios, related_name="usuario_remitente_solicitudes", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.usuario_destinatario
    
class Chat(models.Model):
    pregunta=models.CharField(max_length=200)
    respuesta=models.CharField(max_length=200)
    solicitud=models.ForeignKey(Solicitudes, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.pregunta
    
class Carrito_Compra(models.Model):

    usuario=models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    producto=models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad=models.IntegerField()
    
    def __str__(self):
        return self.usuario
    
class Factura(models.Model):
    valor_total=models.IntegerField()
    estado=models.CharField(max_length=200)
    direccion_envio=models.CharField(max_length=200)
    
    carrito=models.ForeignKey(Carrito_Compra, on_delete=models.CASCADE)
    transportador=models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.valor_total
    