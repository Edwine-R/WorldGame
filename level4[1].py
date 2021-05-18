import time

points_a = 0
points_b = 0
points_c = 0
points_d = 0


def add_points_d():
    global points_d
    if points_d >=10:
        print(f"Congratulations you have {points_d} ponits.")
        print(f"And have completed all levels")
    else:
        print(f"You only have {points_d} points")
        print("Please try again")
        time.sleep(1.5)
        start_level_2()



def question_10d():
    global points_d
    time.sleep(1)
    print("What is the currency of Ukraine")
    answer_10d = input("A:Hryvina, B: Forint C: Lev")
    if answer_10d == "A" or answer_10d == "a"or answer_10d == "Hryvina" or answer_10d == "hryvina":
        print("Correct!")
        points_d = points_d + 10
        add_points_d()
    else:
        add_points_d()


def failure_9d():
    print("INCORRECT")
    question_10d()
        
def question_9d():
    global points_d
    time.sleep(1)
    print("What is the currency of Romania?")
    time.sleep(1)
    answer_9d = input(" A:Lempira, B: Kwacha, C:Leu")
    if answer_9d == "c" or answer_9d == "C" or answer_9d == "Leu" or answer_9d == "Leu":
        print("Correct!")
        points_d = points_d + 10
        print(f"You have now {points_d} points.")
        question_10d()
    else:
        failure_9d()


def failure_8d():
    print("INCORRECT")
    question_9d()
def question_8d():
    global points_d
    time.sleep(1)
    print("What is the currency of Russia?")
    answer_8d = input(" A: Ruble, B: Dinar, C:Kwacha")
    if answer_8d =="A" or answer_8d == "a" or answer_8d =="Ruble" or answer_8d == "ruble" :
        print("Correct!")
        points_d = points_d + 10
        print(f"You have now {points_d} points.")
        time.sleep(1)
        question_9d()
    else:
        failure_8d()



def failure_7d():
    print("INCORRECT")
    question_8d()
        
def question_7d():
    global points_d
    time.sleep(1)
    print("What is the currency of Nigeria?")
    answer_7d = input("A:Rupiah, B:Naira, C:Gourde")
    if answer_7d =="B" or answer_7d == "b" or answer_7d =="Naira" or answer_7d == "naira":
        print("Correct!")
        points_d = points_d + 10
        print(f"You have now {points_d} points.")
        time.sleep(1)
        question_8d()
    else:
        failure_7d()


def failure_6d():
    print("INCORRECT")
    question_7d()
def question_6d():
    global points_d
    time.sleep(1)
    print("what is the currency of Germany?")
    answer_6d = input("A: Euro, B:Peso, C:Pula")
    if answer_6d == "A" or answer_6d =="a" or answer_6d == "Euro" or answer_6d == "euro":
        print("Correct!")
        points_d = points_d + 10
        print(f"You have now {points_d} points.")
        time.sleep(1)
        question_7d()
    else:
        failure_6d()



def failure_5d():
    print("INCORRECT")
    question_6d()
def question_5d():
    global points_d
    time.sleep(1)
    print("What is the currency of Ghana?")
    answer_5d = input("A: Cedis, B:Riel, C: Korona")
    if answer_5d == "A" or answer_5d == "a" or answer_5d == "Cedis" or answer_5d == "cedis":
        print("Correct!")
        points_d = points_d + 10
        print(f"You have now {points_d} points.")
        time.sleep(1)
        question_6d()
    else:
        failure_5d()


def failure_4d():
    print("INCORRECT")
    question_5d()
def question_4d():
    global points_d
    time.sleep(1)
    print("What is the currency of France?")
    time.sleep(1)
    answer_4d = input("A: Franc, B: Forint, C: Euro")
    if answer_4d =="C" or answer_4d =="c" or answer_4d == "Euro" or answer_4d == "euro":
        print("Correct!")
        points_d = points_d + 10
        print(f"You have now {points_d} points.")
        time.sleep(1)
        question_5d()
    else:
        failure_4d()



