import pandas as pd
import re

score_list = pd.read_csv(r'Z:\Temp\信号与系统\NetID.csv')

student_id = score_list.iloc[:, 1]
score = score_list.iloc[:, 2:]

redact = re.compile(r'^\d{5}')
student_id_redacted = student_id.astype('str').str.slice_replace(1, 5, '*****')

print(f'{student_id_redacted.shape}')
print(student_id_redacted.nunique())

hide_name = pd.concat([student_id_redacted, score], axis=1)
hide_name.to_csv(r'score.csv', index=False)
