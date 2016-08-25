

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
    
    def insertRol(nombre_entrada,comprar_entrada,vender_entrada,solicitud_entrada,contestar_solicitud_entrada,cambiar_estado_entrada,publicar_noticias_entrada,consultar_historial_entrada):
        r=Roles()
        r.nombre=nombre_entrada
        r.comprar=comprar_entrada
        r.vender=vender_entrada
        r.solicitud=solicitud_entrada
        r.contestar_solicitud=contestar_solicitud_entrada
        r.cambiar_estado=cambiar_estado_entrada
        r.publicar_noticias=publicar_noticias_entrada
        r.consultar_historial=consultar_historial_entrada
        r.save()
        return "Ha insertado el Rol: "+ nombre_entrada +" exitosamente."
    
    def updateRol(id_actualizar, nombre_actualizar,comprar_actualizar,vender_actualizar,solicitud_actualizar,contestar_solicitud_actualizar,cambiar_estado_actualizar,publicar_noticias_actualizar,consultar_historial_actualizar):
        r=Roles()
        
        r.id=id_actualizar
        r.nombre=nombre_actualizar
        r.comprar=comprar_actualizar
        r.vender=vender_actualizar
        r.solicitud=solicitud_actualizar
        r.contestar_solicitud=contestar_solicitud_actualizar
        r.cambiar_estado=cambiar_estado_actualizar
        r.publicar_noticias=publicar_noticias_actualizar
        r.consultar_historial=consultar_historial_actualizar
        r.save()
        
        return "ha actualizado exitosamente"
    
    def selectRol(nombre_entrada):
        return Roles.objects.filter(nombre=nombre_entrada).values('id','nombre','comprar','vender','solicitud','contestar_solicitud','cambiar_estado','publicar_noticias','consultar_historial')

    def deleteRol(id_delete):
        r=Roles.objects.filter(id=id_delete)
        r.delete()
        
        return "Ha borrado a: "+ nombre_delete
            
class Usuarios(models.Model):
       
    nombre= models.CharField(max_length=100)
    documento=models.IntegerField()
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
    
    
    def insertUser(nombre_user,documento_user,telefono_user,correo_user,direccion_user,placaCarro_user, ciudad_user, codigoPostal_user, password_user, rol_user):
        user=Usuarios()
        user.nombre=nombre_user
        user.documento=documento_user
        user.telefono=telefono_user
        user.correo=correo_user
        user.direccion=direccion_user
        user.placa_carro=placaCarro_user
        user.ciudad=ciudad_user
        user.codigo_postal=codigoPostal_user
        user.password=password_user
        user.rol_id=rol_user
        user.save()
        return "Ha insertado el Rol: "+ nombre_entrada +" exitosamente."
    
    def updateUsuarios(id_actualizar,nombre_user_actualizar,documento_user_actualizar,telefono_user_actualizar,correo_user_actualizar,direccion_user_actualizar,placaCarro_user_actualizar, ciudad_user_actualizar, codigoPostal_user_actualizar, password_user_actualizar, rol_user_actualizar):
        user=Usuarios()
        user.id=id_actualizar
        user.nombre= nombre_user_actualizar
        user.documento=documento_user_actualizar
        user.telefono=telefono_user_actualizar
        user.correo=correo_user_actualizar
        user.direccion=direccion_user_actualizar
        user.placa_carro=placaCarro_user_actualizar
        user.ciudad=ciudad_user_actualizar
        user.codigo_postal=codigoPostal_user_actualizar
        user.password=password_user_actualizar
        user.rol_id=rol_user_actualizar
        user.save()
        return "Datos Actualizados"

    def selectUsuarios(id_entrada):
        return Usuarios.objects.filter(id=id_entrada).values('id','nombre','documento','telefono','correo','direccion','placa_carro','ciudad','codigo_postal','password','rol_id')

    def deleteUsuarios(id_delete):
        user=Usuarios.objects.filter(id=id_delete)
        user.delete()
        
        return "Ha borrado a: "+ id_delete
    
