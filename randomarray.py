
#Example 
import random

array = random.choices([1,2,3], weights = [5,1,1], k = 10)

print(array)

### Output

>>> [1, 1, 1, 1, 1, 2, 1, 3, 1, 3]

#now, let’s not specify the weights parameter and see the output

import random

array = random.choices([1,2,3], k = 10)

print(array)


### Output

>>> [2, 1, 3, 2, 1, 3, 1, 2, 2, 3]
