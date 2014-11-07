import requests
import time
from Tkinter import *


def requestPairing():
    xml = '<?xml version="1.0" encoding="utf-8"?>'\
      '<envelope>'\
      '<api type="pairing">'\
      '<name>hello</name>'\
      '<value>982905</value>'\
      '<port>8080</port>'\
      '</api>'\
      '</envelope>'
    headers = {'Cache-Control': 'no-cache', 'Content-Type': 'text/xml; charset=utf-8', 'Content-Length': '105', 'Connection': 'Close', 'User-Agent':'UDAP/2.0'} # set what your server accepts
    url = 'http://192.168.0.2:8080/udap/api/pairing'
    a =  requests.post(url, data=xml, headers=headers)


    
def sendCommand(char):
    print char
    xml = '<?xml version="1.0" encoding="utf-8"?>'\
          '<envelope><api type="command">'\
          '<name>HandleKeyInput</name>'\
          '<value>'+char+'</value>'\
          '</api>'\
          '</envelope>'
    headers = {'Cache-Control': 'no-cache', 'Content-Type': 'text/xml; charset=utf-8', 'Content-Length': '105', 'Connection': 'Close', 'User-Agent':'UDAP/2.0'} # set what your server accepts
    url = 'http://192.168.0.2:8080/udap/api/command'
    a =  requests.post(url, data=xml, headers=headers)

def key(event):
    print "pressed", repr(event.char)
    print event.char
    if event.char==" ":
        print "Menu"
        sendCommand('47')
    if event.char=="\r":
        print "OK"
        sendCommand('20')
    if event.char=="p":
        print "Power"
        sendCommand('1')
    if event.char=="w":
        time.sleep(0.025)
        print "Vol Up"
        sendCommand('24')
    if event.char=="s":
        time.sleep(0.025)
        print "Vol Down"
        sendCommand('25')
    if event.char=="m":
        print "Mute"
        sendCommand('26')
    if event.char=="r":
        print "Reconnect"
        requestPairing()

def leftKey(event):
    sendCommand('14')

def backSpace(event):
    sendCommand('23')

def rightKey(event):
    sendCommand('15')

def upKey(event):
    sendCommand('12')

def downKey(event):
    sendCommand('13')

def main():
    requestPairing()
    root = Tk()
    frame = Frame(root, width=100, height=100)
    frame.focus_set()
    frame.bind("<Key>", key)
    frame.pack()
    frame.bind('<Left>', leftKey)
    frame.bind('<Right>', rightKey)
    frame.bind('<Down>', downKey)
    frame.bind('<Up>', upKey)
    frame.bind('<BackSpace>', backSpace)

    root.mainloop()

        
        

if __name__=="__main__":
    main()
    
