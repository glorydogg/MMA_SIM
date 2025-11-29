from engine.fight_engine import FightManager
from engine.fighter import Fighter


if __name__ == "__main__":
    fighter1 = Fighter("McGregor", power=95, accuracy=95, stamina=100, grappling= 85, takedown_defense= 65)
    fighter2 = Fighter("Khabib", power=85, accuracy=85, stamina=100, grappling= 99, takedown_defense= 95)

    engine = FightManager(fighter1, fighter2)
    engine.fight()
    