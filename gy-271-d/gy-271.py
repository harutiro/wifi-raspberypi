# -*- coding: utf-8 -*-
#!/usr/bin/python

import RPi.GPIO as GPIO
import os
import smbus2 as smbus
import time


QMC5883_REG_OUT_X_M		= 0x01
QMC5883_REG_OUT_X_L		= 0x00
QMC5883_REG_OUT_Z_M		= 0x05
QMC5883_REG_OUT_Z_L		= 0x04
QMC5883_REG_OUT_Y_M		= 0x03
QMC5883_REG_OUT_Y_L		= 0x02
QMC5883_REG_STATUS		= 0x06
QMC5883_REG_CONFIG_1	= 0x09
QMC5883_REG_CONFIG_2	= 0x0A
QMC5883_REG_IDENT_B		= 0x0B
QMC5883_REG_IDENT_C		= 0x20
QMC5883_REG_IDENT_D		= 0x21




# HMC5883L Class
class HMC5883L():
	DevAdr = 0x0d
	myBus = 0
	if GPIO.RPI_INFO['P1_REVISION'] == 1:
		myBus = 0
	else:
		myBus = 1
	b = smbus.SMBus(myBus)

	def setUp(self):
		self.b.write_byte_data(self.DevAdr, QMC5883_REG_IDENT_B,  0x01)
		self.b.write_byte_data(self.DevAdr, QMC5883_REG_IDENT_C,  0x40)
		self.b.write_byte_data(self.DevAdr, QMC5883_REG_IDENT_D,  0x01)
		self.b.write_byte_data(self.DevAdr, QMC5883_REG_CONFIG_1, 0x1d)

	def getValueX(self):
		return self.getValue(QMC5883_REG_OUT_X_L)

	def getValueY(self):
		return self.getValue(QMC5883_REG_OUT_Y_L)

	def getValueZ(self):
		return self.getValue(QMC5883_REG_OUT_Z_L)

	def getValue(self, adr):
		tmp = self.b.read_byte_data(self.DevAdr, adr)
		sign = tmp & 0x80
		tmp = tmp & 0x7F
		tmp = tmp<<8
		tmp = tmp | self.b.read_byte_data(self.DevAdr, adr+1)

		if sign > 0:
			tmp = tmp - 32768

		return tmp

#	tmp = self.b.read_word_data(self.DevAdr, adr)

# MAIN
myHMC5883L = HMC5883L()
myHMC5883L.setUp()

# LOOP
for a in range(1000):
	x = myHMC5883L.getValueX()
	y = myHMC5883L.getValueY()
	z = myHMC5883L.getValueZ()
	# print(f"X={x} , Y={y} , Z={z} ")
	print(f"{x},{y},{z} ")
	time.sleep(0.1)