def failure_3d():
    print("INCORRECT")
    question_4d()  

def question_3d():
    global points_d
    time.sleep(1)
    print("What is the currency of England?")
    time.sleep(1)
    answer_3d = input("A: Lari, B: Euro, C:Pound")
    if answer_3d == "c" or answer_3d == "C" or answer_3d =="Pound" or answer_3d =="pound":
        print("Correct!")
        points_d = points_d + 10
        print(f"You have now {points_d} points.")
        time.sleep(1)
        question_4d()
    else:
        failure_3d()


def faliure_2d():
    print("Incorrect!")
    question_3d()

def question_2d():
    global points_d
    time.sleep(1)
    print("What is the currency of Australia?")
    time.sleep(1)
    answer_2d = input("A:Escudo, B: Dollar, C:Dalasi")
    if answer_2d == "B" or answer_2d == "b" or answer_2d == "Dollar" or answer_2d == "dollar":
        print("Correct!")
        points_d = points_d + 10
        print(f"You have now {points_d} points.")
        time.sleep(1)
        question_3d()
    else:
        faliure_2d()



def faliure_1d():
    print("Incorrect")
    question_2d()

def question_1d():
    global points_d
    time.sleep(2)
    print("Let's begin")
    time.sleep(2)
    print("What is the currency of Angola?")
    time.sleep(2)
    answer_1d = input("A:Kwanza, B:Dram, C:Florin")
    if answer_1d =="A" or answer_1d =="a" or answer_1d =="Kwanza" or answer_1d =="kwanza":
        print("correct!")
        time.sleep(1)
        points_d = points_d + 10
        print(f"You have now {points_d} points.")
        question_2d()
    else:
        faliure_1d()
        


def start_level_4():
    print("Welcome to Level 4. Would you like to continue playing")
    start = input("Yes or no? ")
    if start == "Yes" or start == "yes" :
        time.sleep(1.5)    
        print("Great")
        question_1d()
    else:
        print("Goodbye")



def add_points_c():
    global points_c
    if points_c >=70:
        print(f"Congratulations you have {points_c} ponits and can now enter level 2")
        start_level_4()
    else:
        print(f"You only have {points_c} points")
        print("Please try again")
        time.sleep(1.5)
        start_level_3()





def failure_10c():
    print("INCORRECT")
    add_points_c()
def question_10c():  
    global points_c
    print("What is the highest mountain in the world?")
    time.sleep(1.5)
    answer_10c = input("A: Kilimanjaro - B: Everest - C: K2 : ")
    if answer_10c == "B" or answer_10c == "b" or answer_10c == "Everest" or answer_10c == "everest":
        print("Correct!")
        points_c = points_c + 10
        print(f"You have now {points_c} points!")
        time.sleep(1)
        print ("WELL DONE!")
        time.sleep(1)
        add_points_c()
    else:
        failure_10c()



def failure_9c():
    print("INCORRECT")
    question_10c()
def question_9c():
    global points_c
    print("Which is the largest country in the world?")
    time.sleep(2)
    answer_9c = input("A: China - B: Japan - C: Russia: ")
    if answer_9c == "C" or answer_9c == "c" or answer_9c == "Russia" or answer_9c == "russia":
        print("Correct!")
        points_c = points_c + 10
        print(f"You have now {points_c} points!")
        time.sleep(1)
        question_10c()
    else:
        failure_9c()


def failure_8c():
    print("INCORRECT")
    question_9c()
def question_8c(): 
    global points_c
    print("Where is River Nile located?")
    time.sleep(2)
    answer_8c = input("A: Irak - B: Mississipi - C: Egypt: ")
    if answer_8c == "C" or answer_8c == "c" or answer_8c == "Egypt" or answer_8c == "egypt":
        print("Correct!")
        points_c = points_c + 10
        print(f"You have now {points_c} points!")
        time.sleep(1)
        question_9c()
    else:
        failure_8c()