class Tipos_Productos(models.Model):
    nombre= models.CharField(max_length=100)
    descripcion=models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
    
    def insertTipos_Producto(nombre_entrada, descripcion_entrada):
        tipo_producto=Tipos_Productos()
        tipo_producto.nombre=nombre_entrada
        tipo_producto.descripcion=descripcion_entrada
        tipo_producto.save()
        return "Ha insertado el Rol: "+ nombre_entrada +" exitosamente."
    
    def updateTipos_Producto(id_actualizar,nombre_entrada_actualizar, descripcion_entrada_actualizar):
        tipo_producto=Tipos_Productos()
        tipo_producto.id=id_actualizar
        tipo_producto.nombre=nombre_entrada_actualizar
        tipo_producto.descripcion=descripcion_entrada_actualizar
        tipo_producto.save()
        return "Datos Actualizados"

    def select_tipo_producto(id_tipo_producto):
        return Tipos_Productos.objects.filter(id=id_tipo_producto).values('id','nombre','descripcion')

    def delete_tipo_producto(id_delete):
        user=Tipos_Productos.objects.filter(id=id_delete)
        user.delete()
        
        return "Ha borrado a: "+ id_delete
    
    
    
    
class Ofertas(models.Model):
    
    tipo=models.CharField(max_length=100)
    valor_descuento=models.IntegerField()
    descripcion=models.CharField(max_length=100)
    fecha_vencimiento=models.DateField()
    duracion=models.CharField(max_length=100)
    
    def __str__(self):
        return self.tipo
    
    def insert_Ofertas(tipo_entrada, valor_descuento_entrada, descripcion_entrada, fecha_Vencimiento_entrada, duracion_entrada):
        oferta=Ofertas()
        oferta.tipo=tipo_entrada
        oferta.valor_descuento = valor_descuento_entrada
        oferta.descripcion=descripcion_entrada
        oferta.fecha_vencimiento = fecha_Vencimiento_entrada
        oferta.duracion = duracion_entrada
        oferta.save()
        return "Ha insertado el Rol: "+ tipo_entrada +" exitosamente."
    
    def update_oferta(id_entrada_actualizar,tipo_entrada_actualizar, valor_descuento_entrada_actualizar, descripcion_entrada_actualizar, fecha_Vencimiento_entrada_actualizar, duracion_entrada_actualizar):
        oferta=Ofertas()
        oferta.id=id_entrada_actualizar
        oferta.tipo=tipo_entrada_actualizar
        oferta.valor_descuento = valor_descuento_entrada_actualizar
        oferta.descripcion=descripcion_entrada_actualizar
        oferta.fecha_vencimiento = fecha_Vencimiento_entrada_actualizar
        oferta.duracion = duracion_entrada_actualizar
        oferta.save()
        return "Datos Actualizados"

    def select_tipo_oferta(id_oferta):
        return Ofertas.objects.filter(id=id_oferta).values('id','tipo','valor_descuento','descripcion','fecha_vencimiento','duracion')

    def delete_tipo_oferta(id_delete):
        oferta=Ofertas.objects.filter(id=id_delete)
        oferta.delete()
        
        return "Ha borrado a: "+ id_delete
    
    
    
