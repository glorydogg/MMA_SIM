import random
class Fighter:
    def __init__(self, name, power, accuracy, stamina, grappling, takedown_defense):
        self.name = name
        self.power = power
        self.accuracy = accuracy
      
        self.grappling = grappling # just for testing
        self.takedown_defense = takedown_defense
        self.submission_defense = random.randint(50, 95)
        self.stamina = stamina
        self.health = 100

        # fighting phase
        self.phase = "standup"

        # fight stats

        self.landed = 0
        self.missed = 0
        self.total_damage = 0
        self.takedowns_landed = 0
        self.takedown_attempts = 0
        # per round stats

        self.round_landed = 0
        self.round_missed = 0
        self.round_total_damage = 0
        self.round_takedown_landed = 0
        self.round_takedown_attempts = 0
        

   

    def take_damage(self, dmg):
        self.health = max(0, self.health - dmg)
    
    def use_stamina(self, cost):
        decay = cost * (1.2 if self.stamina < 40 else 1.0)
        self.stamina = max(0, self.stamina - decay)
    
    def recover_stamina(self):
        regen = 30 if self.stamina < 60 else 15
        self.stamina = max(0, self.stamina + regen) 

    @property
    def effective_power(self):
        return self.power * (self.stamina / 100) 
    
    @property
    def effective_accuracy(self):
        return self.accuracy * (0.8 + self.stamina / 125) 

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
        print(f"Total take downs landed vs attempted: {self.takedowns_landed} - {self.takedown_attempts}")



