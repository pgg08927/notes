import datetime

print(dir(datetime))

now=datetime.datetime.today()
print(now)

birth = datetime.date(1998,12,15)
print(birth.year)
print(birth.month)
print(birth.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

# timedelta
dt=datetime.timedelta(100)
print(now+dt)

# Format date

print(birth.strftime("%A,%B %d,%Y"))
message="I was born on {:%A,%B %d,%Y}."
print(message.format(birth))


# convert string into date
marr_date="5/10/2020"
marr_date_convr=datetime.datetime.strptime(marr_date,"%d/%m/%Y")
print(marr_date_convr)
