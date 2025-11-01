from engine.fighter import Fighter
import random
import time

class FightManager:
    def __init__(self, fighter1, fighter2):
        self.f1 = fighter1
        self.f2 = fighter2


    def fight(self):
        print(f"Fight has started between {self.f1.name} and {self.f2.name}!\n")
        round_num = 1

        while not self.f1.is_knocked_out() and not self.f2.is_knocked_out():
            print(f"---- Round {round_num} ----")
            attacker, defender = random.choice([(self.f1, self.f2), (self.f2, self.f1)])
            damage = random.randint(8, 15) * (attacker.power/100)
            attacker.use_stamina()
            defender.take_damage(damage)

            print(f"{attacker.name} hits {defender.name} for {damage} damage.")
            print(f"{defender.name} health: {defender.get_health()}")
            
            time.sleep(1)

            round_num += 1

            print("\n Fight Over !")
            if self.f1.is_knocked_out():
                print(f"{self.f2} Wins !")
            print (f"{self.f1} wins!")

if __name__ == "__main__":
    fighter1 = Fighter("McGregor", power=80, accuracy=90, stamina=100)
    fighter2 = Fighter("Khabib", power=85, accuracy=85, stamina=100)

    engine = FightManager(fighter1, fighter2)
    engine.fight()