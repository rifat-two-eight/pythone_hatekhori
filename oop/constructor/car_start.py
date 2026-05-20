class Car():
    def __init__(self):
        self.clutch = False
        self.brk = False
    
    def start(self):
        self.clutch = True
        self.brk = True
        print("car started successfully")

car1 = Car()
car1.start()