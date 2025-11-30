import random


PUNCH_LINES = [
    "{A} lands a quick jab on {D}.\n",
    "{A} with the lightning fast jab.\n",
    "{A} gets the jab to go on {D}.\n"
]

PUNCH_MISS_LINES = [
    "{A} fires a jab but it whiffs!\n",
    "{A} just misses the jab — {D} pulls back!\n",
    "{A} throws a jab but {D} slips it!\n",
    "{A}'s jab falls short!\n",
    "{D} avoids the jab with good head movement!\n"
]


KICK_LINES = [
    "{A} lands a nice firm body kick on {D}.\n",
    "OH! {A} rocks {D} with the a head kick!\n",
    "{A} with the firm kick to {D} torso!\n"
]

KICK_MISS_LINES = [
    "{A} throws a body kick but misses!\n",
    "{A}'s kick sails past {D}!\n",
    "{A} tries a head kick but {D} steps away!\n",
    "{A} misses the kick — off balance!\n",
    "{D} reads the kick and avoids it!\n"
]


ELBOW_LINES = [
    "{A} slices {D} with an elbow!\n",
    "{A} with the clever elbow on {D}!\n",
    "Wow! what an elbow by {A} on {D}!\n"
]

ELBOW_MISS_LINES = [
    "{A} swings an elbow but misses!\n",
    "{A} tries to slice with an elbow — {D} dodges!\n",
    "{A}'s elbow misses by inches!\n",
    "{A} throws an elbow but {D} backs out of range!\n",
    "{A} misses the elbow — risky attempt!\n"
]


TAKEDOWN_ATTEMPT_LINES = [
    "{A} shoots in for the takedown!\n",
    "{A} level-changes and drives forward!\n",
    "{A} goes for a double-leg!\n",
    "{A} closes the distance looking for a takedown!\n",
    "{A} changes levels and attacks the hips!\n",
]

TAKEDOWN_FAIL_LINES = [
    "{D} sprawls and denies the takedown!\n",
    "{D} stuffs the shot with great defense!\n",
    "{D} sees it coming and shuts down the attempt!\n",
    "{D} sprawls perfectly and forces {A} back up!\n",
    "{D} defends the takedown — great balance!\n",
]

TAKEDOWN_SUCCESS_LINES = [
    "{A} gets the takedown and lands in top position!\n",
    "{A} drags {D} to the canvas!\n",
    "{A} completes the takedown with authority!\n",
    "{A} brings {D} down and takes control!\n",
    "{A} finishes the takedown and moves to top control!\n",
]

SUBMISSION_ATTEMPT_LINES = [
    "{A} isolates the neck — submission attempt!\n",
    "{A} is hunting for a choke!\n",
    "{A} wraps up the neck and goes for a submission!\n",
    "{A} is tightening up a submission attempt!\n",
    "{A} attacks the neck — this could be tight!\n",
]

SUBMISSION_FAIL_LINES = [
    "{D} fights the hands and escapes!\n",
    "{D} stays calm and slips out!\n",
    "{D} defends well and survives the submission!\n",
    "{D} breaks free — great defense!\n",
    "{D} manages to escape the choke!\n",
]

SUBMISSION_WIN_LINES = [
    "{D} taps! {A} gets the submission!\n",
    "{A} forces the tap — it’s over!\n",
    "{A} locks it in, and {D} has no choice but to tap!\n",
]

KO_WIN_LINES = [
    "{A} drops {D}! It’s over!\n",
    "{D} is out cold — huge KO from {A}!\n",
    "{A} shuts the lights out with a massive shot!\n",
]

LINES = {
    "punch": PUNCH_LINES,
    "punch_miss": PUNCH_MISS_LINES,
    "kick": KICK_LINES,
    "kick_miss": KICK_MISS_LINES,
    "elbow": ELBOW_LINES,
    "elbow_miss": ELBOW_MISS_LINES,
    "takedown_attempt": TAKEDOWN_ATTEMPT_LINES,
    "takedown_fail": TAKEDOWN_FAIL_LINES,
    "takedown_success": TAKEDOWN_SUCCESS_LINES,
    "submission_attempt": SUBMISSION_ATTEMPT_LINES,
    "submission_fail": SUBMISSION_FAIL_LINES,
    "submission_win": SUBMISSION_WIN_LINES,
    "ko_win": KO_WIN_LINES
}

def say(category, A, D):
    if category not in LINES:
        return ""
    
    template = random.choice(LINES[category])
    return template.replace("{A}", A).replace("{D}", D)
    