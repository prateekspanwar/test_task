import pandas as pd
import time

xls_file = pd.read_excel('/home/prateek/test_task/monthly_test.xls', sheet_name='Data 1', header=2)
xls_file.columns.values[1] = "Price"
# xls_file['Date'] = pd.to_datetime(xls_file['Date'])
# xls_file['Date'] = xls_file['Date'] -  pd.to_timedelta(15, unit='d')
xls_file['Date'] = xls_file['Date'].apply(lambda dt: dt.replace(day=1))
print(xls_file['Date'])
# csv_filename = self.generate_filepath('csv')
xls_file.to_csv('/home/prateek/test_task/monthly_test.csv', encoding='utf-8', index=False)