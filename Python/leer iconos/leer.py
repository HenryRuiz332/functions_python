import os
import urllib
from bs4 import BeautifulSoup
from datetime import date, datetime, timedelta
import mysql.connector
from mysql.connector import errorcode
import json
import statistics as stats


fontawesome5 = './fontawesome5/'
contenido = os.listdir(fontawesome5)

iconos = []
for i in range(len(contenido)):
    	# if os.path.isfile(os.path.join(fontawesome5, fichero)) and fichero.endswith('.svg'):
	    #     iconos.append(fichero)
	f = open(fontawesome5 + '' +contenido[i] , 'r')
	name = [contenido[i]] #name icon
	
	svg = f.readlines()
	iconos.append(svg[0])
	f.close()


	try:
	  cnx = mysql.connector.connect(user='root',
	                                database='python')

	  cursor = cnx.cursor()
	except mysql.connector.Error as err:
	  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
	    print("Error de credenciales")
	  elif err.errno == errorcode.ER_BAD_DB_ERROR:
	    print("La base de datos no existe")
	  else:
	    print(err)
	else:
	 	
		insert = ("INSERT INTO iconos "
               "(name,svg) "
               "VALUES (%s, %s)")

		
		
		data =(name, svg)
		
		cursor.execute(insert,data)
		
		emp_no = cursor.lastrowid

		# Make sure data is committed to the database
		cnx.commit()

		cursor.close()
		cnx.close()

	


 # $g = DB::select("select * from iconos");
       
 #        foreach ($g as $key => $value) {
 #            $svg = $value->svg;
 #            echo $svg;
 #             return
 #            $f = explode("/",$value);

 #            return $f;
 #        } php