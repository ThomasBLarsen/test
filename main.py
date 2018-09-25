import serial



f = open("/home/pi/imulogger/temp2.mtb","wb")


ser = serial.Serial('/dev/ttyUSB0',921600,timeout=10)

ser.flush()
ser.write(b'\xfa\xff\x40\x00\xc1')
ConfigWritten = False
DataCollect = b''

for i in range(50000):
	data = ser.read_until(b'\xfa\xff')
	if data[0] ==  13:
		f.write(b'\xfa\xff\x0d')
		f.write(data)
		print("found config")
		ConfigWritten = True
	#printstring = " "
	if ConfigWritten:
		DataCollect  += data
		if 100 % i == 0:
			f.write(DataCollect)
			DataCollect = b''
	#for parts in data:
	#	printstring = printstring + hex(parts) + ' '
	#print(printstring[:30])
ser.close() 
f.close()
