
import random
    
    
random.seed(10)
    
    
class MonteCarlo:
    
    def __init__(self, simulations):
        self.simulations = simulations
    
    @staticmethod
    def generate_random_point():
        return random.uniform(-1, 1), random.uniform(-1, 1)
    
    @staticmethod
    def is_in_unit_circle(point):
        return point[0] ** 2 + point[1] ** 2 <= 1
    
    def estimate(self):
        points_in_circle = 0
    
        for _ in range(self.simulations):
            point = MonteCarlo.generate_random_point()
    
            if MonteCarlo.is_in_unit_circle(point):
                points_in_circle += 1
    
        result = 4 * points_in_circle / self.simulations
        return result