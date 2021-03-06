from entities import Direction
import random

class FixedTimeScheduler:
    def __init__(self, simulator, west_east_time):
        self.simulator = simulator
        self.switch_counter = 600
        self.switch_amount = 600        
        self.switch_time = west_east_time
        self.switch = False

    def schedule(self):  
        self.switch = False
        cars = 0
        reward = 0

        if(self.switch_counter >= self.switch_time):
            if(self.switch_counter >= (self.switch_time + (1/3) * (self.switch_amount - self.switch_time))):
                success = self.simulator.remove_car(Direction.NORTH, 'straight_right')                
                if (success != -1):                    
                    cars += 1
                    reward -= success**2                 
                success = self.simulator.remove_car(Direction.SOUTH, 'straight_right')                
                if (success != -1):
                    cars += 1
                    reward -= success**2                                                                  
            else:
                success = self.simulator.remove_car(Direction.NORTH, 'left')                
                if (success != -1):                                
                    cars += 1
                    reward -= success**2                                                  
                success = self.simulator.remove_car(Direction.SOUTH, 'left')                
                if (success != -1):
                    cars += 1
                    reward -= success**2                                  
        else:            
            if(self.switch_counter >= (1/3) * self.switch_time):
                success = self.simulator.remove_car(Direction.WEST, 'straight_right')                
                if (success != -1):                    
                    cars += 1
                    reward -= success**2             
                success = self.simulator.remove_car(Direction.EAST, 'straight_right')                
                if (success != -1):
                    cars += 1
                    reward -= success**2                                                  
            else:
                success = self.simulator.remove_car(Direction.WEST, 'left')                
                if (success != -1):                                
                    cars += 1
                    reward -= success**2                                 
                success = self.simulator.remove_car(Direction.EAST, 'left')                
                if (success != -1):
                    cars += 1
                    reward -= success**2                                   
        
        self.switch_counter -= 1

        if(self.switch_counter == 0):                
            self.switch_counter = self.switch_amount                                
            self.switch = True

        if(self.switch_counter == self.switch_time):                                
            self.switch = True

        return reward, self.switch, cars
    
    def __str__(self):
        return 'Fixed time scheduler'
