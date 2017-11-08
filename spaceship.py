PLANET='Earth'
NAME=''
WEIGHT=''

def startup():
    global NAME
    print("Hello! Welcome to the Spaceship Game, the point of this game is to make off these planets without gettings blown up, Good Luck!!")
    NAME=input('What is your name? ')
    menu()

def menu():
    global NAME
    global PLANET
    print('Welcome!! ' ,NAME)
    print('1. Start Game\n2. Load Planet')
    choice=input('Choose by number 1 or 2:').lower()
    if choice=='1':
        weight=input('What is your ship weight? ')
        location()
        take_off()
    elif choice=='2':
        print('loading..')
        menu()
    else:
        print('INVALID ENTRY')
        menu()
def take_off():
    global PLANET
    dest = input('What planet do you want to go to? ').lower()
    if dest=='earth':
        print("You are already on Earth, try a different planet")
        dest = input('What planet do you want to go to? ')
        spd=float(input('What speed do you want to go? (in km/s) '))

def check(esc,spd,dest):
    global PLANET
    if spd < esc:
        print('NOT FAST ENOUGH!!! BOOOOM!')
        start_menu()
    elif spd <= (esc * 1.1):
        print('YAY! You made it to %s' % dest)
        PLANET = dest
        location()
    elif spd > (esc * 1.1):
        print('BOOM! YOU BURNED UP GOING TOO FAST!')
        start_menu()
    else:
        print('Uh-oh...')
        take_off()

def location():
    global PLANET
    print('''You are currently on the planet %s''' %PLANET.title())
    take_off()

startup()
def location():
    global PLANET
    print("You are currently on the planet" +PLANET)
    score=''
    print("YOU GOT A SCORE OF",score)

    print("Game Over")
    print("1. Try again\n2. Quit Game")
    if choice=='1':
        print("loading")
    elif choice=='2':
        print('loading..')
        quit()
