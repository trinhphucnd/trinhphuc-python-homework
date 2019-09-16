from flask import *
import mlab
from models.service import Service
from models.customer import Customers 
from mongoengine import *
from random import randint
from faker import Faker
fake = Faker()
app = Flask(__name__)
mlab.connect()

# new_service = Service(name = "Tú Linh",
#   yob = 1995,
#   gender = 0, # 0 = female , 1 = male
#   phone = "0123456789",
#   address = "Hà Nội",
#   status = "Khá Rảnh",
#   description = "ngoan hiền, dễ thương, lễ phép với gia đình, ...”",
#   measurements = [90,60,90])
# new_service.save()

@app.route('/customer')
def customer():
  all_customer = Customers.objects()
  return render_template('customer.html', all_customer = all_customer)

@app.route('/tenmale')
def tenmale():
  not_yet_contact = Customers.objects(contact = False, gender = 1)

  return render_template('ten_male.html',not_yet_contact = not_yet_contact)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<int:gender>')
def search(gender):
  all_service = Service.objects(gender=gender,address__exact = "Hà Nội")
  
  return render_template('search.html',all_service = all_service)


@app.route('/admin')
def admin():
  services = Service.objects()
  return render_template ('admin.html',services = services)

@app.route('/delete/<service_id>')
def delete(service_id):
  service_to_delete = Service.objects.with_id(service_id)
  if service_to_delete is None:
    return "Not Found"
  else:
    service_to_delete.delete()
    return redirect(url_for('admin'))

@app.route('/new-service', methods = ["GET","POST"])
def new_service():
  if request.method == "GET":
    return render_template('new_service.html')
  elif request.method == "POST":
    form = request.form
    name = form['name']
    yob = form['yob']
    address = form['address']
    gender = form['gender']
    new_service = Service(gender=gender , name=name, yob=yob, address=address)
    new_service.save()
    return  redirect(url_for('admin'))

@app.route('/delete-all')
def delete_all():
  all_service = Service.objects()
  all_service.delete()
  return "ok"

@app.route('/update/<service_id>',methods = ["GET","POST"])
def update(service_id):
  service_update = Service.objects.with_id(service_id)
  if request.method == "GET":
    return render_template('new_service.html')
  elif request.method == "POST":
    form = request.form
    name = form['name']
    yob = form['yob']
    address = form['address']
    gender = form['gender']
    service_update.update(set__name=name,set__yob = yob,set__address = address, set__gender = gender)
    return redirect(url_for('admin'))





@app.route('/search')
def search_():
  all_service = Service.objects()
  return render_template('search_.html',all_service = all_service)

@app.route('/detail/<service_id>')
def detail(service_id):
  service_detail = Service.objects.with_id(service_id)
  return render_template('detail.html',service = service_detail)


if __name__ == '__main__':
  app.run( debug=True)
 