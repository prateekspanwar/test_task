### requirement

- python 3.6
- virtual environment
- linux/ubuntu os

### installation instruction

open the terminal and follow the instruction

```
virtualenv -p python3.6 .env
```
```
source .env/bin/activate
```
```
pip install -r requirement.txt
```
### usage instruction

- run the script for downloading the daily and monthly oil price
```
python oilPrice.py
```
- to view the line graph for the latest monthly data file
```
python app.py
```
### features
- a single script for downloading the daily and monthly data csv file 
- a web application to view the line graph