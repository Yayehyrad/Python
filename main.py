# def sum(a, b):
#     """simple function that adds to int"""
#     return a+b

# # print(sum(1,2))
# # help(sum)
# """Zip(dic1,dic2) => val : val
#     enumerate(dic) => index : value
# """
# item1 = ['new' , "old"]
# item2 = [43 , 23]
 
# # for index , name ,num in  enumerate(zip(item1, item2)):
# #     print(index , name , num )
# # mylist = [ 10 if x%2 == 0 else 0 for x in range(1,10)  ]

# # print(mylist)
# arr = [1,2,3,4,5]

# # print(list(map(lambda x : x**2 , arr)))
# class Monster: 
#     def __init__(self , health , energy) -> None:
#         self.health = health
#         self.energy = energy
#     def attack(self):
#         self.energy = self.energy - 20
    

# monster = Monster(90 , 90)
# monster1 = Monster(100 , 100)
# print(monster.energy , monster.health)
# monster.attack()
# print(monster.energy , monster.health , monster1.energy , monster1.health)
# print(monster.__dict__)
# name = "nano"

# print(dir(name))
# def add(a,b):
#     return a+b
# class Test:
#     def __init__(self , fun) -> None:
#         self.fun = fun
 
# test = Test(add)
# print(test.fun(1,2))

class Monster:
    def __init__(self ,health,energy):
        self.health=health
        self.energy = energy
    def det_damage(self , amount):
        self.health -= amount


class Hero:
    def __init__(self, damage , monster) -> None:
            self.damage = damage
            self.monster= monster
    def attack(self):
        self.monster.det_damage(self.damage)

class Attack:
    def bite(self):
        print("bite")
    def strike(self):
        print("strike")
    def slash(self):
        print("slash")
    def kick(self):
        print("kick")


monster1 = Monster(100 , 100)

newPlayer = Hero(30 , monster1)

newPlayer.attack()

print(monster1.health)



"""dunder methods"""



