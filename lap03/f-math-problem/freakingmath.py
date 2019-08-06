from random import *
from eval import *
def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(0,10)
    y = randint(1,10)
    err= randint(-1,1)
    ops = ["+","-","*","/"]
    op = choice(ops)
    result = calc(x,y,op)
    result += err
    return [x, y, op, result]

def check_answer(x, y, op, result, user_choice):
    resultreal = calc(x,y,op)
    err = result - resultreal
    if err == 0 and user_choice == True:
        return True
    elif err != 0 and user_choice == False:
        return True
    else :
        return False

    
