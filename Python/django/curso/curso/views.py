from django.http import HttpResponse
import datetime
import json


from django.template import Template, Context

#primera vista

def inicio(request):


	docExterno = open("A:/laragon/www/Python/django/curso/curso/templates/index.html") 
	plt = Template(docExterno.read())

	docExterno.close()

	ctx = Context()

	documento = plt.render(ctx)

	return HttpResponse(documento)

def vista(request):
	return HttpResponse("Carga de django")


def about(request):
	return HttpResponse("Quienes Somos")


def calculaEdad(request, edad, ano):
	
	periodo = ano - 2021
	edadFutura = edad + periodo
	documento = "<htm><body>En el año %s tendras %s  años" %(ano,edadFutura)
	return HttpResponse(documento)