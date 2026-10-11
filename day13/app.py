import mymath
from mymath import multiply

print(mymath.add(10, 5))   # 15
print(multiply(3, 4))      # 12
print(__name__)            # "__main__" here, but "mymath" inside mymath.py when imported
