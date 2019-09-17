# -*- coding: utf-8 -*-

"""
猫狗队列

"""

class Pet:
    def __init__(self, type):
        self.type = type

    def getPettype(self):
        return self.type

class PetEnterQueue:
    def __init__(self, pet, count):
        self.pet = pet
        self.count = count

    def getpet(self):
        return self.pet

    def getcount(self):
        return self.count

    def getEnterPetType(self):
        return self.pet.getPettype()

class DogCatQueue:
    def __init__(self):
        self.dogQ = []
        self.catQ = []
        self.count = 0

    def add(self, pet):
        if pet.getPettype() == 'dog':
            self.dogQ.append(PetEnterQueue(pet, self.count))
            self.count += 1
        elif pet.getPettype() == 'cat':
            self.catQ.append(PetEnterQueue(pet,self.count))
            self.count += 1
        else:
            print('erro, not dog or cat')

    def pollAll(self):
        if self.dogQ and self.catQ:
            if self.dogQ[0].getcount() < self.dogQ[0].getcount():
                return self.dogQ.pop(0).getpet()
            else:
                return self.catQ.pop(0).getpet()
        elif self.dogQ:
            return self.dogQ.pop(0).getpet()
        elif self.catQ:
            return self.catQ.pop(0).getpet()
        else:
            print('err, queue is empty!')

    def isEmpty(self):
        return len(self.catQ) == 0 and len(self.dogQ) == 0

    def isDogQueueEmpty(self):
        return len(self.dogQ) == 0

    def isCatQueueEmpty(self):
        return len(self.catQ) == 0

    def pollDog(self):
        if not self.isDogQueueEmpty():
            return self.dogQ.pop(0).getpet()
        else:
            print('dog queue is empty!')

    def pollCat(self):
        if not self.isCatQueueEmpty():
            return self.catQ.pop(0).getpet()
        else:
            print('cat queue is empty!')

if __name__ == "__main__":
    test = DogCatQueue()
    dog = 'dog'
    cat = 'cat'
    dog1 = Pet(dog)
    dog2 = Pet(dog)
    dog3 = Pet(dog)
    cat1 = Pet(cat)
    cat2 = Pet(cat)
    cat3 = Pet(cat)


    test.add(dog1)
    test.add(cat1)
    test.add(dog2)
    test.add(cat2)
    test.add(dog3)
    test.add(cat3)

    test.add(dog1)
    test.add(cat1)
    test.add(dog2)
    test.add(cat2)
    test.add(dog3)
    test.add(cat3)

    test.add(dog1)
    test.add(cat1)
    test.add(dog2)
    test.add(cat2)
    test.add(dog3)
    test.add(cat3)

    while not test.isDogQueueEmpty():
        print(test.pollDog().getPettype())



