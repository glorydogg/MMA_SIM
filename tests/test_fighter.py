from engine.fighter import Fighter

# name, power, accuracy, stamina, grappling, takedown_defense, submission_defense
def test_take_damage():
    f = Fighter("Test", 90, 80, 76, 80, 77, 95)
    
    f.take_damage(20)
    assert f.health == 80

# name, power, accuracy, stamina, grappling, takedown_defense, submission_defense
def test_health_cant_go_below_zero():
    f = Fighter("Test", 90, 80, 76, 80, 77, 95)

    f.take_damage(500)
    assert f.health == 0

# name, power, accuracy, stamina, grappling, takedown_defense, submission_defense
def test_stamina_basic():
    f = Fighter("Test", 90, 80, 100, 80, 77, 95)
    

    f.use_stamina(20)
    assert f.stamina == 80

# name, power, accuracy, stamina, grappling, takedown_defense, submission_defense
def test_low_stamina_penalty():
    f = Fighter("Test", 90, 80, 35, 80, 77, 95)

    f.use_stamina(10)
    assert f.stamina == 23

# name, power, accuracy, stamina, grappling, takedown_defense, submission_defense
def test_stamina_never_negative():
    f = Fighter("Test", 90, 80, 100, 80, 77, 95)

    f.use_stamina(500)
    assert f.stamina == 0

# name, power, accuracy, stamina, grappling, takedown_defense, submission_defense
def test_effective_power_changes_with_stamina():
    f = Fighter("Test", 100, 85, 100, 80, 77, 95)
    
    assert f.effective_power == 100  # at 100 stamina

    f.stamina = 50
    assert f.effective_power == 50   # half stamina = half power

    f.stamina = 25
    assert f.effective_power == 25   # quarter stamina = quarter power

# name, power, accuracy, stamina, grappling, takedown_defense, submission_defense
def test_effective_accuracy_changes_with_stamina():
    f = Fighter("Test", 90, 80, 100, 80, 77, 95)

    high = f.effective_accuracy  # stamina = 100

    f.stamina = 50
    mid = f.effective_accuracy

    f.stamina = 0
    low = f.effective_accuracy

    assert high > mid > low  # accuracy should drop as stamina drops

def test_knockout_true():
    f = Fighter("Test", 90, 80, 100, 80, 77, 95)

    f.take_damage(100)
    f.is_knocked_out()
    assert f.is_knocked_out() == True
    
def test_knockout_false():
    f = Fighter("Test", 90, 80, 100, 80, 77, 95)

    f.is_knocked_out()
    assert f.is_knocked_out() == False

       