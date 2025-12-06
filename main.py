from engine.fighter import Fighter
from simulator.simulation import Simulator


def main():
    f1 = Fighter("McGregor", power=95, accuracy=95, stamina=100, grappling= 85, takedown_defense= 65, submission_defense= 85)
    f2 = Fighter("Khabib", power=85, accuracy=85, stamina=100, grappling= 99, takedown_defense= 95, submission_defense= 95)

    sim = Simulator(f1, f2)
    
    sim.run_batch(100)
    sim.summary()

    
if __name__ ==  "__main__":
    main()