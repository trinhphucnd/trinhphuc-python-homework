words = ["Được", "Mới", "Như thế nào", "Làm"]

words ={
    "dc" : "Được " , 
    "ms" : "Mới",
    "ntn" : "Như thế nào",
    "lm" : 'Làm'
}

while True :
    for key , value in words.items():
        print(key , end='   ')

    print()

    y_code = input("Your Code :")
    if y_code in words:
        print("Translation : " , words[y_code])
        
    else:
        ques = input("Not found . Do you want to contribute this word ? (Y/N)")
        if ques == "y" :
            translation = input("Translation : ")
            words[y_code] = translation
            print("updated")
        else:
            break
