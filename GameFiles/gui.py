import PySimpleGUI as sg
import xlwt
import random
import os
from pygame import mixer

# Configs
coins = 0
Health = 10
Houses = 0
workers = 1
resets = 0
Attack = 2
Boss_Attack = 50
mega_resets = 0
Kills = 0
EDam = 1
Boss_Health = 100
# this part of the config set the prices for the buy menu and the names for the item
worker_cost = 100
House_Cost = 10000
reset_cost = 1000000
Health_Cost = 50
mega_reset_cost = 4

# key list
# window['-TEXT-'].update(coins)
# window['-TEXT1-'].update(Attack)
# window['-TEXT2-'].update(Health)
# window['-TEXT3-'].update(Kills)
# window['-TEXT4-'].update(workers)
# window['-TEXT5-'].update(worker_cost)
# window['-TEXT6-'].update(EDam)
# window['-TEXT7-'].update(Boss_Health)
# window['-TEXT8-'].update(Boss_Attack)

# This is the Gui Layouts
sg.theme('Dark Green 7')

layout = [[sg.Text("Coins"), sg.Text(coins, key='-TEXT-'), sg.Button("Fight"), sg.Button('Boss'),
           [sg.Checkbox('Auto Work:', key='checkbox')],
           sg.Push(), sg.Text("kills"),
           sg.Text(Kills, key='-TEXT3-')],
          [sg.Text("Health"), sg.Text(Health, key='-TEXT2-'), sg.Button("Buy Slave"), sg.Push(), sg.Text("Slave Cost"),
           sg.Text(worker_cost, key='-TEXT5-')],
          [sg.Text("Attack"), sg.Text(Attack, key='-TEXT1-'), sg.Button("Work"), sg.Button("Grind"), sg.Push(), sg.Text("Difficulty"),
           sg.Text(EDam, key='-TEXT6-')],
          [sg.Text("Workers"), sg.Text(workers, key='-TEXT4-'), sg.Button("Heal"), sg.Push(),
           sg.Text("Boss Health"), sg.Text(Boss_Health, key='-TEXT7-')],
          [sg.Button("Quit"), sg.Button("Save"), sg.Push(), sg.Text("Boss Attack"), sg.Text(Boss_Attack, key='-TEXT8-')],
          [sg.VPush(), sg.Text("https://github.com/ModDayHippie/IdleGame/tree/main for more updates"),
           [sg.Text("Goal of the game is to kill 1000 bad guys!!")],
                    [sg.Text(" The game will end if you have 0 health or negitive money")]]]

                                # these numpers are the window sixe first is width second is hight
window = sg.Window('MDH-ClickerGame', layout, size=(400, 300))

# Main Event Loop

