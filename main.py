class car :
    def __init__(self,  name,  max_speed, mileage):
        self.name = name
        self.max_speed  = max_speed
        self.mileage = mileage

    def prntdetails(self):
        print ('name is: ', self.name)
        print ('max speed is: ', self.max_speed)
        print ('mileage  is: ',  self.mileage)

altroz  = car('altroz', 120, 23)

altroz.prntdetails()
        