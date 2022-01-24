import pandas as pd


# extracted whole data from csv file
data = pd.read_csv('top_200_password_2020_by_country.csv')

# < 1 second

# listed all the unique country from data
list_of_country = data['country'].unique()


# this will print the all the unique country from data
i = 1
for country in list_of_country:
	print(str(i)+" "+str(country))
	i+=1


# print(data.head(20))

# data for belgium only extracted from whole data
bel_data = data.loc[data['country']=='Belgium']

# filtering the max time taken to crack password in belgium
max_time_to_crack = max(bel_data['Time_to_crack_in_seconds'])
print('Password that max time to crack at belgium in second is '+str(max_time_to_crack))
