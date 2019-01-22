import numpy as np
from numba import njit, prange

 # consav
from consav import linear_interp # for linear interpolation
from consav import golden_section_search # for optimization in 1D

# local modules
import utility

# a. define objective function
@njit
def obj_bellman(c,m,interp_w,par):
    """ evaluate bellman equation """

    # a. end-of-period assets
    a = m-c
    
    # b. continuation value
    w = linear_interp.interp_1d(par.grid_a,interp_w,a)

    # c. total value
    value_of_choice = utility.func(c,par) + w

    return -value_of_choice # we are minimizing

# b. create optimizer
opt_bellman = golden_section_search.create_optimizer(obj_bellman)

# c. solve bellman equation        
@njit(parallel=True)
def solve_bellman(t,sol,par):
    """solve bellman equation using nvfi"""

    # unpack
    v = sol.v[t]
    c = sol.c[t]

    # loop over outer states
    for ip in prange(par.Np):

        # a. permanent income
        p = par.grid_p[ip]

        # b. loop over cash-on-hand
        for im in range(par.Nm):
            
            # i. cash-on-hand
            m = par.grid_m[im]

            # ii. optimal choice
            c_low = np.fmin(m/2,1e-8)
            c_high = m
            c[ip,im] = opt_bellman(c_low,c_high,par.tol,m,sol.w[ip],par)

            # iii. optimal value
            v[ip,im] = -obj_bellman(c[ip,im],m,sol.w[ip],par)
