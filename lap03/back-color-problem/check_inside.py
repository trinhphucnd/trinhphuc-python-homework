# posmouse = []
# rect = [3,4,5,6]

def is_inside(posmouse,rect):
    
    if rect[0]<=posmouse[0]<=rect[0]+rect[2] and rect[1]<=posmouse[1]<=rect[1]+rect[3]:
        
        
        return True
    else:
        
        return False
    