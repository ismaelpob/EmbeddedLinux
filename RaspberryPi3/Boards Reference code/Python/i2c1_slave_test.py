#!/usr/bin/python

##############################################
### Test I2C Master transmission and Read
##############################################

import time
import smbus

##ADDRESS AND I2Cx
I2C_CH = 1
DEVICE_ADDRESS = 0x28

##CMD COMMANDS
MASTER_WRITE_CMD = 0xC1
MASTER_READ_CMD = 0xC2

##Test data register
DEVICE_REG = 0x10

##Data to transmit
buffer_tx = [0x20,0x30,0x40,0x50]
##Data to receive
#1 byte
buffer_byte_rx = 0;
#array of data
#buffer_rx=[0xff,0xff,0xff,0xff];

bus = smbus.SMBus(I2C_CH)

##############################################
### Test send data (DEVICE_REG)
##############################################

#Send 1 byte each 1 sec.
#bus.write_byte(DEVICE_ADDRESS, DEVICE_REG)
#time.sleep(1)

##############################################
### Master write data to slave
##############################################

##Send transmit command
#bus.write_byte(DEVICE_ADDRESS, MASTER_WRITE_CMD)
##Send lenght of: data 5 (BUFFER) + 1 (DEVICE_REG)
#bus.write_byte(DEVICE_ADDRESS, len(buffer_tx) + 1)

##Send DEVICE_REG 0x10  -  [0xC,0x17,0x22,0x2D]
##Form1:
#bus.write_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG, [12, 23, 34, 45])
##Form2:
#bus.write_i2c_block_data(DEVICE_ADDRESS, DEVICE_REG, buffer_tx) 

##############################################
### Master read data from slave
##############################################

##Send read command
#bus.write_byte(DEVICE_ADDRESS, MASTER_READ_CMD)

##Read 1 byte from master
#buffer_byte_rx = bus.read_byte(DEVICE_ADDRESS)
#print (buffer_byte_rx)

##Read data from master
#it send a command MASTER_READ_CMD then it wait the slave data.
#Stm32 will be config like a sequence interrupt.
#buffer_rx = bus.read_i2c_block_data(DEVICE_ADDRESS,MASTER_READ_CMD, 5)
#print (buffer_rx)