def failure_7c():
    print("INCORRECT")
    question_8c()
def question_7c(): 
    global points_c
    print("What is Earth's largest continent?")
    time.sleep(2)
    answer_7c = input("A: Europe - B: Africa - C: Asia: ")
    if answer_7c == "C" or answer_7c == "c" or answer_7c == "Asia" or answer_7c == "asia":
        print("Correct!")
        points_c = points_c + 10
        print(f"You have now {points_c} points!")
        time.sleep(1)
        question_8c()
    else:
        failure_7c()


def failure_6c():
    print("INCORRECT")
    question_7c()
def question_6c():
    global points_c
    print("In which country would you be if you were Visiting the Taj Mahal?")
    time.sleep(2)
    answer_6c = input("A: India - B: Dubai - C: Mongolia:")
    if answer_6c == "A" or answer_6c == "a" or answer_6c == "India" or answer_6c == "india":
        print("Correct!")
        points_c = points_c + 10
        print(f"You have now {points_c} points!")
        time.sleep(1)
        question_7c()
    else:
        failure_6c()


def failure_5c():
    print("INCORRECT")
    question_6c()
def question_5c():
    global points_c
    print("What does each star on the flag of the United States stand for?")
    time.sleep(2)
    answer_5c = input("A: States - B: Presidents - C: Cities: ")
    if answer_5c == "A" or answer_5c == "a" or answer_5c == "States" or answer_5c == "states":
        print("Correct!")
        points_c = points_c + 10
        print(f"You have now {points_c} points!")
        time.sleep(1)
        question_6c()
    else:
        failure_5c()


def failure_4c():
    print("INCORRECT")
    question_5c()
def question_4c():
    global points_c
    print("What continent is Russia Part of?")
    time.sleep(2)
    answer_4c = input("A: Asia - B: Europe - C: Both: ")
    if answer_4c == "C" or answer_4c == "c" or answer_4c == "Both" or answer_4c == "both":
        print("Correct!")
        points_c = points_c + 10
        print(f"You have now {points_c} points!")
        time.sleep(1)
        question_5c()
    else:
        failure_4c()


def failure_3c():
    print("INCORRECT")
    question_4c()
def question_3c():  
    global points_c
    print("How many languages are spoken in Belgium?")
    time.sleep(2)
    answer_3c = input("A: 1 - B: 3 - C: 2: ")
    if answer_3c == "B" or answer_3c == "b" or answer_3c == "3" or answer_3c == "3":
        print("Correct!")
        points_c = points_c + 10
        print(f"You have now {points_c} points!")
        time.sleep(1)
        question_4c()
    else:
        failure_3c()


def failure_2c():
    print("INCORRECT")
    question_3c()
def question_2c():
    global points_c
    print("How many stars we find on America's flag?")
    time.sleep(2)
    answer_2c = input("A: 25 - B: 50 - C: 20: ")
    if answer_2c == "B" or answer_2c == "b" or answer_2c == "50" or answer_2c == "50":
        print("Correct!")
        points_c = points_c + 10
        print(f"You have now {points_c} points!")
        time.sleep(1)
        question_3c()
    else:
        failure_2c()


def failure_1c():
    print("INCORRECT")
    
    question_2c()

def question_1c():
    global points_c
    time.sleep(1.5)
    print("Let's begin")
    time.sleep(2)
    print("What continent is Congo part of?")
    time.sleep(2)
    answer_1c = input("A: Asia - B: South America - C: Africa: ")
    if answer_1c == "C" or answer_1c == "c" or answer_1c == "Africa" or answer_1c == "africa":
        print("Correct!")
        points_c = points_c + 10
        print(f"You have now {points_c} points!")
        time.sleep(1)
        question_2c()
    else:
        failure_1c()
        time.sleep(1)


def start_level_3():
    print("Welcome to Level 3. Would you like to continue playing?")
    start = input("Yes or No? ")
    if start == "Yes" or start == "yes":
        time.sleep(1)
        print("Great")
        question_1c()
    else:
        print("Goodbye")


