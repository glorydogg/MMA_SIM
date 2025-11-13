from fighter import Fighter
import random
import time

class FightManager:
    def __init__(self, fighter1, fighter2):
        self.f1 = fighter1
        self.f2 = fighter2

    def punch(self, attacker, defender):
        base_damage = random.randint(1, 5) 
        fighter_dmg = base_damage * (attacker.power/100)
    
        
        if random.randint(1, 100) <= attacker.accuracy:
            defender.health -= fighter_dmg
            attacker.use_stamina(5)
            print(f"{attacker.name} lands a jab on {defender.name}!\n")
            attacker.landed += 1
            attacker.round_landed += 1
            attacker.total_damage += fighter_dmg
            attacker.round_total_damage += fighter_dmg
        else:
            attacker.use_stamina(10)
            print(f"{attacker.name} misses the jab!\n")
            attacker.missed += 1 
            attacker.round_missed += 1
        
    def kick(self, attacker, defender):
        base_dmg = random.randint(5, 15)
        fighter_dmg = base_dmg * (attacker.power/100)

        # hit chance
        if random.randint(1, 100) <= attacker.accuracy - 15: 

            descriptions = [
                f"{attacker.name} lands a strong head kick on {defender.name}!\n",
                f"{attacker.name} with a nice calf kick on {defender.name}!\n",
                f"{attacker.name} with the kick to the body on {defender.name}!\n"
            ]
            print(random.choice(descriptions))
            defender.health -= fighter_dmg
            attacker.use_stamina(10)
            attacker.landed += 1
            attacker.round_landed += 1
            attacker.total_damage += fighter_dmg
            attacker.round_total_damage += fighter_dmg
        else:
            print(f"{attacker.name} attempts a kick but misses!\n")
            attacker.missed += 1
            attacker.round_missed += 1
        
    def elbow(self, attacker, defender):
        base_dmg = random.randint(20, 30)
        fighter_dmg = base_dmg * (attacker.power/100)

        # hit chance
        if random.randint(1, 100) <= attacker.accuracy - 25:  
            defender.health -= fighter_dmg
            attacker.use_stamina(5)
            print(f"{attacker.name} with the vicious elbow on {defender.name}!!\n")
            attacker.landed += 1
            attacker.round_landed += 1
            attacker.total_damage += fighter_dmg
            attacker.round_total_damage += fighter_dmg
        else:
            attacker.use_stamina(10)
            print(f"{attacker.name} misses an elbow on {defender.name}!\n")
            attacker.missed += 1
            attacker.round_missed += 1



    def fight(self):
        print(f"Fight has started between {self.f1.name} and {self.f2.name}!\n")
        total_rounds = 3
        round_turns = 12
           
        for round_num in range(1, total_rounds + 1):
            print(f"--- Round {round_num} ---")
            self.f1.round_landed = self.f1.round_missed = 0
            self.f2.round_landed = self.f2.round_missed = 0

            for turn in range(1, round_turns + 1):
                attacker, defender = (self.f1, self.f2) if turn % 2 == 1 else (self.f2, self.f1)
                move = random.choices(["punch", "kick", "elbow"], weights = [5,3,1])[0]
                getattr(self, move)(attacker, defender)

                if self.f1.is_knocked_out() or self.f2.is_knocked_out():
                    return
                    
            
            print(f"End of round {round_num}!\n")
            # end of round fighter 1 stats
            print(f"Round {round_num} Stats for {self.f1.name}: \nHits landed: {self.f1.round_landed} ")
            print(f"Hits missed: {self.f1.round_missed}\nTotal Damage: {self.f1.round_total_damage:.1f}\n")
            #end of round fighter 2 stats
            print(f"Round {round_num} Stats for {self.f2.name}: \nHits landed: {self.f2.round_landed} ")
            print(f"Hits missed: {self.f2.round_missed}\nRound Damage: {self.f2.round_total_damage:.1f}")
            
            self.f1.recover_stamina()
            self.f2.recover_stamina()
           

        if self.f1.health >= self.f2.health:
            print(f"{self.f1.name} is the winner by judges decision!")
        else:
            print(f"{self.f2.name} is the winner by judges decision!")

        print("\n--- FINAL FIGHT SUMMARY ---")
        self.f1.fight_summary()
        self.f2.fight_summary()





if __name__ == "__main__":
    fighter1 = Fighter("McGregor", power=80, accuracy=90, stamina=100)
    fighter2 = Fighter("Khabib", power=85, accuracy=85, stamina=100)

    engine = FightManager(fighter1, fighter2)
    engine.fight()