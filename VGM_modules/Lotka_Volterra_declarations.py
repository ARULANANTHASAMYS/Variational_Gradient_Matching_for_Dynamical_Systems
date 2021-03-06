
# # Lotka-Volterra Declarations
# 
# #### Authors: Nico S. Gorbach and Stefan Bauer


# In[1]:

# ## Import Numpy and Symbolic Computation Modules


import numpy as np
import sympy as sym


# In[2]:

# ## Object Class Declarations

odes_path = 'Lotka_Volterra_ODEs.txt' 
fig_shape = (10,8)

class simulation:
    initial_states = [5,3]
    integration_interval = 0.01
    state = None
    observations = None
    
class kernel:
    param = None
    
class time_points:
    true = np.arange(0.0, 4.0, 0.01)
    observed = None
    final_observed = 2.0
    
class symbols:
    state = sym.symbols(['_x_1','_x_2'])
    param = sym.symbols(['_theta_1','_theta_2','_theta_3','_theta_4'])
    
class opt_settings:
    number_of_ascending_steps = 50
    clamp_states_to_observation_fit = 0
    
class locally_linear_odes:
    class ode_param:
        B = None
        b = None
    class state:
        B = None
        b = None
        
class proxy:
    ode_param = None
    state = None