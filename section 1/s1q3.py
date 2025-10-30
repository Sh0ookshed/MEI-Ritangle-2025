#SECTION 1 , QUESTION 3
def get_numbers():
    #locals
    total = 6**5
    div_num = 0
    dice_roll = [1,1,1,1,1,1]
    index = 0
    iterate = False

    for x in range (total-1): 
        if dice_roll[index] == 7:
            dice_roll[index] = 1
            iterate = True
            while iterate == True:
                index += 1
                dice_roll[index]  += 1
                if dice_roll[index] == 7:
                    dice_roll[index] = 1
                else:
                    iterate = False
                    index = 0
        dice_roll[index] +=1
        if 2 in dice_roll and 5 in dice_roll:
            div_num += 1
    return div_num / total



#main
print(round(get_numbers(),3))