import json
from flask import Flask, render_template
import pandas as pd
from oilPrice import download_file
import glob
import os

app = Flask(__name__)

@app.route("/")
def index():
    # getting latest monthly data file for plotting the graph
    list_of_files = glob.glob('monthly/csv/*') # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)

    # read csv and convert it into dataframe
    df = pd.read_csv(latest_file)

    # converting dataframe object into list
    date_data = df['Date'].tolist()
    price_data = df['Price'].tolist()

    legend = 'Monthly Data'
    return render_template('index.html', values=price_data, labels=date_data, legend=legend)

if __name__ == "__main__":
    app.run(debug=True)