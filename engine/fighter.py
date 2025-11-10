import random
class Fighter:
    def __init__(self, name, power, accuracy, stamina):
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.stamina = stamina
        self.health = 100

   

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



