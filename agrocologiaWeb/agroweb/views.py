from django.shortcuts import render

from django.http import HttpResponse



def index(request):

    return HttpResponse("Que pasa gente, si hicienron bien las cosas tendrian que ver esto. la base de datos se llamara agrodb para que las configuren en sus maquinas, el sabado vamos a hacer los modulos para poder tener la base de datos :D vemos ahora :D")

