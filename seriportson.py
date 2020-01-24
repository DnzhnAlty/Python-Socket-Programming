#! /usr/bin/env python
# -*- coding: UTF-8 -*-
# encoding=ascii
from serial.tools import list_ports
from tkinter import ttk
from tkinter import *
import tkinter as fk
import serial.tools.list_ports
from tkinter import messagebox as msg
import serial
import threading
import time
import os

import serial.tools.list_ports

comlist=[]

konum = os.getcwd() +"/" +os.path.basename(__file__)
konum = os.path.normpath(konum)


for port in serial.tools.list_ports.comports():
        comlist.append(port.device)





class Root(Tk):

    def __init__(self):

        super(Root,self).__init__()
        self.title("Serial Communication App")
        self.minsize(1300,500)
        self.maxsize(1300,500)
        self.iconbitmap("icon.ico")

        self.Combo_box()
        self.Label_box()
        self.Button_box()
        self.Text_box()
        self.Space()
        self.MessageWelcome()


    def Combo_box(self):                                    #Listeleme kutusu

        self.comstring=StringVar()
        self.combo_comliste=ttk.Combobox(self,width=10,textvariable=self.comstring,values=comlist)
        self.combo_comliste.grid(column=2,row=0)

        self.baudstring=StringVar()
        self.combo_baudliste = ttk.Combobox(self, width=10,textvariable=self.baudstring)
        self.combo_baudliste["values"]=("4800","9600","19200","38400","57600","115200","23040","460800","921600","1500000")
        self.combo_baudliste.grid(column=2, row=1)

    def Label_box(self):

        self.com_name=ttk.Label(self,text="COM")
        self.com_name.grid(column=0,row=0)

        self.label_2 = ttk.Label(self, text=":")
        self.label_2.grid(column=1, row=0)

        self.com_listting= ttk.Label(self, text="Available COM's List")
        self.com_listting.grid(column=0, row=2)

        self.com_baudrate = ttk.Label(self, text="BaudRate")
        self.com_baudrate.grid(column=0, row=1)

        self.label_2 = ttk.Label(self, text=":")
        self.label_2.grid(column=1, row=1)

        self.label_2 = ttk.Label(self, text=":")
        self.label_2.grid(column=1, row=2)

        self.incominglabel=ttk.Label(self,text="Incoming Data")
        self.incominglabel.grid(column=3,row=6)

    def Button_box(self):

        self.label_9 = ttk.Label(self, text="  ")
        self.label_9.grid(column=3, row=0)

        self.select_com=ttk.Button(self,text="Select",command=self.Msgcombaud)
        self.select_com.grid(column=3,row=0)

        self.refresh_comlist = ttk.Button(self, text="Refresh", command=self.RefComlist)
        self.refresh_comlist.grid(column=3, row=2)

        self.run_comlist = ttk.Button(self, text="Run", command=self.SerialConnection)
        self.run_comlist.grid(column=2, row=4)

        self.sending_comlist = ttk.Button(self, text="Sending",command=self.SendingDataThreading)
        self.sending_comlist.grid(column=1, row=5)

        self.incoming_comlist = ttk.Button(self, text="Incoming",command=self.IncomingDataThreading )
        self.incoming_comlist.grid(column=3, row=5)

        self.senddata_comlist = ttk.Button(self, text="Send Data",command=self.Sendingdata)
        self.senddata_comlist.grid(column=1, row=8)

    def Text_box(self):

        self.text_1=Text(self,width=40,height=8,background="WHITE")
        self.text_1.grid(column=2,row=2)

        self.sending_text_value=StringVar()
        self.sending_text =ttk.Entry(self, width=40,textvariable=self.sending_text_value)
        self.sending_text.grid(column=1, row=7)


        self.incoming_text = Text(self, width=40, height=8, background="WHITE")
        self.incoming_text.grid(column=3, row=7)


    def RefComlist(self):

        ports = list(serial.tools.list_ports.comports())
        for self.com_list in ports:
             self.text_1.insert(0.0,(self.com_list))
             self.text_1.insert(0.0,"\n")

    def MessageWelcome(self):
        msg.showinfo("About","Coded by Denizhan ALTAY")


    def Msgcombaud(self):

        msg.showinfo("Configured","COM         :"+self.comstring.get()+"\n"+"BaudRate :"+self.baudstring.get())


    def Space(self):
        self.spacelabel1=ttk.Label(self,text=" ")
        self.spacelabel1.grid(row=6,column=1)



    def SerialConnection(self):

        self.serialport = serial.Serial()                      # serialport
        self.serialport.baudrate = int(self.baudstring.get())  # Sadece 1 tane seiral port programı  açık olmalı
        self.serialport.port = self.comstring.get()  #
        # deger'i yolla.
        print(self.serialport)
        print(self.serialport.isOpen())

        if (self.serialport.isOpen() == True):
            print(self.serialport.name)
            self.serialport.close()

        elif (self.serialport.isOpen() == False):
            print(self.serialport.name)
            self.serialport.open()

        print(self.serialport.name)

        # serialport.close()

        # serialport.open()

        print(self.serialport.isOpen())

        print(self.serialport)


    def Incomingdata(self):                                       ###YOLLANAN###
        while 1:

            #print(self.serialport.readline().decode("ascii"))
            
            self.incoming_text.insert(END,self.serialport.readline().decode("ascii")+"\n")
            self.incoming_text.see(END)

    def IncomingDataThreading(self):
        threading2 = threading.Thread(target=self.Incomingdata)  ###############TAMAM###############

        threading2.start()


    def Sendingdata(self):                                        ###GÖNDERDİĞİMİZ###          #
        while 1:


            #self.sending_text.insert(END,str(self.sending_text.get()))

            #yollanan=.encode('ascii')
            try :
                self.serialport.write(self.sending_text_value.get().decode('ascii'))
                time.sleep(0.1)

                self.threading1.daemon()
            except AttributeError :
                msg.showinfo("Error", "Please select Com and BaudRate")
                #msg.showinfo("Konumu",konum)
                break




    def SendingDataThreading(self):
        self.threading1 = threading.Thread(target=self.Sendingdata)

        self.threading1.start()




if __name__ == '__main__':

    root=Root()
  
    root.mainloop()

print(
    "\n".join(
        [
            port.device
            for port in list_ports.comports()

        ]))