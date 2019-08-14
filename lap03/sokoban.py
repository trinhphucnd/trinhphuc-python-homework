map_sokoban = {
    "x" : 6,
    "y" : 5,
}

player = {
    "x" : 0,
    "y" : 4,
}

boxes = [
    {"x": 1 , "y": 1},
    {"x": 2 , "y": 2},
    {"x": 3 , "y": 3},
]

dess = [
    {"x": 2 , "y" :1},
    {"x": 3 , "y" :2}, 
    {"x": 4 , "y" :3},
]

while True :

    for y in range(map_sokoban['y']): 
        for x in range(map_sokoban['x']):   

            box_is_here = False
            for box in boxes :
                if x == box["x"] and y == box["y"]:
                    box_is_here = True
                    break
            
            
            des_is_here = False
            for des in dess:
                if x == des["x"] and y == des["y"]:
                    des_is_here = True
                    break
            
            player_is_here =  False
            if x == player["x"] and y == player["y"]:
                player_is_here =True
                
        
            if box_is_here:
                print("B ",end="")
          
            elif player_is_here:     
                print("P ",end="")
            elif des_is_here:   
                print("D ",end="")
            else :
                print("- ", end="")

        print()

        # end print map_sokoban

    win = True
    for box in boxes:
        if box not in dess:
            win = False
    if win :
        print('You win')
        break

    move =  input("your move ? ").upper()
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
        
        next_pos_box = {'x': box['x'] + dx, 'y' : box['y'] + dy}
        next_pos_player =  {'x': player['x'] + dx, 'y' : player['y'] + dy}
        next_pos_player_two ={'x': player['x'] + 2*dx, 'y' : player['y'] + 2*dy}
        
        if (boxes.count(next_pos_player)) == 1 and (boxes.count(next_pos_player_two)) == 1 :
        
            player['x'] += 0
            player['y'] += 0
            
            break
       
        
        elif (boxes.count(next_pos_player_two)) == 0 and  (boxes.count(next_pos_player)) == 1 \
            and 0 <= next_pos_player_two['x'] < map_sokoban["x"] and 0 <= next_pos_player_two['y'] <= map_sokoban["y"] :
            
            player['x'] += dx
            player['y'] += dy
            
            break
        
        elif  (boxes.count(next_pos_box)) == 0 and (boxes.count(next_pos_player)) == 0 \
            and 0 <= next_pos_player['x'] < map_sokoban["x"] and 0 <= next_pos_player_two['y'] <= map_sokoban["y"]  :
            
            player['x'] += dx
            player['y'] += dy
            
            break
        
            

    for box in boxes:
        
        if  0 == (boxes.count(next_pos_box)) and box['x'] == player['x'] and box['y'] == player['y']\
             and 0 <= box['x'] + dx < map_sokoban["x"] and 0 <= box['y'] + dy < map_sokoban["y"]:
            box['x'] += dx
            box['y'] += dy
    
    

       
    
    
    

    
    
