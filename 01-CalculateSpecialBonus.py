# Problem 1 - Calculate Special Bonus ( https://leetcode.com/problems/calculate-special-bonus/)
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Approach 1
    # Condition 1 - Employee ID is odd
    odd_id = employees['employee_id'] % 2 == 1

    # Condition 2 - Employee's name does not start with 'M'
    name_start = ~employees['name'].str.startswith('M')

    # Combining both conditions
    bonus = odd_id & name_start

    # Employee bonus column
    employees['bonus'] = employees['salary'].where(bonus, 0)

    return employees[['employee_id', 'bonus']].sort_values(by = 'employee_id')

    # Approach 2
    result = []
    for i in range(len(employees)):
        employee_id = employees['employee_id'][i]
        name = employees['name'][i]

        if (employee_id % 2 != 0) and (name[0] != 'M'):
            result.append([employee_id, employees['salary'][i]])
        else:
            result.append([employee_id, 0])
    
    df = pd.DataFrame(result, columns = ['employee_id', 'bonus']).sort_values(by = ['employee_id'])
    return df

    # Approach 3
    employees['bonus'] = employees.apply(lambda x : x['salary'] if x['employee_id'] % 2 != 0 and not x['name'].startswith('M') else 0, axis = 1)
    
    return employees[['employee_id', 'bonus']].sort_values(by = ['employee_id'])