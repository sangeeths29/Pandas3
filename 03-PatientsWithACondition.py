# Problem 3 - Patients with a Condition ( https://leetcode.com/problems/patients-with-a-condition/)
import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    # Approach 1
    result = []
    for i in range(len(patients)):
        patient_id = patients['patient_id'][i]
        patient_name = patients['patient_name'][i]
        conditions = patients['conditions'][i]

        for condition in conditions.split():
            if condition.startswith('DIAB1'):
                result.append([patient_id, patient_name, conditions])
                break
    return pd.DataFrame(result, columns = ['patient_id', 'patient_name', 'conditions'])

    # Approach 2
    return patients[patients['conditions'].str.contains(r"(^|\s)DIAB1", regex = True)]