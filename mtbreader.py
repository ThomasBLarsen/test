f = open("/home/pi/imulogger/temp.mtb","rb")
hexstring = ""
for a in f.read():
	hexstring = hexstring + hex(a) + " "
print(hexstring)
f.close()
