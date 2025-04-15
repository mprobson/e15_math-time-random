import math
import time
import random

def math_examples():
  '''Using math-module functions'''
  print("### MATH module examples ### ")
  num1 = 24
  n_sq1 = math.sqrt(num1)
  print(f"the Square root of {num1} is {n_sq1:.2f}")
  print()

  #the Greatest Common Divisor
  num2 = 54
  gcd = math.gcd(num1, num2)
  print(f"the GCD of {num1} and {num2} is {gcd:.2f}")
  print()

  num3 = 2
  n_pow1 = math.pow(n_sq1,2)
  print(f"the Square of {n_sq1} is {n_pow1:.2f}")
  print(f"the Square of {n_sq1} is {n_pow1}")
  print()

  print("Some important 'constants' are: ")
  print(" PI: ", math.pi)
  print(" e: ", math.e)
  print("\n")

def time_examples():
  '''Using time-module functions'''
  print("### TIME module examples ### ")
  #printing the current time
  t0 = time.time()
  print(f"t0: {t0}")
  time.sleep(1.5) # do nothing for 5 seconds
  t1 = time.time()
  print(f"t1: {t1}")
  print(f"time between t0 and t1 : {t1-t0}")

  c_time = time.ctime()
  print(c_time)

  current = time.time()
  time_struct = time.localtime(current)
  print("time_struct:", time_struct)
  print("\nyear:", time_struct.tm_year)
  print("tm_hour:", time_struct.tm_hour)
  print("\n")

def random_examples():
  '''Using random-module functions'''
  print("### RANDOM module examples ### ")
  # random floats in a range
  for i in range(10):
    num = random.random()
    print(f"random number {i:2d} : {num:.3f} ")
  print()
  # random integers in a range
  for i in range(8):
    num = random.randint(4,13)
    print(f"random number {i:2d} : {num:2d} ")
  print()

  # setting a repeatable pattern
  random.seed(123)
  for i in range(8):
    num = random.randint(4,13)
    print(f"random number {i:2d} : {num:2d} ")
  print("\n")

def main():
  # using the math module
  math_examples()

  # using the time module
  #time_examples()

  # using the random module
  #random_examples()


if __name__ == "__main__":
    main()
