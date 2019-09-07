from flask import Flask, render_template
import mlab
from models.service import Service
from models.customer import Customers 
from mongoengine import *
from random import randint
from faker import Faker
fake = Faker()
app = Flask(__name__)
mlab.connect()

# new_customer = Custommers(name = fake.name(),
# gender = randint(0,1),
# email = fake.email(),
# phone_number = fake.msisdn(),
# job = fake.job(),
# company = fake.company())
# new_customer.save()

@app.route('/customer')
def customer():
  all_customer = Customers.objects()
  return render_template('customer.html', all_customer = all_customer)

@app.route('/tenmale')
def tenmale():
  count = 1
  not_yet_contact = Customers.objects(contact = False, gender = 1)

  return render_template('ten_male.html',not_yet_contact = not_yet_contact,count = count)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<int:gender>')
def search(gender):
  all_service = Service.objects(gender=gender,address__exact = "Hà Nội")
  
  return render_template('search.html',all_service = all_service)



if __name__ == '__main__':
  app.run( debug=True)
 