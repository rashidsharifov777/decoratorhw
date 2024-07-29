from datetime import datetime
from os.path import exists

if not exists("table.txt"):
    with open("table.txt","w") as file:
        file.write(f"Function name    |   Worked time   | arguments   |   keyword arguments   | result  \n")


def logger(func):
    def inner(*args, **kwargs):
        try:
            result=func(*args, **kwargs) #5 5/0
            result_str=str(result)
        except Exception as e:
            result=e
            result_str=str(e)
        func_name=f"{func.__name__:<16}"
        worked_time=f"{datetime.now()}"
        args_str=",".join(map(str,args))  #map-> ["1","2"] -> "1,2"
        kwargs_str=",".join([f"{key}={value}" for key,value in kwargs.items()])#{"a":1,"b":2} -> [{"a",1},{"b",2}]  -> ["a=1","b=2"] "a=1,b=2"
        with open("table.txt","a") as file:
            file.write(f"{func_name}    |    {worked_time}   |  {args_str}    |   {kwargs_str}  |  {result_str} \n")
    return inner







@logger
def sum(a,b): #sum(1,[2,3,4])
    return a+b

@logger
def divide(a,b):
    return a/b


sum(1,2)
divide(a=5,b=0)