def add_points_b():
    global points_b
    if points_b >=70:
        print(f"Congratulations you have {points_b} ponits and can now enter level 3")
        start_level_3()
    else:
        print(f"You only have {points_b} points")
        print("Please try again")
        time.sleep(1.5)
        start_level_2()






def failure_10b():
    print("INCORRECT")
    add_points_b()
def question_10b():
    global points_b
    print("What is the capital of France?")
    time.sleep(2)
    answer_10b = input("A: Lion - B: Paris - C: Dreux : ")
    if answer_10b == "B" or answer_10b == "b" or answer_10b == "Paris" or answer_10b == "paris":
        print("Correct")
        points_b = points_b + 10
        print(f"You have now {points_b} points!.")
        time.sleep(1)
        print ("WELL DONE!")
        time.sleep(1)
        add_points_b()
    else:
        failure_10b()


def failure_9b():
    print("INCORRECT")
    question_10b()
def question_9b():
    global points_b
    print("What is the capital of Russia?")
    time.sleep(2)
    answer_9b = input("A: Moscow - B: Ryazan - C: Omsk: ")
    if answer_9b == "A" or answer_9b == "a" or answer_9b == "Moscow" or answer_9b == "moscow":
        print("Correct!")
        points_b = points_b + 10
        print(f"You have now {points_b} points!")
        time.sleep(1)
        question_10b()
    else:
        failure_9b()


def failure_8b():
    print("INCORRECT")
    question_9b()
def question_8b():   
    global points_b
    print("What is the capital of England?")
    time.sleep(2)
    answer_8b = input("A: Liverpool - B: Manchester - C: London: ")
    if answer_8b == "C" or answer_8b == "c" or answer_8b == "London" or answer_8b == "london":
        print("Correct!")
        points_b = points_b + 10
        print(f"You have now {points_b} points!")
        time.sleep(1)
        question_9b()
    else:
        failure_8b()


def failure_7b():
    print("INCORRECT")
    question_8b()
def question_7b(): 
    global points_b
    print("What is the capital of Nigeria?")
    time.sleep(2)
    answer_7b = input("A: Abuja - B: Lagos - C: Karu: ")
    if answer_7b == "A" or answer_7b == "a" or answer_7b == "Abuja" or answer_7b == "abuja":
        print("Correct!")
        points_b = points_b + 10
        print(f"You have now {points_b} points!")
        time.sleep(1)
        question_8b()
    else:
        failure_7b()


def failure_6b():
    print("INCORRECT")
    question_7b()
def question_6b():
    global points_b
    print("What is the capital of Romenia?")
    time.sleep(2)
    answer_6b = input("A: Brasov - B: Sibiu - C: Bucharest: ")
    if answer_6b == "C" or answer_6b == "c" or answer_6b == "Bucharest" or answer_6b == "bucharest":
        print("Correct!")
        points_b = points_b + 10
        print(f"You have now {points_b} points!")
        time.sleep(1)
        question_7b()
    else:
        failure_6b()


def failure_5b():
    print("INCORRECT")
    question_6b()
def question_5b():
    global points_b
    print("What is the capital of Australia?")
    time.sleep(2)
    answer_5b = input("A: Sydney - B: Camberra - C: Braddon: ")
    if answer_5b == "B" or answer_5b == "b" or answer_5b == "Camberra" or answer_5b == "camberra":
        print("Correct!")
        points_b = points_b + 10
        print(f"You have now {points_b} points!")
        time.sleep(1)
        question_6b()
    else:
        failure_5b()


def failure_4b():
    print("INCORRECT")
    question_5b()
def question_4b():
    global points_b
    print("What is the capital of Germany?")
    time.sleep(2)
    answer_4b = input("A: Bonn - B: Brandenburg - C: Berlin: ")
    if answer_4b == "C" or answer_4b == "c" or answer_4b == "Berlin" or answer_4b == "berlin":
        print("Correct!")
        points_b = points_b + 10
        print(f"You have now {points_b} points!")
        time.sleep(1)
        question_5b()
    else:
        failure_4b()


