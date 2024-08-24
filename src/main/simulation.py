from numpy import e, square, pi, sqrt
from data import test_datas, test_value_name, test_result_name
import random
from scipy.stats import norm
from solution import Solution
from params import parameters, simulator, solution_archive_size, solution_archive, q_value


total_pheromone = 0

class Simulation:
    def initialize_simulation(self):
        for i in range(solution_archive_size):
            solution = Solution()
            solution.test_data  = random.choice(test_datas)
            for parameter in parameters:
                solution.variables[parameter] = random.uniform(*parameters[parameter])
            sim_result = simulator.simulate_test(solution)
            solution.update_pheromone(sim_result)
            global total_pheromone
            total_pheromone += solution.pheromone
            solution_archive.append(solution)
        self.modify_weights()
    
    def modify_weights(self):
        self.reorder_solution_archive()
        for i in range(solution_archive_size):
            solution = solution_archive[i]
            solution.weight = self.calculate_weight(i)

    def reorder_solution_archive(self):
        solution_archive.sort(reverse=True)

    def calculate_weight(self, rank):
        weight = self.get_weight(rank)
        return weight

    def print_solution_archive(self):
        for solution in solution_archive:
            print(solution.variables, '**', solution.weight, '**',solution.pheromone)
    def get_weight(selt, i):
        a = (1/(q_value*solution_archive_size*sqrt(2*pi)))*(e**(-(square(i-1)/(2*square(q_value*solution_archive_size)))))
        return a

#initialize_simulation()
#print_solution_archive()
