


'''
import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

plt.scatter(x, y,color= 'red')
plt.show()
'''

"""
import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0 '''mean value''', 1.0 '''std dev''', 100000)

plt.hist(x, 100,color= 'red')
plt.show()
"""

'''
import numpy
import matplotlib.pyplot as plt

x = numpy.random.uniform(0.0, 5.0, 100000)

plt.hist(x, 100) # 100 is bar value 
plt.show()
'''

'''
#percentile
import numpy as np

ages = [59,45,12,26,65,7,18]

per = np.percentile(ages,50)

print(per)
'''

'''
# own variance
import numpy as np
def get_var(num_list:list):
    mean = np.mean(num_list)

    new_list = []
    for item in num_list:
        temp = mean - item
        temp *= temp
        new_list.append(temp)

    return np.mean(new_list)
    
speed = [32,111,138,28,59,77,97]
var = get_var(speed)
variance = np.var(speed)
print(f"var: {var}")
print(f"variance: {variance}")
print(f"same: {var == variance}")
'''

'''
import numpy as np
import math as m

speed = [32,111,138,28.59]

variance = np.var(speed)
standart_deviation = np.std(speed)
sqroot_standart_deviation = m.sqrt(variance)

print(f"variance: {variance}")
print(f"standart deviation: {standart_deviation}")
print(f"sqrt standart deviation: {sqroot_standart_deviation}")
print(f"same: {standart_deviation == sqroot_standart_deviation}")
'''


'''
import numpy

speed = [86,87,88,86,87,85,86]
storage = [5,5,5,5]
test = [1,2,3,4,5,6,7,8,9,10]
test2 = [1,2,3,7,1,1,1,1,1,1,1,1,16,6,7,7,7,8,9,0,999999999]

x = numpy.std(speed)
y = numpy.std(storage)
z = numpy.std(test)
w = numpy.std(test2)

print(x)
print(f"storage std: {y}")
print(f"test std: {z}")
print(f"test2 std: {w}")
'''


'''
# mean , median , mode
import numpy as np
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean = np.mean(speed)
median = np.median(speed)
mode = stats.mode(speed)

print(f"mean: {mean} median: {median} mode: {mode.count}")

'''