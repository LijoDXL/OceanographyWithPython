# TO-SHOW: how to run a .py script
#==========
# run this script by typing the command below to your terminal:
# python test_script.py
# to run it in IPython, type:
# IPython
# It will open the python interative terminal, where you can type:
# %run test_script.py

# you might have to activate the environment where you have installed IPython and numpy-
# before runnning this script (to activate use: conda activate your-env-name)

import numpy as np
arr  = np.zeros((4,4))
add1 = arr+1
print(arr)
