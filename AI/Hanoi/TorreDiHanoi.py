moves_counter=1
L=[['A'],['B'],['C']]           #list of lists: status of each rod



def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    global moves_counter
    global L
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)

    if from_rod == 'A':                 #individuates the from_rod rod
        x = 0
    elif from_rod == 'B':
        x=2
    else:
        x=1
    
    if to_rod == 'A':                   #individuates the to_rod rod
        y=0
    elif to_rod == 'B':
        y=2
    else:
        y=1

    L[y].append(L[x].pop())                 #updates rod status
    
    print("   " if moves_counter <= 9 else "" ,"  " if moves_counter <100 and moves_counter >9 else "", " " if moves_counter >=100 and moves_counter <1000 else "", "" if moves_counter>=1000 else "", str(moves_counter) + "." ,"Move disk", n, "from rod", from_rod, "to rod", to_rod, ". A(", str(L[0][1:]).strip("[]"),"), ","B(", str(L[2][1:]).strip("[]"),"),  ", "C(",str(L[1][1:]).strip("[]"),").")
   #print("   " if moves_counter <= 9 else "" ,"  " if moves_counter <100 and moves_counter >9 else "", " " if moves_counter >=100 and moves_counter <1000 else "", "" if moves_counter>=1000 else "", str(moves_counter) + "." ,"Move disk", n, "from rod", from_rod, "to rod", to_rod, ".A(", str(L[0][1:]).strip("[]"),"), ","B(", str(L[2][1:]).strip("[]"),"),  ", "C(",str(L[1][1:]).strip("[]"),").")

    moves_counter=moves_counter+1
    
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)







N = int(input("How many disks?  "))
if N >= 1 and N <= 10: 
    for i in reversed(range(N)):            #input check
        L[0].append(i+1)
    
    print("   Initial state ", L[0][0], "(", str(L[0][1:]).strip("[]"),"),", L[1][0], "(", str(L[1][1:]).strip("[]"),"),", L[2][0],"(",str(L[2][1:]).strip("[]"),").")
    #print("   Initial state ", L[0][0], "(", str(L[0][1:]).strip("[]"),"),", L[1][0], "(", str(L[1][1:]).strip("[]"),"),", L[2][0],"(",str(L[2][1:]).strip("[]"),").")

    TowerOfHanoi(N, L[0][0], L[2][0], L[1][0])
    print("\t Program ends")

else:
    print("Wrong input, must be a number 1<=N<=10")