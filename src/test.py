
import pytest 
import math

 print("Hello My Team")
 
 def add(a,b):
 	return a + b
 
 def test_add_functionality():
 	assert add(4,6) == 10

# It's a change from Nada's machine

def sub(a , b):
  return a - b

def test_sub_functionality():
  assert sub(5,20) == -15
  
  
def sqrt(a):
  return math.sqrt(a); 

def test_square_root_functionality():
  assert sqrt(625) == 25
  assert sqrt(0) == 0
  assert sqrt(100) == 10
  assert sqrt(400) == 20
  
