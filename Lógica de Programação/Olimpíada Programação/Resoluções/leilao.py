N = int(input())
maiorlance = 0
menorlance = 0

for i in range (N):
    C = str(input())
    V = float(input())
    
    if(i==0):
        maiorlance = V
        menor = V
      
    else:
        if V > maiorlance:
            maiorlance=V
        
        if V < menorlance:
            menorlance<V
    
print(C)
print(maiorlance)