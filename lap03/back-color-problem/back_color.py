from random import *
from check_inside import *
shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():
    return shapes



def generate_quiz():
    return [
                choice(['RED','BLUE',"GREEN",'YELLOW']),
                choice(['#4CAF50','#FFD600','#C62828','#3F51B5',]),
                randint(0,1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    posmouse = [x,y]
    if quiz_type == 0 and text == "BLUE":
        check = is_inside(posmouse,shapes[0]['rect'])
        print(check)
        if check :
            return True
        else :
            return False
    elif quiz_type == 0 and text == "RED":
        check = is_inside(posmouse,shapes[1]['rect'])
        print(check)
        
        if check :
            return True
        else :
            return False
    elif quiz_type == 0 and text == "YELLOW":
        # print(check)
        
        check = is_inside(posmouse,shapes[2]['rect'])
        print(check)
        if check :
            return True
        else :
            return False
    elif quiz_type == 0 and text == "GREEN":
        check = is_inside(posmouse,shapes[3]['rect'])
        print(check)
        if check:
            return True
        else :
            return False
    
    elif quiz_type == 1 and color == '#3F51B5':
        check = is_inside(posmouse,shapes[0]['rect'])
        print(check)
        if check :
            return True
        else :
            return False
    elif quiz_type == 1 and color == '#C62828':
        check = is_inside(posmouse,shapes[1]['rect'])
        print(check)
        if check  :
            return True
        else :
            return False
    elif quiz_type == 1 and color == '#FFD600':
        check = is_inside(posmouse,shapes[2]['rect'])
        print(check)
        if check  :
            return True
        else :
            return False
    elif quiz_type == 1 and color == '#4CAF50':
        check = is_inside(posmouse,shapes[3]['rect'])
        print(check)
        if check  :
            return True
        else :
            return False

    
