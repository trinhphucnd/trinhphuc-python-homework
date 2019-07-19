from pymongo import MongoClient
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot


mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)

db = client.get_default_database()

check=[]
customers = db['customers']
all_customers = customers.find()
for customers in all_customers:

    check.append(customers["ref"])
value_event = check.count('events')
value_ads = check.count('ads')
value_wom = check.count('wom')
total = value_event +  value_ads + value_wom 
per_event = check.count('events')/total*100
per_ads = check.count('ads')/total*100
per_wom = 100 - per_ads - per_event

labels = ["Events", "Advertisements", "Word of mouth."]
values = [per_event,per_ads,per_wom]
color = ['red','blue', 'yellow']
pyplot.pie(values,
labels=labels,
colors=color,
shadow=True)

pyplot.show()

