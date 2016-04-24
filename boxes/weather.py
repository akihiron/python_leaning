from src import daily,weekly 

print("Daily forecast:"\
,daily.forecast())
print("Weekly forecast")
for number,outlook in \
enumerate(weekly.forecast(),1):
	print(number,outlook)





#description =report.get_description()

#print("Today'sweather:",description)

