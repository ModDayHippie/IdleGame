import PySimpleGUI as sg
import os
sg.theme('Dark Green 7')
layout = [[sg.Text("You Have Been Killed!! Please restart script to play again")],
          [sg.Button("Quit")]]

window = sg.Window('MDH-IdleGame', layout)

while True:
    event, values =window.read()

    if event in ('Quit'):
        break

    #if event in ('restart'):
        #def call_otherfile(self):
            #os.system("gui.py")  # Execute new script
            #os.close()  # close Current Script
        #break