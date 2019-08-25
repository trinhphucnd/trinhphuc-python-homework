def check_array(x,y,arrays):
    for array in arrays:
        if x == array['x'] and y == array['y']:
            return True

def save_boxes(save_boxes):
    boxes_save = []
    for box in save_boxes:
        boxes_save.append(box.copy())
    return boxes_save



def print_map(map_sokoban,boxes,dess,player,os):
    
    for y in range(map_sokoban['y']): 
        for x in range(map_sokoban['x']):   
            
            
            player_is_here =  False
            if x == player["x"] and y == player["y"]:
                player_is_here =True
                
        
            if check_array(x,y,boxes):
                print("B ",end="")
          
            elif player_is_here:     
                print("P ",end="")
            
            elif check_array(x,y,dess):   
                print("D ",end="")
            
            elif check_array(x, y,os):
                print("O ",end="")
            
            else :
                print(". ", end="")
            

        print()
        
def check_in_map(x,y,max_x,max_y):
    return 0 <= x < max_x and 0 <= y < max_y

def check_next_pos(next_pos,array):
    return array.count(next_pos)


def check_result(boxes,dess):
    for box in boxes:
        if box not in dess:
            return False
    return True
