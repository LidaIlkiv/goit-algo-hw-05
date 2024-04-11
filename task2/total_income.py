from typing import Callable
import re

def generator_numbers(text: str):    
    i = 0  
    num = r' \d+\.\d{2} '
    list_of_numbers = re.findall(num.strip(), text)
        
    for i in range(0, len(list_of_numbers)):
        list_of_numbers[i] = float(list_of_numbers[i])        
        yield list_of_numbers[i]
        i +=1
           

def sum_profit(text: str, func: Callable[[str], float]):
    sum = 0    
    gen = func(text)    
    for gen in func(text) :
        sum += gen
    return sum
    

text = """Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід,
доповнений додатковими надходженнями 27.45 і 324.00 доларів."""
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")


