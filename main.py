class car :

    tires  =  4 #class variables
    color = 'white'

    def __init__(self,  name,  max_speed, mileage):
        self.name = name
        self.max_speed  = max_speed
        self.mileage = mileage
        self.musys = self.musicsystm() #paraenthesis are mandatory while creting an object/inner object.

    def prntdetails(self):
        print ('name is: ', self.name)
        print ('max speed is: ', self.max_speed)
        print ('mileage  is: ',  self.mileage)
        self.musys.show()

    #inner class music system
    class musicsystm:
        def __init__(self):
            self.brand = 'JBL'
            self.nospkrs = 6
        
        def show(self):
            print("musicsystem brand is", self.brand,"Number of speakers is", self.nospkrs)

# creating class methods 
    @classmethod
    def displaytires(cls):
        print ("Every  car has", car.tires, "tires")

    @classmethod
    def changenumbeoftires(cls, tires):
        cls.tires =  tires
        print ("Number of tires is changed to ", car.tires)

#  Create static methods
    @staticmethod
    def showcolor():
        print(car.color)

# global method
def speeddiff(a:car , b:car):
    if(type(a) != type(b)):
        print('cannot compare')
        return
    print('Difference in speed is:', a.max_speed - b.max_speed)

class bike :
    def __init__(self, max_speed) :
        self.max_speed = max_speed
        pass

altroz  = car('altroz', 120, 23)
nexon = car('nexon', 125, 18 )
shine = bike(90)

# altroz.prntdetails()
# print(type(car))


# speeddiff(nexon, altroz)
# speeddiff(nexon,  shine)

# practice class variables
# print (altroz.tires)
# altroz.tires = 7
# print (nexon.tires)
# print (altroz.tires)

# car.displaytires()
# car.changenumbeoftires(8)
# car.showcolor()