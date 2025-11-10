from fighter import Fighter
import random
import time

class FightManager:
    def __init__(self, fighter1, fighter2):
        self.f1 = fighter1
        self.f2 = fighter2

    def punch(self, attacker, defender):
        base_damage = random.randint(5, 10) 
        fighter_dmg = base_damage * (attacker.power/100)
    
        
        if random.randint(1, 100) <= attacker.accuracy:
            defender.health -= fighter_dmg
            attacker.use_stamina(5)
            print(f"{attacker.name} lands a jab on {defender.name}!")
        else:
            attacker.use_stamina(10)
            print(f"{attacker.name} misses the jab!")
        
    def kick(self, attacker, defender):
        base_dmg = random.randint(10, 20)
        fighter_dmg = base_dmg * (attacker.power/100)

        # hit chance
        if random.randint(1, 100) <= attacker.accuracy - 15: 

            descriptions = [
                f"{attacker.name} lands a strong head kick on {defender.name}!",
                f"{attacker.name} with a nice calf kick on {defender.name}!",
                f"{attacker.name} with the kick to the body on {defender.name}!"
            ]
            print(random.choice(descriptions))
            defender.health -= fighter_dmg
            attacker.use_stamina(10)
        else:
            print(f"{attacker.name} attempts a kick but misses!")
        
    def elbow(self, attacker, defender):
        base_dmg = random.randint(25, 35)
        fighter_dmg = base_dmg * (attacker.power/100)

        # hit chance
        if random.randint(1, 100) <= attacker.accuracy - 25:  
            defender.health -= fighter_dmg
            attacker.use_stamina(5)
            print(f"{attacker.name} with the vicious elbow on {defender.name}!!!")
        else:
            attacker.use_stamina(10)
            print(f"{attacker.name} misses an elbow on {defender.name}!")
            




    def fight(self):
        print(f"Fight has started between {self.f1.name} and {self.f2.name}!\n")
        total_rounds = 3
        round_turns = 10
           
        for round_num in range(1, total_rounds + 1):
            print(f"\n--- Round {round_num} ---")
            for turn in range(1, round_turns + 1):
                attacker, defender = (self.f1, self.f2) if turn % 2 == 1 else (self.f2, self.f1)
                move = random.choice(["punch", "kick", "elbow"])
                getattr(self, move)(attacker, defender)

                if self.f1.is_knocked_out() or self.f2.is_knocked_out():
                    return
                    
            
            print(f"End of round {round_num}!")
            self.f1.recover_stamina()
            self.f2.recover_stamina()
           

        if self.f1.health >= self.f2.health:
            print(f"{self.f1.name} is the winner by judges decision!")
        else:
            print(f"{self.f2.name} is the winner by judges decision!")




if __name__ == "__main__":
    fighter1 = Fighter("McGregor", power=80, accuracy=90, stamina=100)
    fighter2 = Fighter("Khabib", power=85, accuracy=85, stamina=100)

    engine = FightManager(fighter1, fighter2)
    engine.fight()