import dimod
from dimod import SimulatedAnnealingSampler

# The objective function to minimize is E(x1,x2)= x1 + x2 - 2x1x2.
# Define a small QUBO
# The keys are tuples of variables (i, j), and values are the coefficients Q_i,j
Q = {
    (0, 0): 1,  # Linear coefficient for qubit 0 (Q_0,0 * x_0)
    (1, 1): 1,  # Linear coefficient for qubit 1 (Q_1,1 * x_1)
    (0, 1): -2   # Quadratic coefficient for the interaction between 0 and 1 (Q_0,1 * x_0 * x_1)
}
# We can also define a small QUBO as
#Q = {('x1', 'x1'): 1, ('x2', 'x2'): 1, ('x1', 'x2'): -2}

# Use a local simulated annealer
sampler = SimulatedAnnealingSampler()

# Solve it!
response = sampler.sample_qubo(Q, num_reads=100)

# Display results
print("Results:")
for sample, energy in response.data(['sample', 'energy']):
    print(sample, "Energy:", energy)
