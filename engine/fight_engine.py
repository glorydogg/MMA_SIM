from engine.fighter import Fighter
from utils.logger import FightLogger
import random
import time

logger = FightLogger()



class FightManager:
    def __init__(self, fighter1, fighter2):
        self.f1 = fighter1
        self.f2 = fighter2
        self.phase = "standup"
        self.winner = None
        self.win_type = None
        self.current_round = 1
        self.fight_over = False
        
    def punch(self, attacker, defender):
        base_damage = random.randint(1, 5) 
        fighter_dmg = base_damage * (attacker.effective_power /100)
    
        
        if random.randint(1, 100) <= attacker.effective_accuracy:
            defender.health -= fighter_dmg
            attacker.use_stamina(3)
            print(f"{attacker.name} lands a jab on {defender.name}!\n")
            attacker.landed += 1
            attacker.round_landed += 1
            attacker.total_damage += fighter_dmg
            attacker.round_total_damage += fighter_dmg
        else:
            attacker.use_stamina(6)
            print(f"{attacker.name} misses the jab!\n")
            attacker.missed += 1 
            attacker.round_missed += 1
        
    def kick(self, attacker, defender):
        base_dmg = random.randint(5, 15)
        fighter_dmg = base_dmg * (attacker.effective_power / 100)

        # hit chance
        if random.randint(1, 100) <= attacker.effective_accuracy - 15: 

            descriptions = [
                f"{attacker.name} lands a strong head kick on {defender.name}!\n",
                f"{attacker.name} with a nice calf kick on {defender.name}!\n",
                f"{attacker.name} with the kick to the body on {defender.name}!\n"
            ]
            print(random.choice(descriptions))
            defender.health -= fighter_dmg
            attacker.use_stamina(5)
            attacker.landed += 1
            attacker.round_landed += 1
            attacker.total_damage += fighter_dmg
            attacker.round_total_damage += fighter_dmg
        else:
            print(f"{attacker.name} attempts a kick but misses!\n")
            attacker.use_stamina(8)
            attacker.missed += 1
            attacker.round_missed += 1
        
    def elbow(self, attacker, defender):
        base_dmg = random.randint(20, 30)
        fighter_dmg = base_dmg * (attacker.effective_power / 100)

        # hit chance
        if random.randint(1, 100) <= attacker.effective_accuracy - 25:  
            defender.health -= fighter_dmg
            attacker.use_stamina(4)
            print(f"{attacker.name} with the vicious elbow on {defender.name}!!\n")
            attacker.landed += 1
            attacker.round_landed += 1
            attacker.total_damage += fighter_dmg
            attacker.round_total_damage += fighter_dmg
        else:
            attacker.use_stamina(6)
            print(f"{attacker.name} misses an elbow on {defender.name}!\n")
            attacker.missed += 1
            attacker.round_missed += 1

    def takedown(self, attacker, defender):
        print(f"{attacker.name} attempts a double leg on {defender.name}!\n")
        
        # Calculate takedown success chance
        skill_diff = attacker.grappling - defender.takedown_defense
        base_chance = 50 + (skill_diff * 0.8)
        stamina_factor = 0.6 + (attacker.stamina / 200)
        adjusted_chance = base_chance * stamina_factor
        luck = random.randint(-10, 10)
        final_chance = max(5, min(95, adjusted_chance + luck))
        
        #outcome
        roll = random.randint(1, 100)
        if roll <= final_chance:
            print(f"{attacker.name} secures the takedown and moves to top control!\n")
            attacker.phase = "ground_top"
            defender.phase = "ground_bottom"
            self.phase = "ground"
            attacker.use_stamina(8)
            #defender.use_stamina(5)
            attacker.round_takedown_landed += 1
            attacker.round_takedown_attempts += 1
            attacker.takedowns_landed += 1
            attacker.takedown_attempts += 1
        else:
            print(f"{defender.name} sprawls and stuffs the takedown!\n")
            attacker.use_stamina(12)
            defender.use_stamina(5)
            attacker.round_takedown_attempts += 1
            attacker.takedown_attempts += 1

    def ground_control(self, attacker, defender):
        if attacker.phase == "ground_top":
            action = random.choices(
                ["ground_strike", "maintain_control","submission_attempt"], 
                weights= [6, 2, 2]

            )[0]
            getattr(self, action)(attacker, defender)
        else:
            action = random.choices(
                ["defend", "attempt_escape"], weights=[3, 7])[0]
            getattr(self, action)(attacker, defender)

    
    def ground_strike(self, attacker, defender):
        
        dmg = random.randint(2, 6) * (attacker.effective_power / 100)
        defender.take_damage(dmg)

        #stamina usage

        attacker.use_stamina(4)
        defender.use_stamina(6)    

        print(f"{attacker.name} lands another blow from top control on {defender.name}!\n")
    
    def defend(self, defender):
        print(f"{defender.name} defending strikes while on the bottom!\n")
        defender.use_stamina(2)


    def maintain_control(self, attacker, defender):
        print(f"{attacker.name} is gaining their stamina while tiring out {defender.name}!\n")
        attacker.stamina = min(100, attacker.stamina + 6)
        defender.use_stamina(4)
            
    def attempt_escape(self, attacker, defender):
        #escape chance ground game
        escape_chance = max(5, min(90, 25 + (defender.stamina - attacker.grappling) * 0.2))
        if random.randint(1, 100) <= escape_chance:
            print(f"{defender.name} scrambles and gets back to his feet!\n")
            self.phase = "standup"
            defender.phase = "standup"
            attacker.phase = "standup"

        else:
            print(random.choice([
                f"{attacker.name} continues to land blows from top control.\n",
                f"{attacker.name} maintains heavy pressure from the top.\n",
                f"{defender.name} unable to shake of {attacker.name}!\n"
                ]))
        
    def submission_attempt(self, attacker, defender):
        print(f"{attacker.name} attempts a rear naked choke!\n")
        chance = 20 + (attacker.grappling - defender.submission_defense) * 0.3
        chance = max(5, min(80, chance))
        if random.randint(1, 100) <= chance:
            print(f"{defender.name} taps out! {attacker.name} wins via submission!\n")
            defender.health = 0 
            self.phase = "standup"
            self.win_type = "Submission"
            self.winner = attacker.name

            self.fight_over = True
            self.end_fight()
            return
        else:
            print(f"{defender.name} survives the choke attempt!\n")
            attacker.use_stamina(10)

    def end_fight(self):
        print("\n--- FINAL FIGHT SUMMARY ---")
        self.f1.fight_summary()
        self.f2.fight_summary()
        
        # after fight ends
        self.fight_over = True

        fight_data = {
            "fighter1": self.f1.name,
            "fighter2": self.f2.name,
            "winner": self.winner,
            "method": self.win_type,
            "round": self.current_round
        }
        
        logger.log_fight(fight_data)


    def fight(self):
        print(f"Fight has started between {self.f1.name} and {self.f2.name}!\n")
        total_rounds = 3
        round_turns = 12
           
        while self.current_round <= total_rounds:
            if self.fight_over:
                return
            print(f"--- Round {self.current_round} ---")
            self.f1.phase = "standup"
            self.f2.phase = "standup"
            self.phase = "standup"
            self.f1.round_landed = self.f1.round_missed = 0
            self.f2.round_landed = self.f2.round_missed = 0
            self.f1.round_takedown_landed = self.f1.round_takedown_attempts = 0
            self.f2.round_takedown_landed = self.f2.round_takedown_attempts = 0

            for turn in range(1, round_turns + 1):
                if self.fight_over:
                    return
                    
                if self.f1.is_knocked_out():
                    self.winner = self.f2.name
                    self.win_type = "KO"
                    self.end_fight()
                    return
                elif self.f2.is_knocked_out():
                    self.winner = self.f1.name
                    self.win_type = "KO"
                    self.end_fight()
                    return
            
                if self.phase == "standup":
                    #alternate turns
                    attacker, defender = (self.f1, self.f2) if turn % 2 == 1 else (self.f2, self.f1)
                    move = random.choices(["punch", "kick", "elbow", "takedown"], weights = [5,3,1,1])[0]
                    getattr(self, move)(attacker, defender)
                elif self.phase == "ground":
                     #lock control
                    if self.f1.phase == "ground_top":
                        self.ground_control(self.f1, self.f2) 
                    elif self.f2.phase == "ground_top":
                        self.ground_control(self.f2, self.f1)  


                if self.fight_over:
                    return
                    
            
            print(f"End of round {self.current_round}!\n")
            # end of round fighter 1 stats
            print(f"Round {self.current_round} Stats for {self.f1.name}: \nHits landed: {self.f1.round_landed} ")
            print(f"Hits missed: {self.f1.round_missed}\nTotal Damage: {self.f1.round_total_damage:.1f}\n")
            print(f"Takedowns landed: {self.f1.round_takedown_landed}")
            print(f"Takedowns attempts: {self.f1.round_takedown_attempts}\n")
            
            #end of round fighter 2 stats
            print(f"Round {self.current_round} Stats for {self.f2.name}: \nHits landed: {self.f2.round_landed} ")
            print(f"Hits missed: {self.f2.round_missed}\nRound Damage: {self.f2.round_total_damage:.1f}\n")
            print(f"Takedowns landed: {self.f2.round_takedown_landed}")
            print(f"Takedowns attempts: {self.f2.round_takedown_attempts}\n")

            self.f1.recover_stamina()
            self.f2.recover_stamina()

            if self.current_round < total_rounds:
                self.current_round += 1
            
           
            
        if self.f1.health > self.f2.health and self.current_round >= 3:
            print(f"\n{self.f1.name} is the winner by judges decision!")
            self.winner = self.f1.name
            self.win_type = "Decision"
            self.end_fight()
            return
                
        elif self.f1.health < self.f2.health and self.current_round >= 3:
            print(f"\n{self.f2.name} is the winner by judges decision!")
            self.winner = self.f2.name
            self.win_type = "Decision"
            self.end_fight()
            return

        


        




    