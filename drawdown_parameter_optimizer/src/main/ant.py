""" Ant: for ACOR algoritm """

from src.main.solution import Solution
from src.main.params import parameters
from scipy.stats import truncnorm

class Ant:
    def __init__(self, no, test_data):
        """ Constructor: initilizes object variables """
        
        self.no = no
        self.test_data = test_data
    
    def find_solution(self, old_solution, sds):
        """
        Generates a new solution
        Return: generated solution
        """
        new_solution = Solution()

        # Each ant generates solutions wuth the vary same test data
        new_solution.test_data = self.test_data

        # Sample gussian distributions generated by solution
        # for new values to variables of new solution
        for variable in new_solution.variables:
            # mean or loc: equals value of variable in old_solution
            mu = old_solution.variables[variable]
            # standard seviations of current variable with other solutoons
            sd = sds[variable]
            # Upper and lower range of parameter
            a, b = parameters[variable]
            a, b = (a - mu)/sd, (b - mu)/sd
            # Generate gussian diatribution to ample 
            gus = truncnorm(a, b, loc=mu, scale=sd)
            # Sample gussian distribution
            new_solution.variables[variable] = gus.rvs()
        
        return new_solution
