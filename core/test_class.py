from itertools import count
class Fridge:

    
    def in_fridge (self, wanted_food):
        fridge = {'apples':10, 'oranges':3, 'milk':2}
        count=0
        try:
            count = fridge[wanted_food]
            print(count)
        except KeyError:
            count = 0
                      
        return count

if __name__ == '__main__':
    Fridge().in_fridge('apples')