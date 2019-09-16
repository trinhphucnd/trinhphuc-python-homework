from models.service import Service
from models.customer import Customers
import mlab
from faker  import Faker 
from random import randint,choice
mlab.connect()

fake = Faker()
# for i in range (100):
#     print("Saving", i +1, ".........")
#     new_service = Service(name =fake.name(),
#     yob = randint(1995,2000) ,
#     gender = randint(0,1),
#     phone = fake.phone_number(),
#     address = fake.address(),
#     status = choice([True,False]))

#     new_service.save()
for i in range (10):
    print("Saving", i +1, ".........")
    new_customer = Customers(name = fake.name(),
    gender = randint(0,1),
    email = fake.email(),
    phone_number = fake.msisdn(),
    job = fake.job(),
    company = fake.company(),
    contact = choice([True,False])
    )
    new_customer.save()