import random

def score_round(f1_stats, f2_stats):
        """
    f1_stats / f2_stats = dict containing:
    landed, damage, tkd_landed, tkd_attempts
    """

        f1_score = 10
        f2_score = 10

        # DAMAGE → biggest factor
        if f1_stats["f1_damage"] > f2_stats["f2_damage"] * 1.3:
            f1_score, f2_score = 10, 9
        elif f2_stats["f2_damage"] > f1_stats["f1_damage"] * 1.3:
            f1_score, f2_score = 9, 10

    # STRIKING VOLUME
        if f1_stats["f1_landed"] > f2_stats["f2_landed"] + 10:
            f2_score -= 1
        elif f2_stats["f2_landed"] > f1_stats["f1_landed"] + 10:
            f1_score -= 1

    # WRESTLING DOMINANCE
        if f1_stats["f1_takedowns"] > f2_stats["f2_takedowns"]:
            f1_score += 0
        elif f2_stats["f2_takedowns"] > f1_stats["f1_takedowns"]:
            f2_score += 0

    # MAKE SURE SCORES STAY VALID UFC SCORES
        f1_score = max(7, min(10, f1_score))
        f2_score = max(7, min(10, f2_score))

        return f1_score, f2_score

      

def score_fight():
    
    pass
