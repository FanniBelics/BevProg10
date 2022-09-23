#Készíts két listát és írasd ki azokat az elemeket amik megegyeznek a listában

li1 = list(range(10)) #számok 1-10
li1.append(2)
li2 = list(range(0, 10, 2)) #páros számok 1-10

for i in li1:
    for j in li2:
        if i == j: 
            print(i)

for i in li1:
    if i in li2:
        print(i)