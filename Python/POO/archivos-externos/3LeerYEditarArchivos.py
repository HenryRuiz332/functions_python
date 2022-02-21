from io import open

archivotexto = open("files/ejemplo.txt", "r+");#Lee y escribe

#result = archivotexto.readlines();

listTexto = archivotexto.readlines();

listTexto[1] = " Esta henry linea ha sido modificada desde otro archivo \n";

archivotexto.seek(0);

archivotexto.writelines(listTexto);

archivotexto.close();