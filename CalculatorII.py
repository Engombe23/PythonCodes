expression = input("Enter an expression: ")

def calculator(exp):
    
    x = exp.split(",")
    
    operator = x[1]

    if operator == "+":
        print(float(x[0]) + float(x[2]))
        
    elif operator == "-":
        print(float(x[0]) - float(x[2]))
        
    elif operator == "*":
        print(float(x[0]) * float(x[2]))
     
    elif operator == "/":
        print(float(x[0]) / float(x[2]))
        
    elif operator == "e":
        print(float(x[0]) ** float(x[2]))   
    
    elif operator == "%":
        print(float(x[0]) % float(x[2]))   
    
calculator(expression)