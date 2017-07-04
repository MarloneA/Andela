class Car(object):
    """ This is the car class """

    def __init__(self, name, model, car_type): # default car properties
        self.name = 'General'
        self.model = 'GM'
    
    """ defining car properties """
    self.name = name
    self.model = model
    self.car_type = car_type

    if self.name == 'Porshe' or self.name == 'Koenigsegg': # number of doors
        self.num_of_doors = 2
    else:
        self.num_of_doors = 4

    if self.car_type != 'trailer': # number of wheels
        self.num_of_wheels = 4

    def is_saloon(self):
        if self.num_of_wheels == 4:
            self.car_type = 'saloon'
            return True
        else:
            return False
    
    #def drive(self):
        