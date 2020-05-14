import requests
import pandas as pd
import time

class OilPrice:

    def __init__(self,url,time_period):
        self.url = url
        self.time_period = time_period
        self.timestr = time.strftime("%Y%m%d_%H%M%S")
        print('script initialized')
    
    def generate_csv_file(self):
        
        xls_filename = self.download_remote_file()
     
        # reading xls file
        try:
            xls_data = pd.read_excel(xls_filename, sheet_name='Data 1', header=2)
        except  Exception:
            print('unable to read the xls file please, check the file')

        print('data processing, please wait')
        xls_data.columns.values[1] = "Price"
        
        if self.time_period == 'monthly':
            xls_data['Date'] = xls_data['Date'].apply(lambda dt: dt.replace(day=1))

        csv_filename = self.generate_filepath('csv')
        print('file convertion started')
        xls_data.to_csv(csv_filename, encoding='utf-8', index=False)
        print('check the new generated csv file')
    def download_remote_file(self):
        # download xls file
        try:
            get_xls_file = requests.get(self.url)
        except Exception:
            print('Please re-check the url of file')

        
        # creating unique filename
        new_xls_file = self.generate_filepath('xls')
        
        # writing data in a xls file
        with open(new_xls_file, 'wb') as output:
            output.write(get_xls_file.content)

        print('xls file downloaded')
        return new_xls_file    
    
    def generate_filepath(self,filetype):
        filename = self.time_period+'/'+filetype+'/'+self.time_period+'_'+self.timestr+'.'+filetype
        return filename

if __name__ == "__main__":
    # download url of the xls file
    daily_xls_url = 'https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDd.xls'
    monthly_xls_url = 'https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDm.xls'

    data = OilPrice(monthly_xls_url,'monthly')
    data.generate_csv_file()

    data = OilPrice(daily_xls_url,'daily')
    data.generate_csv_file()