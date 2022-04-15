import math


def hotDogs():
    hotDogPack = 10
    hotDogBunPack = 8
    print("how many people are going to be attending the cookout?")
    x = int(input())
    if x != "":
        print("Ok!, how many hot dogs will each person be getting?")
        y = int(input())
        if y != "":
            neededHotDogPack = math.ceil(x * y / hotDogPack)
            neededHotDogBunPack = math.ceil(x * y / hotDogBunPack)
            leftOverHotDogs = (hotDogPack * neededHotDogPack) - (x * y)
            leftOverHotDogsBun = (hotDogBunPack * neededHotDogBunPack) - (x * y)
            print("required packs of hot dogs: ", neededHotDogPack, "\nrequired packs of hot dog buns:", neededHotDogBunPack,
                  "\nleftover hot dogs: ", leftOverHotDogs, "\nleftover hotdog bun", leftOverHotDogsBun)
        else:
            print("please enter the expected number of people")
    else:
        print("please enter the expected number of hot dogs each person will be getting")


hotDogs()