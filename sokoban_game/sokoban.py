from funcion_sokoban import *


map_sokoban = {
    "x" : 6,
    "y" : 6,
}

player = {
    "x" : 0,
    "y" : 4,
}
save_player_pos ={"x" : 0,
    "y" : 4,}
save_player_pos['x'] = player['x']
save_player_pos['y'] = player['y']


boxes = [
    {"x": 1 , "y": 1},
    {"x": 4 , "y": 2},
    {"x": 3 , "y": 4},
]

dess = [
    {"x": 2 , "y" :1},
    {"x": 3 , "y" :2}, 
    {"x": 4 , "y" :4},
]

obs = [
    {"x": 2 , "y" :2},
    {"x": 3 , "y" :1}, 
    {"x": 4 , "y" :3},
]



print_map(map_sokoban,boxes,dess,player,obs)

while True :


    move =  input("Your move ? or (Z-undo) : ").upper()
    
    
    if move == "Z":
        player['x'] = save_player_pos['x']
        player['y'] = save_player_pos['y']
        boxes = boxes_save
        
    else:
        
        boxes_save = save_boxes(boxes)
        save_player_pos['x'] = player['x']
        save_player_pos['y'] = player['y']
        
        dx = 0
        dy = 0  

        if move =="W":
            dy = -1
        elif move == "S":
            dy = 1
        elif move == "A":
            dx = -1
        elif move == "D":
            dx = 1
        
        for box in boxes :
            
            next_box_pos = {'x': box['x'] + dx, 'y' : box['y'] + dy}
            next_player_pos =  {'x': player['x'] + dx, 'y' : player['y'] + dy}
            next_player_pos_two ={'x': player['x'] + 2*dx, 'y' : player['y'] + 2*dy}
            
            # Player không đẩy được 2 hộp
            if check_next_pos(next_player_pos,boxes) == 1 and check_next_pos(next_player_pos_two,boxes) == 1 :
            
                player['x'] += 0
                player['y'] += 0
                
                break
        
            # Player không đẩy được box qua chướng ngại vật
            elif check_next_pos(next_player_pos_two,boxes) == 0 and  check_next_pos(next_player_pos,boxes) == 1 and check_next_pos(next_player_pos_two,obs) == 0 \
                and check_in_map(next_player_pos_two['x'],next_player_pos_two['y'],map_sokoban['x'],map_sokoban['y']) :
                
                player['x'] += dx
                player['y'] += dy
                
                break
            
            # Player di chuyển tự do , không đi qua được chướng ngại vật
            elif  check_next_pos(next_box_pos,boxes) == 0 and check_next_pos(next_player_pos,boxes) == 0 and check_next_pos(next_player_pos,obs) == 0 \
                and  check_in_map(next_player_pos['x'],next_player_pos['y'],map_sokoban['x'],map_sokoban['y'])  :
                
                player['x'] += dx
                player['y'] += dy
                
                break

        

        for box in boxes:
            
            if   box['x'] == player['x'] and box['y'] == player['y'] and check_next_pos(next_box_pos,boxes) == 0 \
                and check_in_map(box['x'] , box['y'], map_sokoban["x"],map_sokoban["y"]):
                
                box['x'] += dx
                box['y'] += dy

    # In map
    print_map(map_sokoban,boxes,dess,player,obs)
    print()
    
    # Kiểm tra kết quả
    if check_result(boxes,dess):
        print("You Win")
        break
            


    
    

       
    
    
    

    
    
