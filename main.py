class car :

    tires  =  4 #class variables

    def __init__(self,  name,  max_speed, mileage):
        self.name = name
        self.max_speed  = max_speed
        self.mileage = mileage

    def prntdetails(self):
        print ('name is: ', self.name)
        print ('max speed is: ', self.max_speed)
        print ('mileage  is: ',  self.mileage)

class bike :
    def __init__(self, max_speed) :
        self.max_speed = max_speed
        pass

altroz  = car('altroz', 120, 23)
nexon = car('nexon', 125, 18 )
shine = bike(90)

# altroz.prntdetails()
# print(type(car))

def speeddiff(a:car , b:car):
    if(type(a) != type(b)):
        print('cannot compare')
        return
    print('Difference in speed is:', a.max_speed - b.max_speed)

speeddiff(nexon, altroz)
speeddiff(nexon,  shine)

#practice class variables
print (altroz.tires)
altroz.tires = 7
print (nexon.tires)
print (altroz.tires)