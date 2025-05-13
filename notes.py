def divide(a,b):
    try:
        #try smth
        result = a /b
    except ZeroDivisionError:
        print("error can't dvide by 0")
    else: 
        print(result)

divide(10,0)