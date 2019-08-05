point = [1,2]
rec = [3,4,5,6]

def is_inside(point,rec):
    
    print(point,rec)
 
    if rec[0]<=point[0]<=rec[0]+rec[2] and rec[1]<=point[1]<=rec[1]+rec[3]:
        print(True)
    else:
        print(False)
    return