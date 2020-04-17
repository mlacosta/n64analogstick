
# Precise N64 Analog Stick and buttons mapping
# by Mariano L. Acosta (marianoacosta.003@gmail.com)

from System.IO.Ports import SerialPort 

if starting:
	_serial = SerialPort("COM3",115200) 
	_serial.Open()	

val = _serial.ReadLine()  
data = val.split(" ",2) #maxsplit

x_val = float(data[1])
y_val = float(data[2])

if abs(x_val)>4:
	mouse.deltaX = x_val

if abs(y_val)>4:
	mouse.deltaY = -y_val



if data[0][0] == "4":

	keyboard.setKeyDown(Key.A)
else:
    keyboard.setKeyUp(Key.A)

if data[0][1] == "4":

	keyboard.setKeyDown(Key.B)
else:
    keyboard.setKeyUp(Key.B)

if data[0][2] == "4":

	keyboard.setKeyDown(Key.Z)
else:
    keyboard.setKeyUp(Key.Z)

if data[0][3] == "4":

	keyboard.setKeyDown(Key.S)
else:
    keyboard.setKeyUp(Key.S)

if data[0][4] == "4":

	keyboard.setKeyDown(Key.NumberPad8)
else:
    keyboard.setKeyUp(Key.NumberPad8)

if data[0][5] == "4":

	keyboard.setKeyDown(Key.NumberPad2)
else:
    keyboard.setKeyUp(Key.NumberPad2)

if data[0][6] == "4":

	keyboard.setKeyDown(Key.NumberPad4)
else:
    keyboard.setKeyUp(Key.NumberPad4)

if data[0][7] == "4":

	keyboard.setKeyDown(Key.NumberPad6)
else:
    keyboard.setKeyUp(Key.NumberPad6)

if data[0][10] == "4":

	keyboard.setKeyDown(Key.T)
else:
    keyboard.setKeyUp(Key.T)

if data[0][11] == "4":

	keyboard.setKeyDown(Key.R)
else:
    keyboard.setKeyUp(Key.R)

if data[0][12] == "4":

	keyboard.setKeyDown(Key.I)
else:
    keyboard.setKeyUp(Key.I)

if data[0][13] == "4":

	keyboard.setKeyDown(Key.J)
else:
    keyboard.setKeyUp(Key.J)

if data[0][14] == "4":

	keyboard.setKeyDown(Key.M)
else:
    keyboard.setKeyUp(Key.M)

if data[0][15] == "4":

	keyboard.setKeyDown(Key.K)
else:
    keyboard.setKeyUp(Key.K)
   
    
