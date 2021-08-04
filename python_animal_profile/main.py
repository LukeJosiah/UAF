import sys
import os

def main():
    file = 'animalProfile.txt'
    hours = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    periods = ['AM', 'PM']
    # text file assume the following format:
    #                                       type of animal
    #                                       weight of animal
    #                                       cups of food per day
    #                                       number of feedings per day
    #
    #
    # read animal type, weight, cups per day, and number of feedings from text file
    with open(file) as fp:
        line = fp.readline().strip()
        animal = line

        line = fp.readline().strip()
        weight = float(line)

        line = fp.readline().strip()
        cupsPerDay = float(line)

        line = fp.readline().strip()
        numberOfFeedings = int(line)

    # 3 animals (more can be added in future) recommended feeding amount.
    # calculate a recommended feeding amount for animal type (dog)
    if animal == 'dog':
        if weight <= 3:
            recommendingFeedingAmount = .33
        elif weight <= 6:
            recommendingFeedingAmount = .5
        elif weight <= 10:
            recommendingFeedingAmount = .75
        elif weight <= 15:
            recommendingFeedingAmount = 1
        elif weight <= 20:
            recommendingFeedingAmount = 1.33
        elif weight <= 30:
            recommendingFeedingAmount = 1.75
        elif weight <= 40:
            recommendingFeedingAmount = 2.25
        elif weight <= 50:
            recommendingFeedingAmount = 2.66
        elif weight <= 60:
            recommendingFeedingAmount = 3
        elif weight <= 70:
            recommendingFeedingAmount = 3.5
        elif weight <= 80:
            recommendingFeedingAmount = 3.75
        elif weight <= 90:
            recommendingFeedingAmount = 4.25
        elif weight <= 100:
            recommendingFeedingAmount = 4.5
        else:
            recommendingFeedingAmount = 4.5 + .33*((weight-100)/10)

    # (cat)
    if animal == 'cat':
        if weight <= 5:
            recommendingFeedingAmount = .33
        elif weight <= 10:
            recommendingFeedingAmount = .5
        elif weight <= 15:
            recommendingFeedingAmount = .75
        else:
            recommendingFeedingAmount = .75 + .25*((weight-15)/5)
    
    # (pot-bellied pig)
    if animal == 'pot-bellied pig':
        recommendingFeedingAmount = (weight/25)*.5


    f = open("profile.txt", "w+")

    f.write(animal + "\n")
    f.write(str(weight) + "\n")
    f.write(str(cupsPerDay) + "\n")
    f.write(str(numberOfFeedings) + "\n")
    f.write(str(recommendingFeedingAmount) + "\n")
    
    f.close()
    
    
    
"""     print(recommendingFeedingAmount)
        print(animal)
        print(weight)
        print(cupsPerDay)
        print(numberOfFeedings) """


if __name__ == '__main__':
    main()
