f = open("/home/pi/imulogger/temp.mtb","rb")
hexstring = ""
for a in f.read(30):
	hexstring = hexstring + hex(a) + " "
print(hexstring)
f.close()
