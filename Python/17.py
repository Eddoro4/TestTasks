import pandas as pd
import numpy as np


def fill_missing_salary(employees:pd.DataFrame):
    copy = employees.copy()
    avg = copy.groupby('department')['salary'].transform(lambda x: x.mean())
    employees = employees.transform(lambda x: x.fillna(avg))
    print(employees)
    pass

employees = pd.DataFrame({
    'department': ['sales', 'sales', 'sales', 'it', 'it'],
    'salary': [100, None, 145, 300, None],
})

print(fill_missing_salary(employees))