import random
def random_walk_2(n):
    x,y = 0,0
    for i in range(n):
        (dx,dy)=random.choice([(0,1),(0,-1),(1,0),(-1,0)])
        x += dx
        y +=dy
    return (x,y)
for i in range(25):
    walk = random_walk_2(10)
    print(walk,"Distance from home =", abs(walk[0])+abs(walk[1]))
number_of_walks=20000
for walk_lenght in range(1,31):
    no_transport = 0
    for i in range(number_of_walks):
        (x,y)=random_walk_2(walk_lenght)
        distance=abs(x)+abs(y)
        if distance <=4:
            no_transport +=1
    no_transport_percentage = float(no_transport)/number_of_walks
    print("walk size = ",walk_lenght," /% of no transport =",100*no_transport_percentage)