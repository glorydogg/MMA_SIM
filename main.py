import os
from engine.fighter import Fighter
from engine.fight_engine import FightManager
from simulator.simulation import Simulator

def get_valid_int_input(prompt="Enter a number: "):
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please try again.")
    

def fighter_list():

    FIGHTERS_ELITE = [
    Fighter("Jon Jones", 92, 88, 95, 96, 95, 90),
    Fighter("Kamaru Usman", 88, 85, 97, 95, 90, 88),
    Fighter("Israel Adesanya", 90, 95, 92, 80, 85, 82),
    Fighter("Alexander Volkanovski", 86, 92, 98, 87, 92, 88),
    Fighter("Charles Oliveira", 88, 86, 90, 94, 82, 98),
    Fighter("Islam Makhachev", 85, 86, 95, 99, 92, 95)
]
    FIGHTERS_MID = [
    Fighter("Dustin Poirier", 90, 88, 88, 80, 78, 75),
    Fighter("Justin Gaethje", 92, 82, 90, 75, 80, 70),
    Fighter("Leon Edwards", 87, 90, 93, 82, 88, 85),
    Fighter("Max Holloway", 80, 92, 97, 78, 80, 82),
    Fighter("Robert Whittaker", 88, 89, 90, 85, 86, 85),
    Fighter("Petr Yan", 88, 90, 92, 83, 84, 80)
]
    FIGHTERS_BRAWLERS = [
    Fighter("Francis Ngannou", 100, 70, 85, 70, 75, 65),
    Fighter("Derrick Lewis", 98, 68, 78, 68, 70, 65),
    Fighter("Tai Tuivasa", 92, 75, 82, 70, 72, 70),
    Fighter("Paulo Costa", 95, 78, 88, 75, 80, 75),
    Fighter("Yoel Romero", 93, 80, 96, 90, 88, 80),
    Fighter("Conor McGregor Prime", 96, 96, 88, 80, 70, 75)
]
    FIGHTERS_GRAPPLERS = [
    Fighter("Khabib Nurmagomedov", 86, 84, 95, 99, 98, 90),
    Fighter("Ben Askren Prime", 72, 70, 92, 98, 88, 85),
    Fighter("Demian Maia", 70, 78, 88, 95, 80, 99),
    Fighter("Curtis Blaydes", 85, 82, 90, 94, 88, 84),
    Fighter("GSP Prime", 88, 90, 95, 98, 97, 90),
    Fighter("Henry Cejudo", 86, 90, 92, 97, 95, 88)
]
    ALL_FIGHTERS = {
    "Elite": FIGHTERS_ELITE,
    "Mid": FIGHTERS_MID,
    "Brawlers": FIGHTERS_BRAWLERS,
    "Grapplers": FIGHTERS_GRAPPLERS
}

    return ALL_FIGHTERS



def main():
    #default fighters
    f1 = Fighter("McGregor", power=95, accuracy=95, stamina=100, grappling= 85, takedown_defense= 65, submission_defense= 85)
    f2 = Fighter("Khabib", power=85, accuracy=85, stamina=100, grappling= 99, takedown_defense= 95, submission_defense= 95)
    
    ALL_FIGHTERS = fighter_list()
    
    while True:
        os.system('cls')
        print("--- Welcome to MMA SIM! --")

        print("Please pick an option from the menu below.\n 1. Run a single fight\n " \
        "2. Run batch simulation\n 3. Change fighters\n 4. View Fighter stats\n 5. Quit\n")

        choice = get_valid_int_input("Enter an option: ")   

        if choice == 1:
            manager = FightManager(f1, f2) #run a single fight
            manager.fight()
            
            input("\nPress enter to continue")

        elif choice == 2:
            sim = Simulator(f1,f2)
            number_of_fights = get_valid_int_input("How many fights do you want to run: ")
            sim.run_batch(number_of_fights) # run batch sim
            sim.summary()

            input("\nPress enter to continue")

        elif choice == 3:   
            print("Which fighter do you want to replace?")
            print(f"Fighter 1: {f1.name}")
            print(f"Fighter 2: {f2.name}")

            # show categories
            fighter_replacement_choice = get_valid_int_input("Pick 1 or 2: ")
            for i, category in enumerate(ALL_FIGHTERS.keys(), start=1):
                print(i, category)
                
            selected_category = input("Now selected a category: ")


            print(f"Now pick a fighter from {selected_category}")
            for i, fighter in enumerate(ALL_FIGHTERS[selected_category], start=1):
                print(i, fighter.name)
                
            fighter_index = int(input("Pick a fighter number: "))
                    
            chosen_fighter = ALL_FIGHTERS[selected_category][fighter_index - 1]
           
                
            if fighter_replacement_choice == 1:
                f1 = chosen_fighter
            else:
                f2 = chosen_fighter
            input("\nPress enter to continue")

        elif choice == 4:
            print("\nFighter 1:")
            f1.summary()

            print("\nFighter 2:")
            f2.summary()
            input("\nPress enter to continue")
        else:
            quit()   

    
   

    
if __name__ ==  "__main__":
    main()