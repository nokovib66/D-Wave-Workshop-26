# Minimize the following nonlinear function:
#   f(x,y) = (x-1)^2 + (y-2)^2 + sin(3x) + cos(2y)
# subjet to bounds
#    -5 <= x <= 5

from dwave.system import LeapHybridNLSampler
import dimod

# Define the objective function
def objective(x):
    return (x[0] - 1)**2 + (x[1] - 2)**2 + np.sin(3*x[0]) + np.cos(2*x[1])

# Define variable bounds
bounds = [(-5, 5), (-5, 5)]  # for x and y

# Create the problem in dimod format
model = dimod.ContinuousQuadraticModel()
model.set_objective(objective)

# Initialize the NLP hybrid solver
sampler = LeapHybridNLSampler()

# Submit the problem
result = sampler.sample_cqm(model)

# Show best result
best = result.first
print("Best solution found:")
print(best.sample)
print("Energy:", best.energy)


