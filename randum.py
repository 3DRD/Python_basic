import random

# few random functions
# random.random - to get random numbers between 0-1
# random.randint(intial,final) - to get random from intial integer to final integer
# random.choice(List_name) -to get a random choice out of list

for i in range(3):
    print(random.random())

for i in  range(3):
    print(random.randint(10,20))

name=['DRD',"ARD",'RRD',"TRD"]
choice=random.choice(name)
print(choice)

for i in range(3):
    print(random.randrange(6,10,1))