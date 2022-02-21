from datetime import date, datetime, timedelta
import mysql.connector
from mysql.connector import errorcode
import json
import statistics as stats

fecha = datetime.now()




##OBTENEMOS DATOS HTM DE UNA WEB

import urllib.request
import os
from datetime import date
from datetime import datetime






fechaStrHtml = str(fecha.day)+'_'+str(fecha.month)+'_'+str(fecha.year)+'_'+str(fecha.hour)+'_'+str(fecha.minute)+'_'+str(fecha.second)

datosPreciosHoy = urllib.request.urlopen('https://preciohoy.com/prevision-euro-dolar').read().decode()

datosFinanzas = urllib.request.urlopen('https://cincodias.elpais.com/mercados/divisas/eurosxdolares_usa/41/').read().decode()



#Primer valor obtenido
exchangeratesapi = urllib.request.urlopen('https://api.exchangeratesapi.io/latest').read().decode()
strValor = exchangeratesapi
y = json.loads(strValor)
valorDolar = y['rates']['USD']
float(valorDolar)
#print(valorDolar)




from bs4 import BeautifulSoup
soup =  BeautifulSoup(datosPreciosHoy,'html.parser')
pagina1 =  soup.find_all('div', {'class','rightma'})


from bs4 import BeautifulSoup
soup2 =  BeautifulSoup(datosFinanzas,'html.parser')
#pagina2 =  soup.find_all('section', {'class','header-ticker'})
pagina2 =  soup2.find_all('section')



#Vaor obtenido de 
obtenerPrecioDatosPreciosHoy = soup.find_all('td', {'class','bn'})
x = obtenerPrecioDatosPreciosHoy[0].find('strong').next
#print(x)
float(x)

valoresDelMercado = [valorDolar, float(x)]
precioDolarMegatodo = stats.mean(valoresDelMercado)
# print(f"promedio = {stats.mean(valoresDelMercado)}")  



# print(tags)
obtener = ''
for tag in pagina1:
	obtener = tag


obtenerP = []
for tag2 in pagina2:
	obtenerP.append(tag2);
	


	

def writeFile(nombreArchivo, html):

	archivo = open(nombreArchivo, "w")
	archivo.write(str(html) + os.linesep)
	archivo.close()


# writeFile('pagina'+fechaStrHtml+'.html', obtener)
# writeFile('valorEuro'+fechaStrHtml+'.html', obtenerPrecioDatosPreciosHoy)

# writeFile('obtener2'+fechaStrHtml+'.html', obtenerP)

# writeFile('exchangeratesapi'+fechaStrHtml+'.html', exchangeratesapi)

def TasaCambioV1():
    a = valorDolar
    b = float(x)
    promedio = precioDolarMegatodo

    return [{"valor1":a,"valor2":b,"promedio":promedio}]

print(precioDolarMegatodo)
#print(TasaCambioV1())

# try:
#   cnx = mysql.connector.connect(user='root',
#                                 database='progx_megatodo')

#   cursor = cnx.cursor()
# except mysql.connector.Error as err:
#   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#     print("Error de credenciales")
#   elif err.errno == errorcode.ER_BAD_DB_ERROR:
#     print("La base de datos no existe")
#   else:
#     print(err)
# else:
 

# 	tomorrow = datetime.now().date() + timedelta(days=1)

# 	query = ("UPDATE conversion_monedas set vigente = 0")
# 	cursor.execute(query)

# tasa = ("INSERT INTO conversion_monedas "
#                "(moneda_base, moneda_conversion, tasa, vigente, created_at, updated_at) "
#                "VALUES (%s, %s, %s, %s, %s, %s)")


# data = ('EURO', 'DOLAR', precioDolarMegatodo, 1, fecha, fecha)

# # Insert new employee
# cursor.execute(tasa, data)
# emp_no = cursor.lastrowid



# # Make sure data is committed to the database
# cnx.commit()

# cursor.close()
# cnx.close()
