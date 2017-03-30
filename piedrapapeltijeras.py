# !/usr/bin/python
# -*-coding: utf-8-*-

piedra = 1
Papel = 2
Tijera = 3
 
J1 = input("J1 Elige una Opcion: 1)Piedra, 2)Papel o 3)Tijeras: ")
J2 = input("J2 Elige una Opcion: 1)Piedra, 2)Papel o 3)Tijeras: ")

if(J1 == 1):
	if(J2 == 1):
		print "Empate"

if(J1 == 1):
	if(J2 == 2):
		print "J2 Gana"

if(J1 == 1):
	if(J2 == 3):
		print "J1 Gana"

if(J1 == 2):
	if(J2 == 1):
		print "J1 Gana"

if(J1 == 2):
	if(J2 == 2):
		print "Empate"

if(J1 == 2):
	if(J2 == 3):
		print "J2 Gana"

if(J1 == 3):
	if(J2 == 1):
		print "J2 Gana"

if(J1 == 3):
	if(J2 == 2):
		print "J1 Gana"

if(J1 == 3):
	if(J2 == 3):
		print "Empate"

