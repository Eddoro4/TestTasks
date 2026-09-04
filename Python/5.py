import pandas as pd
import numpy as np

def second_highest_salary(employees:pd.DataFrame):
    salaries = {}
    for departament,salary in zip(employees['department'],employees['salary']):
        salaries.setdefault(departament,set()).add(salary)
    result = {
        'department': [],
        'salary': []
        }
    for dep in salaries:
        if len(salaries[dep]) < 2:
            continue
        else:
            salary = sorted( list(salaries[dep]),reverse=True )[1]
            result['department'].append(dep)
            result['salary'].append(salary)
    return pd.DataFrame(result).sort_values(by='department')
    pass

employees = pd.DataFrame({
    'department': ['sales', 'sales', 'sales', 'it', 'it', 'hr'],
    'name': ['ann', 'bob', 'kate', 'dan', 'eve', 'fred'],
    'salary': [100, 100, 80, 300, 250, 50],
})

print(second_highest_salary(employees))