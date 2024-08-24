""" Algorithm parameters. """


from simulators import Simulator

# Model parameters to optimize: thier range .
parameters = {"a":(1, 5), "b":(1, 10)}

# No of discovered solutions to s.tore fore ACOR algorithm
solution_archive_size = 10  * len(parameters)

# Inversely affects convergence speed etc.
q_value  = 0.5

# Temporarily stores some previous solution
solution_archive = []

# Runs the Simulstiom
simulator = Simulator()