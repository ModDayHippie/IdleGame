import PySimpleGUI as sg
import xlwt
import random
import os

# Configs
coins = 100
Health = 10
Houses = 0
workers = 1
resets = 0
Attack = 2
Boss_Attack = 7
mega_resets = 0
Kills = 0

# this part of the config set the prices for the buy menu and the names for the item
worker_cost = 100
House_Cost = 10000
reset_cost = 1000000
Health_Cost = 50
mega_reset_cost = 4

# This is the Gui Layouts

sg.theme('Dark Green 7')

layout = [[sg.Text("Coins"), sg.Text(coins, key='-TEXT-'), sg.Button("Fight"), sg.Text("kills"),
           sg.Text(Kills, key='-TEXT3-')],
          [sg.Text("Health"), sg.Text(Health, key='-TEXT2-'), sg.Button("Store")],
          [sg.Text("Attack"), sg.Text(Attack), sg.Button("Work")],
          [sg.Text("Workers"), sg.Text(workers, key='-TEXT4-'), sg.Button("Heal")],
          [sg.Button("Quit"), sg.Button("Save")],
          [sg.Text("If you like the game please follow for more updates")]]

window = sg.Window('MDH-IdleGame', layout)

# Main Event Loop

while True:
    event, values = window.read()
    window['-TEXT-'].update(coins)
    window['-TEXT2-'].update(Health)
    window['-TEXT3-'].update(Kills)
    window['-TEXT4-'].update(workers)

    if event in ('Quit'):
        break

    if event in ('Store'):
        coins -= 1 * worker_cost
        workers += 1
        # these lines update the window, test 1 - 3 are diffrent variables
        window['-TEXT-'].update(coins)
        window['-TEXT2-'].update(Health)
        window['-TEXT4-'].update(workers)

    if event in ('Save'):
        # this will save to an exel file
        book = xlwt.Workbook(encoding="utf-8")
        sheet1 = book.add_sheet("Sheet 1")
        sheet1.write(0, 0, "coins")
        sheet1.write(1, 0, "kills")
        sheet1.write(2, 0, "health")
        sheet1.write(0, 1, coins)
        sheet1.write(1, 1, Health)
        sheet1.write(2, 1, Attack)
        book.save("GameSave.xls")

    if event in ('Heal'):
        coins -= 20
        Health += 5
        # update window
        window['-TEXT-'].update(coins)
        window['-TEXT2-'].update(Health)

    if event in ('Fight'):
        # rng picks a number from 1-10
        Attack_Rng = random.randint(0, 10)
        # if number is less then 5
        if Attack_Rng < 5:
            # you lose some health
            Health -= Attack * (resets + 1)
            # this updates the window texts
            window['-TEXT-'].update(coins)
            window['-TEXT2-'].update(Health)
        else:
            # you kill the bandit
            # Health -= Attack * (resets + 1)
            coins += 20
            Kills += 1
            # this updates the window texts
            window['-TEXT-'].update(coins)
            window['-TEXT2-'].update(Health)
            window['-TEXT3-'].update(Kills)

    if event in ('Work'):
        # add coins based on workers * 5
        coins += 5 * workers
        window['-TEXT-'].update(coins)
    # if your coins are less then 0 you lose
    if coins < 0:
        os.system("test.py")
        os.close()
        # break
    # if your health is 0 or less you lose
    if Health <= 0:
        os.system("test.py")
        os.close()
        # break
window.close()