while True:
    event, values = window.read()
    window['-TEXT-'].update(coins)
    window['-TEXT1-'].update(Attack)
    window['-TEXT2-'].update(Health)
    window['-TEXT3-'].update(Kills)
    window['-TEXT4-'].update(workers)
    window['-TEXT5-'].update(worker_cost)
    window['-TEXT6-'].update(EDam)
    window['-TEXT7-'].update(Boss_Health)
    window['-TEXT8-'].update(Boss_Attack)

    if event in ('Quit'):
        break

    elif values['checkbox'] == True:
        print("hello")

    if event in ('Buy Slave'):
        if coins <= worker_cost:
            window['-TEXT-'].update(coins)
            window['-TEXT1-'].update(Attack)
            window['-TEXT2-'].update(Health)
            window['-TEXT3-'].update(Kills)
            window['-TEXT4-'].update(workers)
            window['-TEXT5-'].update(worker_cost)
            window['-TEXT6-'].update(EDam)
            window['-TEXT7-'].update(Boss_Health)
            window['-TEXT8-'].update(Boss_Attack)
        else:
            mixer.init()
            mixer.music.load("coin.mp3")
            mixer.music.set_volume(10)
            mixer.music.play()
            coins -= 1 * worker_cost
            workers += 1
            worker_cost += 200 * workers
            # these lines update the window, test 1 - 3 are diffrent variables
            window['-TEXT-'].update(coins)
            window['-TEXT2-'].update(Health)
            window['-TEXT4-'].update(workers)
            window['-TEXT5-'].update(worker_cost)
            print("buy")

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
        mixer.init()
        mixer.music.load("health.mp3")
        mixer.music.set_volume(0.3)
        mixer.music.play()
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
            mixer.init()
            mixer.music.load("oof.mp3")
            mixer.music.set_volume(0.5)
            mixer.music.play()
            # you lose some health
            Health -= EDam
            # this updates the window texts
            window['-TEXT-'].update(coins)
            window['-TEXT2-'].update(Health)
        else:
            # you kill the bandit
            mixer.init()
            mixer.music.load("Sword.mp3")
            mixer.music.set_volume(0.3)
            mixer.music.play()
            # playsound('Sword.wav')
            # Health -= Attack * (resets + 1)
            coins += 20
            Kills += 1
            EDam += 0.3 * Kills
            # this updates the window texts
            window['-TEXT-'].update(coins)
            window['-TEXT2-'].update(Health)
            window['-TEXT3-'].update(Kills)
            window['-TEXT6-'].update(EDam)

    if event in ('Work'):
        mixer.init()
        mixer.music.load("work.mp3")
        mixer.music.set_volume(0.3)
        mixer.music.play()
        # add coins based on workers * 5
        coins += 5 * workers
        window['-TEXT-'].update(coins)
    # if your coins are less then 0 you lose
    if coins < 0:
        os.system("EndMenu.py")
        os.close()
        # break
    # if your health is 0 or less you lose
    if Health <= 0:
        os.system("EndMenu.py")
        os.close()
        # break

    if event in ('Boss'):
        # rng picks a number
        Boss_Rng = random.randint(0, 10)
        # if number is less then 8
        if Boss_Rng < 9:
            mixer.init()
            mixer.music.load("oof.mp3")
            mixer.music.set_volume(0.5)
            mixer.music.play()
            Health -= Boss_Attack
            window['-TEXT2-'].update(Health)
        else:
            Boss_Health -= Attack
            Boss_Attack += 3
            mixer.init()
            mixer.music.load("Sword.mp3")
            mixer.music.set_volume(0.3)
            mixer.music.play()
            window['-TEXT-'].update(coins)
            window['-TEXT2-'].update(Health)
            window['-TEXT3-'].update(Kills)
            window['-TEXT7-'].update(Boss_Health)
            window['-TEXT8-'].update(Boss_Attack)

    if event in ('Grind'):
        Grind_Rng = random.randint(0, 10)
        if Grind_Rng < 8:
            coins += 8 * workers * 10
            workers -= 1
        else:
            coins += 8 * workers * 10
            window['-TEXT-'].update(coins)
            window['-TEXT2-'].update(Health)
            window['-TEXT3-'].update(Kills)
            window['-TEXT4-'].update(workers)
            window['-TEXT5-'].update(worker_cost)
            window['-TEXT6-'].update(EDam)
            window['-TEXT7-'].update(Boss_Health)
            window['-TEXT8-'].update(Boss_Attack)

    if Kills == 5:
        Attack += 2
        window['-TEXT-'].update(coins)
        window['-TEXT1-'].update(Attack)
        window['-TEXT2-'].update(Health)
        window['-TEXT3-'].update(Kills)
        window['-TEXT4-'].update(workers)
        window['-TEXT5-'].update(worker_cost)
        window['-TEXT6-'].update(EDam)
        window['-TEXT7-'].update(Boss_Health)
        window['-TEXT8-'].update(Boss_Attack)
    if Kills == 10:
        Attack += 3
        window['-TEXT-'].update(coins)
        window['-TEXT1-'].update(Attack)
        window['-TEXT2-'].update(Health)
        window['-TEXT3-'].update(Kills)
        window['-TEXT4-'].update(workers)
        window['-TEXT5-'].update(worker_cost)
        window['-TEXT6-'].update(EDam)
        window['-TEXT7-'].update(Boss_Health)
        window['-TEXT8-'].update(Boss_Attack)
    if Kills == 15:
        Attack += 4
        window['-TEXT-'].update(coins)
        window['-TEXT1-'].update(Attack)
        window['-TEXT2-'].update(Health)
        window['-TEXT3-'].update(Kills)
        window['-TEXT4-'].update(workers)
        window['-TEXT5-'].update(worker_cost)
        window['-TEXT6-'].update(EDam)
        window['-TEXT7-'].update(Boss_Health)
        window['-TEXT8-'].update(Boss_Attack)
    if Kills == 20:
        Attack += 5
        window['-TEXT-'].update(coins)
        window['-TEXT1-'].update(Attack)
        window['-TEXT2-'].update(Health)
        window['-TEXT3-'].update(Kills)
        window['-TEXT4-'].update(workers)
        window['-TEXT5-'].update(worker_cost)
        window['-TEXT6-'].update(EDam)
        window['-TEXT7-'].update(Boss_Health)
        window['-TEXT8-'].update(Boss_Attack)



window.close()