class Productos(models.Model):
    
    nombre=models.CharField(max_length=100)
    precio=models.IntegerField()
    cantidad=models.IntegerField()
    propietario=models.CharField(max_length=100)
    
    oferta=models.ForeignKey(Ofertas, on_delete=models.CASCADE)
    tipo=models.ForeignKey(Tipos_Productos, on_delete=models.CASCADE)
    
    usuarioFK=models.ManyToManyField(Usuarios)
    
    def __str__(self):
        return self.nombre
    
     
    def insert_producto(nombre_entrada, precio_entrada, cantidad_entrada, propietario_entrada, oferta_entrada, tipo_entrada, usuariofk_entrada):
        producto=Productos()
        producto.nombre=nombre_entrada
        producto.precio=precio_entrada
        producto.cantidad=cantidad_entrada
        producto.propietario=propietario_entrada
        producto.oferta=oferta_entrada
        producto.tipo=tipo_entrada
        producto.usuarioFk=usuariofk_entrada
        producto.save()
        return "Ha insertado el Rol: "+ nombre_entrada +" exitosamente."
    
    def update_producto(id_actualizar,nombre_entrada_actualizar, precio_entrada_actualizar, cantidad_entrada_actualizar, propietario_entrada_actualizar, oferta_entrada_actualizar, tipo_entrada_actualizar, usuariofk_entrada_actualizar):
        producto=Productos()
        producto.id=id_actualizar
        producto.nombre=nombre_entrada
        producto.precio = precio_entrada
        producto.cantidad=cantidad_entrada
        producto.propietario = propietario_entrada
        producto.oferta=oferta_entrada
        producto.tipo=tipo_entrada
        producto.usuarioFk=usuariofk_entrada
        producto.save()
        return "Datos Actualizados"

    def select_producto(id_producto):
        return Productos.objects.filter(id=id_producto).values('id','nombre','precio','cantidad','propietario','oferta_id','tipo_id')

    def delete_producto(id_delete):
        producto=Productos.objects.filter(id=id_delete)
        producto.delete()
        
        return "Ha borrado a: "+ id_delete
 
    
