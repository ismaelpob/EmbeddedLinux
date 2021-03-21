#!/usr/bin/python

##############################################
##### Test I2C Master transmission and Read
##############################################

import time
import smbus
import struct

##ADDRESS AND I2Cx
I2C_CH = 1
DEVICE_ADDRESS = 0x28
NUMBER_DATA_VAR = 3

##CMD COMMANDS
CHECK_STATUS_CMD       = 0xC1
READ_ID_VER_CMD        = 0xC2
READ_DATA_CMD          = 0xC3
WRITE_TO_PARAMETER_CMD = 0xC4
RESET_SLAVE_CMD        = 0xC5

#DATA LENGTH
LENGTH_READ_ID_VER  = 4;
LENGTH_READ_DATA   = NUMBER_DATA_VAR * 4;
LEN_WRITE_TO_PARAMETER_CMD = 4;

#buffer for read data
buffer_hex = [0x00000000,0x00000000,0x00000000]

#Init 
bus = smbus.SMBus(I2C_CH)

##############################################
##### CHECK STATUS
##############################################
bus.write_byte(DEVICE_ADDRESS, CHECK_STATUS_CMD)
buffer_rx = bus.read_byte(DEVICE_ADDRESS)
if buffer_rx == 254:
    print("Check status: OK")
else:
    print("Check status: ERR")

##############################################
##### CHECK ID AND VERSION
##############################################
buffer_rx = bus.read_i2c_block_data(DEVICE_ADDRESS,READ_ID_VER_CMD, LENGTH_READ_ID_VER)
print("Check ID: " + str(hex(buffer_rx[0])))
print("Check Version: " + chr(buffer_rx[1]) + chr(buffer_rx[2]) + chr(buffer_rx[3]))

##############################################
##### DATA ADQUISITION
##############################################
buffer_rx = bus.read_i2c_block_data(DEVICE_ADDRESS,READ_DATA_CMD, LENGTH_READ_DATA)
buffer_hex[0] = (buffer_rx[0]) + (buffer_rx[1] << 8) + (buffer_rx[2] << 16) + (buffer_rx[3] << 24)
buffer_hex[1] = (buffer_rx[4]) + (buffer_rx[5] << 8) + (buffer_rx[6] << 16) + (buffer_rx[7] << 24)
buffer_hex[2] = (buffer_rx[8]) + (buffer_rx[9] << 8) + (buffer_rx[10] << 16) + (buffer_rx[11] << 24)

print("Data1: " + str(struct.unpack('!f', bytes.fromhex(format(buffer_hex[0], 'x')))[0]))
print("Data2: " + str(struct.unpack('!f', bytes.fromhex(format(buffer_hex[1], 'x')))[0]))
print("Data3: " + str(struct.unpack('!f', bytes.fromhex(format(buffer_hex[2], 'x')))[0]))

##############################################
##### WRITE TO PARAMETER
##############################################

buffer_hex = [0x00,0x00,0x00,0x00]
data_float = 35.6

buffer_hex_full = hex(struct.unpack('<I', struct.pack('<f', data_float))[0])

buffer_hex[0] = int((buffer_hex_full[2]+buffer_hex_full[3]), 16)
buffer_hex[1] = int((buffer_hex_full[4]+buffer_hex_full[5]), 16)
buffer_hex[2] = int((buffer_hex_full[6]+buffer_hex_full[7]), 16)
buffer_hex[3] = int((buffer_hex_full[8]+buffer_hex_full[9]), 16)
bus.write_byte(DEVICE_ADDRESS, WRITE_TO_PARAMETER_CMD)
bus.write_i2c_block_data(DEVICE_ADDRESS, WRITE_TO_PARAMETER_CMD, [buffer_hex[0],buffer_hex[1],buffer_hex[2],buffer_hex[3]])

print('Write to parameter: ' + str(data_float) + " - " + str(buffer_hex_full))

##############################################
##### RESET SLAVE
##############################################
#bus.write_byte(DEVICE_ADDRESS, RESET_SLAVE_CMD)
#print('Slave Software Reset...')




















