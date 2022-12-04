# *args = allows you to pass multiple non-key arguments 
# **kwargs = allows you to pass multpile keyword arguments
#            * = unpacking operator

def add(*args):
  total = 0
  for i in args:
    total +=1
  print(total)
# here each argument we pass in is being added to a tuple
# you can name the tuple anything ,here args
add(1,2,3,4,5)

#kwargs :
def minus(**kwargs):
  for key,value in kwargs:
    print(value)
# here the arguments are paassed in as keyword thus keyword becomes the key and the argument becomes value thus kwargs is a dictionary
    
