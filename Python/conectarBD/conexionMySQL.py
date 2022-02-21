from datetime import date, datetime, timedelta
import mysql.connector
from mysql.connector import errorcode
from config import database

try:
  	cnx = mysql.connector.connect(user='root',
                                database='progx_megatodo')

  	cursor = cnx.cursor()
except mysql.connector.Error as err:
  	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    		print("Error de credenciales")
  	elif err.errno == errorcode.ER_BAD_DB_ERROR:
    		print("La base de datos no existe")
  	else:
    		print(err)
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