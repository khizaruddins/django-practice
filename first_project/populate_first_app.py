import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

# fake data population

import random
from first_app.models import AccessRecord, Webpage, Topic, User
from faker import Faker

fakegen = Faker()

topics = ['Search', 'Social', 'MarketPlace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N = 5):
    for entry in range(N):
        #  get topics for the entry
        top = add_topic()

        #  create fake data for the entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create the new webpage entry

        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # create fake access record for that web page

        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

        # create fake users

        name = fakegen.name().split(' ')
        fake_firstName = name[0]
        fake_lastName = name[1]
        fake_email = fakegen.email()
        usr = User.objects.get_or_create(first_name = fake_firstName, last_name = fake_lastName, email = fake_email)[0]

if __name__ == '__main__':
    print("population scripts!!")
    populate(20)
    print('populating complete')
