V = int(input())
A = int(input())
F = int(input())
P = int(input())
total = 0
V2 = V -A
V3 = V2 - F
V4 = V3 - P

if(A < V):
    total = total + 1
    V2 = V - A
    
if (F < V2):
    total = total + 1 
    V3 = V2 - F

if (P < V3):
    total = total + 1
    V4 = V3 - P
    
print (total)