def failure_3b():
    print("INCORRECT")
    question_4b()
def question_3b(): 
    global points_b  
    print("What is the capital of Angola?")
    time.sleep(2)
    answer_3b = input("A: Huila - B: Luanda - C: Huambo: ")
    if answer_3b == "B" or answer_3b == "b" or answer_3b == "Luanda" or answer_3b == "luanda":
        print("Correct!")
        points_b = points_b + 10
        print(f"You have now {points_b} points!")
        time.sleep(1)
        question_4b()
    else:
        failure_3b()


def failure_2b():
    print("INCORRECT")
    question_3b()

def question_2b():
    global points_b
    print("What is the capital of Italy?")
    time.sleep(2)
    answer_2b = input("A: Rome - B: Milan - C: Venice: ")
    if answer_2b == "A" or answer_2b == "a" or answer_2b == "Rome" or answer_2b == "rome":
        print("Correct!")
        points_b = points_b + 10
        print(f"You have now {points_b} points!")
        time.sleep(1)
        question_3b()
    else:
        question_3b()

def failure_1b():
    print("INCORRECT")
    question_2b()
def question_1b():
    global points_b
    time.sleep(1)
    print("Let's begin")
    time.sleep(2)
    print("What is the capital of Portugal?")
    time.sleep(2)
    answer_1b = input("A: Porto - B: Faro - C: Lisbon: ")
    if answer_1b == "C" or answer_1b == "c" or answer_1b == "Lisbon" or answer_1b == "lisbon":
        print("Correct!")
        points_b = points_b + 10
        print(f"You have now {points_b} points!")
        time.sleep(1)
        question_2b()
    else:
        failure_1b()
        time.sleep(1)


def start_level_2():
    print("Welcome to Level 2. Would you like to continue playing?")
    start = input("Yes or no? ")
    if start == "Yes" or start == "yes":
        time.sleep(1)
        print("Great")
        question_1b()
    else:
        print("Goodbye")


def add_points_a():
    global points_a
    if points_a >=70:
        print(f"Congratulations you have {points_a} ponits and can now enter level 2")
        start_level_2()
    else:
        print(f"You only have {points_a} points")
        print("Please try again")
        time.sleep(1.5)
        start_game()


def failure_10a():
    add_points_a()
    
def question_10a():
    global points_a
    print("What is Nigeria official language? ")
    time.sleep(1)
    print("A:Hausa - B:English - C:Yoruba ")
    time.sleep(1)
    answer_10a = input("A, B or C? ")
    if answer_10a == "B" or answer_10a == "b":
        print("Correct")
        points_a = points_a + 10
        print(f"You have now {points_a} points!")
        add_points_a()
    else:
        failure_10a()
        time.sleep(1)



def failure_9a():
    print("INCORRECT")
    question_10a()
def question_9a():
    global points_a
    print("What is Cambodia official Language?")
    time.sleep(1)
    print("A:Cham - B:Thai - C:Khmer ")
    time.sleep(1)
    answer_9a = input("A, B or C? ")
    if answer_9a == "C" or answer_9a == "c":
        print("Correct")
        points_a = points_a + 10
        print(f"You have now {points_a} points!")
        question_10a()
    else:
        failure_9a()


def failure_8a():
    print("INCORRECT")
    question_9a()
def question_8a():
    global points_a
    print("What is the official language of Vatican city?")
    time.sleep(1)
    print("A:Italian - B:Latin - C:German ")
    time.sleep(1)
    answer_8a = input("A, B or C? ")
    if answer_8a == "A" or answer_8a == "a":
        print("Correct")
        points_a = points_a + 10
        print(f"You have now {points_a} points!")
        question_9a()
    else:
        failure_8a()

def failure_7a():
    print("INCORRECT")
    question_8a()
