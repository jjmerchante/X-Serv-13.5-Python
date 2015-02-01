#!/usr/bin/python

fich=open("/etc/passwd","r")
users_lines = fich.readlines()
fich.close()

dicc = {}

for user_line in users_lines:
    lista_user = user_line.split(":")
    username = lista_user[0]
    shell = lista_user[-1][:-1]
    dicc[username]=shell
    
try:
    print "root:", dicc["root"]
    print "imaginario:", dicc["imaginario"]
except KeyError:
    print "Usuario no encontrado"
    