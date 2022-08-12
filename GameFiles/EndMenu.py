import PySimpleGUI as sg

sg.theme('Dark Green 7')

layout = [[sg.Text("You have died or ran out of coins, please play again")],
          [sg.Button("Quit")]]

window = sg.Window('MDH-IdleGame', layout)

# Main Event Loop

while True:
    event, values = window.read()

    if even in 'Quit':
        break
