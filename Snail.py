
def snail(snail_map):
    
    hi = []
    if snail_map[0] == []:
        return hi


    val1 = snail_map[0][0]
    val2 = snail_map[0][1]
    val3 = snail_map[0][2]
    val4 = snail_map[1][2]

    val5 = snail_map[2][2]
    val6 = snail_map[2][1]
    val7 = snail_map[2][0]
    val8 = snail_map[1][0]
    val9 = snail_map[1][1]

    route=[]


    calc = [val1,val2,val3,val4,val5,val6,val7,val8,val9]


    for i in calc:
        route.append(i)

    # print(route)

snail([[]])