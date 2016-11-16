from data_from_ng import REVIEWS

from optimization_objective import make_optimization_objective

from random import seed

# In simultaneous_perturbation.py, you can implement Spall's algorithm.
#
# Alternatively, you can use Ng's method for calculating subsequent guesses as discussed in README.txt


# The following is a dummy implementation!! It is your job to implement it. See also the comment above.
def optimize_ng_example():
    lamb = 1.0  # I'd call this lambda, except in Python lambda is a keyword. Initialize to 1.0. What should it be?
    optimization_objective_function = make_optimization_objective(lamb, REVIEWS)
    x_list = [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0)]  # i, movie, x
    theta_list = [(0.0, 0.0), (0.0, 0.0), (0.0, 0.0), (0.0, 0.0)]  # j, user, theta
    print "Initially, the optimization objective is " + str(optimization_objective_function(x_list, theta_list))

if __name__ == "__main__":
    seed("lets see what happens")
    optimize_ng_example()
