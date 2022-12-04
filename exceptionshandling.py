#excpetions = events detected during execution that inturrept the flow of a program

try :# we created a try block here to check if this code will give any trace back issue or not
    numerator = int(input("what is 1num"))
    denominator = int(input("what is 2nd num"))
    result = numerator/denominator
    print(result)
except ZeroDivisionError as e:
    print("u cant divide by 0")# here this will catch all the errors where something is divided by 0
    print(e)  # as e at the end stores the error in the variable given(here e)
except ValueError as e:
    print("only int plsss")# catches all the errors where different variable types are used 
    print(e)      
except Exception as e:
    print("went wrong")    # and it does as denominator = 0
    print(e)
else:
    print(result)
finally:
    print("this block of code will always excecute regardless of the exception")        
