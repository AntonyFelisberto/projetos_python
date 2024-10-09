class Car(object):
    def __init__(self,speed,state):
        self.speed = speed
        self.state = state
    
    def start(self):
        self.state = "running"
        return self.state
    
    def turn_off(self):
        self.state = "off"
        return self.state
    
    def accelerate(self):
        self.speed +=10
        return self.speed
    
    def stop(self):
        self.speed = 0
        return self.speed

