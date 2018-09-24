import serial



f = open("/home/pi/imulogger/temp.mtb","wb")


ser = serial.Serial('/dev/ttyUSB0',921600,timeout=10)

ser.flush()
ser.write(b'\xfa\xff\x40\x00\xc1')
for i in range(100):
	data = ser.read_until(b'\xfa\xff')
	if data[0] ==  13:
		f.write(b'\xfa\xff\x0d')
		f.write(data)
		print("found config")
	printstring = " "
	f.write(data)
	for parts in data:
		printstring = printstring + hex(parts) + ' '
	print(printstring[:30])
ser.close() 
f.close()
