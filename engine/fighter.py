import random
class Fighter:
    def __init__(self, name, power, accuracy, stamina):
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.stamina = stamina
        self.health = 100

        # fight stats

        self.landed = 0
        self.missed = 0
        self.total_damage = 0

        # per round stats

        self.round_landed = 0
        self.round_missed = 0
        self.round_total_damage = 0
        

   

    def take_damage(self, dmg):
        self.health = max(0, self.health - dmg)
    
    def use_stamina(self, num):
        self.stamina = max(0, self.stamina - num)
    
    def recover_stamina(self):
        self.stamina = max(0, self.stamina + 10) 

    def get_stamina(self):
        return self.stamina
    
    def get_health(self):
        return self.health

    def is_knocked_out(self):
        if self.health <= 0:
            print(f"{self.name} has been knocked out!")
            return True
        return False
    
    def fight_summary(self):
        total_strikes = self.landed + self.missed
        accuracy = (self.landed/ total_strikes * 100) if total_strikes else 0
        print(f"\n> {self.name}")
        print(f"Total landed: {self.landed}")
        print(f"Total missed: {self.missed}")
        print(f"Accuracy: {accuracy:.1f}%")
        print(f"Total Damage Inflicted: {self.total_damage:.1f}")



