---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.2'
      jupytext_version: 1.5.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

## Jupyter Notebook
* interactive computing
* cells can be a code, markdown or raw text
* prints out last time of cell, no need to add `print()`
* use markdown to write your thoughts
* two modes: command mode and edit mode


## shortcuts to remember:
* `enter` or `double-click`, start edit mode
* `esc` to return to command mode
* `shift+enter` execute current cell and move to next
* `ctrl+enter` execute current cell and stay there
* `a` and `b`, add cell above or below
* `dd` delete a cell
* `c` and then `v`, copy and paste a cell
* `m` turn cell into markdown
* `y` trun cell into code


## The basics

```python
# no data type declaration
a = 3
b = 19
a+b
```

```python
# string concat
first_name = 'Shaji'
second_name = 'P'
first_name+' '+second_name
```

```python
# string method example
statement = "this is a sentence"
statement.count('s')
```

```python
# string method example
statement.split()
```

```python
# Python list
x = [12,9,6,4]
y = [1,2,4]
x+y # lists are concatenated
```

```python
# list method example
z = x+y
z.count(4)
```

```python
# in-build sum function
sum(x)
```

```python
# in-built sort
sorted(x)
```

```python
# using functions from math
from math import pi,sqrt
r = 4
sqrt(2*pi*r)
```

## Plotting

```python
import matplotlib.pyplot as plt
import numpy as np # see next section
%matplotlib inline
```

```python
# create range of values from 0 to 2pi in steps of 0.1
x = np.arange(0,2*pi,0.1)
```

```python
# create y as sine function with x as independent variable
y = np.sin(x)
```

```python
# graph for the function y
plt.plot(x,y)
```

## Numpy

```python
# numpy, the backborne of scientific computing 
# all array related operations are defined in numpy
import numpy as np
```

```python
# create 2x3 array of 1's
x_arr = np.ones((2,3))
x_arr
```

```python
# adds a scalar value element wise
x_arr + 4
```

```python
x_arr
# to reflect change, store the values to the old array
# uncomment below two lines to see the change
#x_arr = x_arr+4
#x_arr
```

```python
y_arr = np.array([2,2,2])
y_arr
```

```python
# array broadcasting
# matches the shape and adds the y_arr row to each -
# row of x_arr
x_arr + y_arr
```

```python tags=["raises-exception"]
y_arr = np.array([5,8])
x_arr+y_arr # broadcasting fails
```

```python
# to rectifyabove error and add elements of y_arr to each column of x_arr
# change "orentation of y_arr" first
y_arr[:,np.newaxis] 
```

```python
# now you can add them
y_arr[:,np.newaxis]  + x_arr
```

## Speeding up operations with code change

```python
import random
import numba
```

```python
# create a list of 10k random elements
x = [random.random() for i in range(10000)]
y = [random.random() for i in range(10000)]
z = [] # empty list to store result
```

```python
%%time
# first, let's try good old for loop
for i in range(len(x)):
    z.append(x[i] + y[i])
print(z[:3]) # print first 3 elements
```

```python
%%time
# now list comprehension
z  = [x[i] + y[i] for i in range(len(x))]
```

```python
%%time
# using zip()
# zip() and enumerate() are useful functions
z  = [a + b for a,b in zip(x,y)]
```

```python
# create numpy arrays
xa = np.array(x)
ya = np.array(y)
```

```python
%%time
# using numpy addition
za = xa+ya
za[:3]
```

```python
# Take another example of finding sum of all elements in an array
# Below function finds sum of all elements in x
def add(x):
    total = 0
    for i in range(x.shape[0]):
        total = total+x[i]
    return total
```

```python
# array of 10 million items
x = np.random.rand(10000000)
```

```python
%%time 
add(x)
```

#### Just in time (JIT) compiler

```python
@numba.jit
def add_jit(x):
    total = 0
    for i in range(x.shape[0]):
        total = total+x[i]
    return total
```

```python
%%time
add_jit(x)
```

```python
%%time
add_jit(x) # already compiled, hence faster this time
```

```python
%%time
# numpy sum
x.sum()
```

## Remarks:
* Python is not slow per say
* the way you code matters
* stick to existing fuctions in numpy when available
* numpy functions are optimized for speed


## Further references
* example [notebook](https://nbviewer.jupyter.org/github/rabernat/intro_to_physical_oceanography/blob/master/lectures/03_air_sea_exchange.ipynb)
* https://ipython-books.github.io/
* learn more about matplotlib [plots](https://nbviewer.jupyter.org/github/jrjohansson/scientific-python-lectures/blob/master/Lecture-4-Matplotlib.ipynb)
* https://github.com/fangohr/introduction-to-python-for-computational-science-and-engineering

```python

```
