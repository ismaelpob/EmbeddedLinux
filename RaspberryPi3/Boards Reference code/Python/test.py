import smbus
import struct

WRITE_TO_PARAMETER_CMD = 0xC4
LEN_WRITE_TO_PARAMETER_CMD = 4;
DEVICE_ADDRESS = 0x28

bus = smbus.SMBus(1)

buffer_hex = [0x00,0x00,0x00,0x00]
data_float = 35.6

buffer_hex_full = hex(struct.unpack('<I', struct.pack('<f', data_float))[0])
print(buffer_hex_full)

buffer_hex[0] = int((buffer_hex_full[2]+buffer_hex_full[3]), 16)
buffer_hex[1] = int((buffer_hex_full[4]+buffer_hex_full[5]), 16)
buffer_hex[2] = int((buffer_hex_full[6]+buffer_hex_full[7]), 16)
buffer_hex[3] = int((buffer_hex_full[8]+buffer_hex_full[9]), 16)

print(buffer_hex[0])
print(buffer_hex[1])
print(buffer_hex[2])
print(buffer_hex[3])

bus.write_i2c_block_data(DEVICE_ADDRESS, WRITE_TO_PARAMETER_CMD, [buffer_hex[0],buffer_hex[1],buffer_hex[2],buffer_hex[3]])