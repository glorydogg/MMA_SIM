from engine.judges import score_round


def test_judge_damage_win():    
        f1 = {"f1_landed": 5, "f1_damage": 50, "f1_takedowns":0}
        f2 = {"f2_landed": 5, "f2_damage": 10, "f2_takedowns":0}
        
        s1, s2 = score_round(f1, f2)
        
        assert (s1, s2) == (10, 9)