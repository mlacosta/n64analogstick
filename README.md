# N64 Arduino Controller with 100% Analog Stick Sensitivity (Fix) 
<h3>Author: Mariano L. Acosta</h3>
<h2>What you need:</h2>
<ul>
  <li>A Nintendo 64 controller</li>
  <li>An Arduino UNO</li>
  <li>A set of 3 cables</li>
  <li>FreePie Software (Free)</li>
  <li>An N64 emulator that allows the mouses axis as a control input (i.e w/the NRange Input plugin)</li>

</ul>
<h1>Intro and Motivation</h1>
This project is based on the instructable: https://www.instructables.com/id/Use-an-Arduino-with-an-N64-controller/ by quasse. Originally it uses Processing to read the data sent by the N64 controller in order to control the keyboard and mouse. However, the mouse version of the instructable doesn't work properly with an emulator because the character in a game get stuck when the cursor reaches the border of the screen. This is due the Java class 'Robot' used by the script in Processing that moves the cursor to an absolute position instead of using incremental deltas which are necessary for the controller plugin to correctly track the movement of the stick. A quick solution to this problem is to use the digital pad instead, but with this the sensitivity of the analog stick is lost and therefore the movement is not accurate. 

<h1>The Solution</h1>
After an exahustive search on the internet I found this I/O emulator: https://github.com/AndersMalmgren/FreePIE/wiki (FreePie). So what I did was to create a simple script that reads the serial data sent by the Arduino, then unpack it and map it to the keyboard and mouse. I solved the problem of using 'deltas' in the cursor and now the analog stick works great with full sensitivity in Project 64. To use this solution, load the program 'N64_Arduino.ino' to an Arduino Uno, connect the cables to a N64 controller as the intructable says and then run the script 'N64Stick.py' with FreePie and now you are able to use the controller in a emulator with its full capability. 


<h1>Please Note</h1>
You have to modify the COM port in the script to match your board. In my case I used the 'COM 3' port.