class Imagen_Producto(models.Model):
    imagen=models.ImageField(upload_to='/imagenes')
    
    producto=models.ForeignKey(Productos, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.imagen
    
    def insert_imagen(imagen_entrada,producto_entrada):
        imagen=Imagen_Producto()
        imagen.imagen = imagen_entradan
        imagen.producto = producto_entrada
        imagen.save()
        return "Ha insertado el Rol: "+ nombre_entrada +" exitosamente."
    
    def update_imagen(id_entrada_actualizar,imagen_entrada_actualizar,producto_entrada_actualizar):
        imagen=Imagen_Producto()
        imagen.id=id_entrada_actualizar
        imagen.imagen = imagen_entrada_actualizar
        imagen.producto = producto_entrada_actualizar
        imagen.save()
        return "Datos Actualizados"

    def select_imagen(id_imagen):
        return Imagen_Producto.objects.filter(id=id_imagen).values('id','imagen','producto_id')

    def delete_producto(id_delete):
        imagen=Productos.objects.filter(id=id_delete)
        imagen.delete()
        
        return "Ha borrado a: "+ id_delete
 
    
    
class Preguntas_Productos(models.Model):
    
    producto=models.ForeignKey(Productos, on_delete=models.CASCADE)
    pregunta=models.CharField(max_length=100)
    respuesta=models.CharField(max_length=100)
    usuario_remitente=models.ForeignKey(Usuarios, related_name="usuario_remitente_preguntas_productos", on_delete=models.CASCADE)
    usuario_destinatario=models.ForeignKey(Usuarios, related_name="usuario_destinatario_preguntas_productos",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.pregunta
    
    def insert_preguntas_producto(producto_entrada,pregunta_entrada,respuesta_entrada,usuario_remitente_entrada, usuario_destinatario_entrada):
        preguntas=Preguntas_Productos()
        preguntas.producto= producto_entrada
        preguntas.pregunta= pregunta_entrada
        preguntas.respuesta= respuesta_entrada
        preguntas.usuario_remitente = usuario_remitente_entrada
        preguntas.usuario_destinatario = usuario_destinatario_entrada
        preguntas.save()
        return "Ha insertado el Rol: "+ nombre_entrada +" exitosamente."
    
    def update_preguntas_producto(id_entrada,producto_entrada,pregunta_entrada,respuesta_entrada,usuario_remitente_entrada, usuario_destinatario_entrada):
        preguntas=Preguntas_Productos()
        preguntas.id=id_entrada
        preguntas.producto= producto_entrada
        preguntas.pregunta= pregunta_entrada
        preguntas.respuesta= respuesta_entrada
        preguntas.usuario_remitente = usuario_remitente_entrada
        preguntas.usuario_destinatario = usuario_destinatario_entrada
        preguntas.save()
        return "Datos Actualizados"

    def select_preguntas_producto(id_pregunta):
        return Preguntas_Productos.objects.filter(id=id_pregunta).values('id','pregunta','respuesta','producto_id','usuario_destinatario_id','usuario_remitente_id')

    def delete_preguntas_producto(id_delete):
        preguntas=Preguntas_Productos.objects.filter(id=id_delete)
        preguntas.delete()
        
        return "Ha borrado a: "+ id_delete
    
class Noticias(models.Model):
    titulo_noticia=models.CharField(max_length=100)
    contenido_noticia=models.CharField(max_length=500)
    
    propietario=models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.titulo_noticia
    
    def insert_noticias(titulo_noticia_entrada,contenido_noticia_entrada,propietario_entrada):
        noticias=Noticias()
        noticias.titulo_noticia= titulo_noticia_entrada
        noticias.contenido_noticia= contenido_noticia_entrada
        noticias.propietario= propietario_entrada
        noticias.save()
        return "Ha insertado el Rol: "+ nombre_entrada +" exitosamente."
    
    def update_noticias(id_entrada_actualizar,titulo_noticia_entrada_actualizar,contenido_noticia_entrada_actualizar,propietario_entrada_actualizar):
        noticias=Noticias()
        noticias.id=id_entrada_actualizar
        noticias.titulo_noticia= titulo_noticia_entrada_actualizar
        noticias.contenido_noticia= contenido_noticia_entrada_actualizar
        noticias.propietario= propietario_entrada_actualizar
        noticias.save()
        return "Datos Actualizados"

    def select_noticias(id_noticia):
        return Noticias.objects.filter(id=id_noticia).values('id','titulo_noticia','contenido_noticia','propietario_id')

    def delete_noticias(id_delete):
        noticias=Noticias.objects.filter(id=id_delete)
        noticias.delete()
        
        return "Ha borrado a: "+ id_delete
    
    
class Logs(models.Model):
    tipo=models.CharField(max_length=100)
    informacion=models.CharField(max_length=100)
    
    def __str__(self):
        return self.tipo
    
    def insert_logs(tipo_entrada,informacion_entrada):
        log=Logs()
        log.tipo= tipo_entrada
        log.informacion= informacion_entrada
        log.save()
        return "Ha insertado el Rol: "+ nombre_entrada +" exitosamente."
    
    def update_logs(id_entrada,tipo_entrada,informacion_entrada):
        log=Logs()
        log.id=id_entrada
        log.tipo= tipo_entrada
        log.informacion= informacion_entrada
        log.save()
        return "Datos Actualizados"

    def select_logs(id_log):
        return Logs.objects.filter(id=id_log).values('id','tipo','informacion')

    def delete_logs(id_delete):
        log=Logs.objects.filter(id=id_delete)
        log.delete()
        
        return "Ha borrado a: "+ id_delete
    
    
class Solicitudes(models.Model):
    usuario_destinatario=models.ForeignKey(Usuarios, related_name="usuario_destinatario_solicitudes", on_delete=models.CASCADE)
    usuario_remitente=models.ForeignKey(Usuarios, related_name="usuario_remitente_solicitudes", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.usuario_destinatario
    
    def insertSolicitud(usuarioDestinatario,usuarioRemitente):
        r=Solicitudes()
        r.usuario_destinatario=usuarioDestinatario
        r.usuario_remitente=usuarioRemitente
        r.save()
        return "Ha insertado la solicitud exitosamente."

    def updateSolicitud(id_actualizar,usuarioDestinatario,usuarioRemitente):
        r=Solicitudes()
        r.id=id_actualizar
        r.usuario_destinatario=usuarioDestinatario
        r.usuario_remitente=usuarioRemitente
        r.save()
        
        return "ha actualizado exitosamente"
    
    def selectSolicitud(id_select):
        return Solicitudes.objects.filter(id=id_select).values('id','usuario_destinatario','usuario_remitente')

    def deleteSolicitud(id_borrar):
        r=Solicitudes.objects.filter(id=id_borrar)
        r.delete()

        return "Ha borrado a: "+ id_borrar     

    
class Chat(models.Model):
    pregunta=models.CharField(max_length=200)
    respuesta=models.CharField(max_length=200)
    solicitud=models.ForeignKey(Solicitudes, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.pregunta
    
    def insertChat(Pregunta,Respuesta,Solicitud):
        r=Chat()
        r.pregunta=Pregunta
        r.respuesta=Respuesta
        r.solicitud=Solicitud
        r.save()
        return "Ha insertado el chat exitosamente."

    def updateChat(id_actualizar,Pregunta,Respuesta,Solicitud):
        r=Chat()
        r.id=id_actualizar
        r.pregunta=Pregunta
        r.respuesta=Respuesta
        r.solicitud=Solicitud
        r.save()
        
        return "ha actualizado exitosamente"
    
    def selectChat(id_select):
        return Chat.objects.filter(id=id_select).values('id','Pregunta','Respuesta','Solicitud')

    def deleteChat(id_borrar):
        r=Chat.objects.filter(id=id_borrar)
        r.delete()

        return "Ha borrado a: "+ id_borrar 
    
class Carrito_Compra(models.Model):

    usuario=models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    producto=models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad=models.IntegerField()
    
    def __str__(self):
        return self.usuario
    
    
    def insertC_Compra(Usuario,Producto,Cantidad):
        r=Carrito_Compra()
        r.usuario=Usuario
        r.producto=Producto
        r.cantidad=Cantidad
        r.save()
        return "Ha insertado al carrito exitosamente."

    def updateC_Compra(id_actualizar,Usuario,Producto,Cantidad):
        r=Carrito_Compra()
        r.id=id_actualizar
        r.usuario=Usuario
        r.producto=Producto
        r.cantidad=Cantidad
        r.save()
        
        return "ha actualizado exitosamente"
    
    def selectC_Compra(id_select):
        return Carrito_Compra.objects.filter(id=id_select).values('id','Usuario','Producto','Cantidad')

    def deleteC_Compra(id_borrar):
        r=Carrito_Compra.objects.filter(id=id_borrar)
        r.delete()

        return "Ha borrado a: "+ id_borrar
    
class Factura(models.Model):
    valor_total=models.IntegerField()
    estado=models.CharField(max_length=200)
    direccion_envio=models.CharField(max_length=200)
    
    carrito=models.ForeignKey(Carrito_Compra, on_delete=models.CASCADE)
    transportador=models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    
    productosFK=models.ManyToManyField(Productos)
    transportadorFK=models.ManyToManyField(Usuarios, related_name="transportador_mxm",)
    def __str__(self):
        return self.valor_total
    
    def insertFactura(vlr_total,Estado,Direccion,Carrito,Transportador,ProductosFk,TransportadorFk):
        r=Factura()
        r.valor_total=vlr_total
        r.estado=Estado
        r.direccion_envio=Direccion
        r.carrito=Carrito
        r.transportador=Transportador
        r.productosFK=ProductosFk
        r.transportadorFK=TransportadorFk
        r.save()
        return "Ha insertado la factura exitosamente."

    def insertFactura(id_actualizar,vlr_total,Estado,Direccion,Carrito,Transportador,ProductosFk,TransportadorFk):
        r=Factura()
        r.id=id_actualizar
        r.valor_total=vlr_total
        r.estado=Estado
        r.direccion_envio=Direccion
        r.carrito=Carrito
        r.transportador=Transportador
        r.productosFK=ProductosFk
        r.transportadorFK=TransportadorFk
        r.save()
        
        return "ha actualizado exitosamente"
    
    def insertFactura(id_select):
        return Factura.objects.filter(id=id_select).values('id','vlr_total','Estado','Direccion','Carrito','Transportador''ProductosFk','TransportadorFk')

    def insertFactura(id_borrar):
        r=Factura.objects.filter(id=id_borrar)
        r.delete()

        return "Ha borrado a: "+ id_borrar
    