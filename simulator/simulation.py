from engine.fight_engine import FightManager
from engine.fighter import Fighter

class Simulator:
    def __init__(self, base_f1: Fighter, base_f2: Fighter):
        # Base fighter's stats

        self.base_f1 = base_f1
        self.base_f2 = base_f2

        self.results = {
            "fighter1_wins": 0,
            "fighter2_wins": 0,
            "ko_wins": 0,
            "sub_wins": 0,
            "decision": 0
        }
        self.history = []

    def clone_fighters(self):
        f1 = Fighter(
            name=self.base_f1.name,
            power=self.base_f1.power,
            accuracy=self.base_f1.accuracy,
            stamina=self.base_f1.stamina,
            grappling=self.base_f1.grappling,
            takedown_defense=self.base_f1.takedown_defense,
            submission_defense=self.base_f1.submission_defense
        )
        f2 = Fighter(
            name=self.base_f2.name,
            power=self.base_f2.power,
            accuracy=self.base_f2.accuracy,
            stamina=self.base_f2.stamina,
            grappling=self.base_f2.grappling,
            takedown_defense=self.base_f2.takedown_defense,
            submission_defense=self.base_f2.submission_defense
        )
        return f1, f2
    
    def run_one_fight(self):
        f1, f2 = self.clone_fighters()
        manager = FightManager(f1, f2)
        manager.fight()

        # record winner info
        self.history.append({
            "winner": manager.winner,
            "method": manager.win_type,
            "round": manager.current_round
        })

        # update tallies
        if manager.winner == f1.name:
            self.results["fighter1_wins"] += 1
        else:
            self.results["fighter2_wins"] += 1
        
        if manager.win_type == "KO":
            self.results["ko_wins"] += 1
        elif manager.win_type == "Submission":
            self.results["sub_wins"] += 1
        else:
            self.results["decision"] += 1
        
        print("DEBUG winner:", manager.winner, manager.win_type)

    def run_batch(self, n :int):
        for _ in range(n):
            self.run_one_fight()

    def summary(self):
        print("\n=== Simulation Summary ===")
        print(f"{self.base_f1.name} wins: {self.results['fighter1_wins']}")
        print(f"{self.base_f2.name} wins: {self.results['fighter2_wins']}")
        print(f"KO wins: {self.results['ko_wins']}")
        print(f"Submission wins: {self.results['sub_wins']}")
        print(f"Decision wins: {self.results['decision']}")




