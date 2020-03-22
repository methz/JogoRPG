import time, os
from player import Player
from map import Map
from enemy import Enemy

def showTitleScreen():

    titleFrame1 = '''                                                                                                                                                                                                                                                                                                                                      
        /$$$$$$$                               /$$ /$$        /$$$$$$   /$$$$$$  /$$   /$$  /$$$$$$ 
        | $$__  $$                             |__/| $$       /$$__  $$ /$$$_  $$| $$  | $$ /$$__  $$
        | $$  \ $$  /$$$$$$  /$$$$$$   /$$$$$$$ /$$| $$      |__/  \ $$| $$$$\ $$| $$  | $$| $$  \ $$
        | $$$$$$$  /$$__  $$|____  $$ /$$_____/| $$| $$        /$$$$$$/| $$ $$ $$| $$$$$$$$|  $$$$$$$
        | $$__  $$| $$  \__/ /$$$$$$$|  $$$$$$ | $$| $$       /$$____/ | $$\ $$$$|_____  $$ \____  $$
        | $$  \ $$| $$      /$$__  $$ \____  $$| $$| $$      | $$      | $$ \ $$$      | $$ /$$  \ $$
        | $$$$$$$/| $$     |  $$$$$$$ /$$$$$$$/| $$| $$      | $$$$$$$$|  $$$$$$/      | $$|  $$$$$$/
        |_______/ |__/      \_______/|_______/ |__/|__/      |________/ \______/       |__/ \______/ 
    '''                                                                                                                                                                       
    
    titleFrame2 = '''
        $$$$$$$\                               $$\ $$\        $$$$$$\   $$$$$$\  $$\   $$\  $$$$$$\  
        $$  __$$\                              \__|$$ |      $$  __$$\ $$$ __$$\ $$ |  $$ |$$  __$$\ 
        $$ |  $$ | $$$$$$\  $$$$$$\   $$$$$$$\ $$\ $$ |      \__/  $$ |$$$$\ $$ |$$ |  $$ |$$ /  $$ |
        $$$$$$$\ |$$  __$$\ \____$$\ $$  _____|$$ |$$ |       $$$$$$  |$$\$$\$$ |$$$$$$$$ |\$$$$$$$ |
        $$  __$$\ $$ |  \__|$$$$$$$ |\$$$$$$\  $$ |$$ |      $$  ____/ $$ \$$$$ |\_____$$ | \____$$ |
        $$ |  $$ |$$ |     $$  __$$ | \____$$\ $$ |$$ |      $$ |      $$ |\$$$ |      $$ |$$\   $$ |
        $$$$$$$  |$$ |     \$$$$$$$ |$$$$$$$  |$$ |$$ |      $$$$$$$$\ \$$$$$$  /      $$ |\$$$$$$  |
        \_______/ \__|      \_______|\_______/ \__|\__|      \________| \______/       \__| \______/ 
    
    '''
                                                                                                                                                                                                                                                                                                                                      
    startTime = time.time()
    currentTime = time.time()  
    counter = 0  
    
    while(currentTime < startTime + 3.0):  
        if counter % 2 == 0:
            print(titleFrame1)                                                                                                                                                            
        else:
            print(titleFrame2)
        counter += 1
        time.sleep(0.3)
        os.system("cls")
        currentTime = time.time()                                                                                                                                    
                                                                                                                                                                       
def main():
    showTitleScreen()   
    p = Player()
    m = Map()
    e = Enemy()
    chosenMap = m.getRandomMap()
    print('Você acordou em', chosenMap, 'sem saber como foi parar aqui...')
    randomEnemy = e.getRandomEnemy(chosenMap)
    print('Oh! Você se deparou com o ' + randomEnemy.name + '.\n Ele vai te atacar com ' + randomEnemy.weapon + '!')
   
main()