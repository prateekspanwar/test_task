import requests
import pandas as pd
import time

# download url of the xls file
daily_xls_url = 'https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDd.xls'
monthly_xls_url = 'https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDm.xls'

def download_file(url, time_period):
    # download xls file
    get_xls_file = requests.get(url)
    
    # creating unique filename 
    timestr = time.strftime("%Y%m%d_%H%M%S")
    xls_filename = time_period+'/'+time_period+'_'+timestr+'.xls'
    
    # writing data in a xls file
    with open(xls_filename, 'wb') as output:
        output.write(get_xls_file.content)

    # converting xls to csv file
    xls_file = pd.read_excel(xls_filename, sheet_name='Data 1', header=2)
    xls_file.columns.values[1] = "Price"
    
    csv_filename = time_period+'/csv/'+time_period+'_'+timestr+'.csv'
    xls_file.to_csv(csv_filename, encoding='utf-8', index=False)

if __name__ == "__main__":
    download_file(daily_xls_url,'daily')
    download_file(monthly_xls_url,'monthly')