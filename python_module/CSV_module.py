
path='F:\Python\Google Stock Market Data - google_stock_data.csv'
#file=open(path)   also can be used
lines= [line for line in open(path)]
 #   print(line)

print(lines[1])


#removing space
print(lines[0].strip())

print(lines[0].strip().split(',')) # convert it into list

dataset=[line.strip().split(',') for line in open(path)]

print(dataset[0])
print(dataset[1])
print(type(dataset[0]))

# CSV module as abov has limited functions

import csv
from datetime import datetime

print(dir(csv))

file=open(path,
          newline='') # makes sure it will open correctly with all platforms

reader=csv.reader(file)
header=next(reader)

header=next(reader)  # first line is the header
data=[col for col in reader]  # read reaminings data
print(data[0])

# still its data is saved as string

data=[]
for col in reader:
    date=datetime.strptime(col[0],'%m/%d/%Y')
    open_price=float(col[1])
    high=float(col[2])
    low=float(col[3])
    close=float(col[4])
    volume=int(col[5])
    adj_close=float(col[6])
    data.append([date,open_price,high,low,close,volume,adj_close])

# Compute and store daily stock exchange

returns_path='F:\Python\Google_stock_return.csv'
file=open(returns_path,'w')
writer=csv.writer(file)
writer.writerow(['Date','Return'])

for i in range(len(data)-1):
    todays_row=data[i]
    todays_date=todays_row[0]
    todays_price=todays_row[-1]
    yes_row=data[i+1]
    yes_price=yes_row[-1]

    daily_return=(todays_price-yes_price)/yes_price

    formated_date=todays_date.strftime('%m/%d,%Y')
    writer.writerow([formated_date,daily_retun])

