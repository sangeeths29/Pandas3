# Problem 2 - Fix Names in a Table ( https://leetcode.com/problems/fix-names-in-a-table/ )
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    # Approach 1
    users['name'] = users['name'].str[0].str.upper() + users['name'].str[1:].str.lower()
    return users.sort_values(by = ['user_id'])

    # Approach 2
    users['name'] = users['name'].str.capitalize()
    return users.sort_values(by = ['user_id'])