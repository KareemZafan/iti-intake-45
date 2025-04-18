
import pytest 

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