def question_7a():
    global points_a
    print("Other than English what language do they speak in Canada?")
    time.sleep(1)
    print("A:French - B:Spainish - C:German ")
    time.sleep(1)
    answer_7a = input(" A, B or C? ")
    if answer_7a == "A" or answer_7a == "a":
        print("Correct")
        points_a = points_a + 10
        print(f"You have now {points_a} points!")
        question_8a()
    else:
        failure_7a()

def failure_6a():
    print("INCORRECT")
    question_7a()
def question_6a():
    global points_a
    print("Other than English what language do they speak in New Zealand?")
    time.sleep(1)
    print("A:Kiwi - B: Mandarin - C:Māori ")
    time.sleep(1)
    answer_6a = input("A, B or C? ")
    if answer_6a == "C" or answer_6a == "c":
        print("Correct")
        points_a = points_a + 10
        print(f"You have now {points_a} points!")
        question_7a()
    else:
        failure_6a()

def failure_5a():
    print("INCORRECT")
    question_6a()
def question_5a():
    global points_a
    print("What is the most spoken language in India?")
    time.sleep(1)
    print("A: Hindi - B: Bengali - C: Mandarin ")
    time.sleep(1)
    answer_5a = input("A, B or C? ")
    if answer_5a == "A" or answer_5a == "a":
        print("Correct")
        points_a = points_a + 10
        print(f"You have now {points_a} points!")
        question_6a()
    else:
        failure_5a()

def failure_4a():
    print("INCORRECT")
    question_5a()
def question_4a():
    global points_a
    print("What is the most spoken language in Brazil?")
    time.sleep(1)
    print("A: Portuguese - B: English - C: Spanish ")
    time.sleep(1)
    answer_4a = input(" A, B or C? ")
    if answer_4a == "A" or answer_4a == "a":
        print("Correct")
        points_a = points_a + 10
        print(f"You have now {points_a} points!")
        question_5a()
    else:
        failure_4a()


def failure_3a():
    print("INCORRECT")
    question_4a()
def question_3a():
    global points_a
    print("What is the mostly spoken language in China?")
    time.sleep(1.5)
    print("A: Taiwan - B: Manarin - C: Cantonese ")
    time.sleep(1.5)
    answer_3a = input("A, B or C? ")
    if answer_3a == "B" or answer_3a == "b":
        print("Correct")
        points_a = points_a + 10
        print(f"You have now {points_a} points!")
        question_4a()
        
    else:
        failure_3a()


def failure_2a():
    print("INCORRECT")
    question_3a()

def question_2a():
    global points_a
    print("What language do they speak in France?")
    time.sleep(1.5)
    print("A: English - B: German - C: French ")
    time.sleep(1.5)
    answer_2a = input("A, B or C? ")
    if answer_2a == "C" or answer_2a == "c":
        print("Correct")
        points_a = points_a + 10
        print(f"You have now {points_a} points!")
        question_3a()
    else:
        failure_2a()



def failure_1a():
    print("INCORRECT")
    question_2a()

def question_1a():
    global points_a
    time.sleep(3)
    print("Let's begin")
    time.sleep(2)
    print("What language do they speak in Wales?")
    time.sleep(2)
    print("A: Welsh - B: English - C: Gaelic? ")
    time.sleep(1)
    answer_1a = input("A, B or C? ")
    if answer_1a == "A" or answer_1a == "a" :
        print("Correct!")
        time.sleep(1)
        points_a = points_a + 10
        print(f"You have now {points_a} points!")
        question_2a()
    else:
        failure_1a()
        time.sleep(1)

def begin():
    name = input("What is your name?")
    print(f"Welcome {name}")
    time.sleep(1)
    print("There is 4 levels in this game to get to the next level you have to score 70 point or more.")
    time.sleep(3)
    print("Each question is worth 10 points.")
    question_1a()

def start_game ():
    print("Would you like to play?")
    start = input("Yes or no?")
    if start == "Yes" or start =="yes":
        print("Great")
        begin()
    else:
        print("Goodbye until next time")
start_game()
