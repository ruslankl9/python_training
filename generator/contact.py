from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys
import datetime

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + ' '*10
    return prefix + ''.join([random.choice(symbols) for i in range(random.randrange(maxlen))])

month_names = [datetime.date(2000, m, 1).strftime('%B') for m in range(1, 13)]

testdata = [Contact(first_name='', last_name='')] + \
[
    Contact(
        first_name=random_string("First Name", 10),
        middle_name=random_string("Middle Name", 20),
        last_name=random_string("Last Name", 20),
        nickname=random_string("nickname", 20),
        title=random_string("title", 20),
        company=random_string("Company", 20),
        address=random_string("Address", 20),
        home_phone_number=random_string("homephone", 10),
        mobile_phone_number=random_string("mobilephone", 10),
        work_phone_number=random_string("workphone", 10),
        fax_number=random_string("faxnumber", 10),
        email=random_string("email", 20),
        email2=random_string("email2", 20),
        email3=random_string("email3", 20),
        homepage_url=random_string("home_url", 20),
        bday=random.randrange(1, 28),
        bmonth=random.choice(month_names),
        byear=random.randrange(1900, 2016),
        aday=random.randrange(1, 28),
        amonth=random.choice(month_names),
        ayear=random.randrange(1900, 2016),
        address2=random_string("Address2", 20),
        phone_number2=random_string("phone2", 10),
        notes=random_string("notes", 100)
    )
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, 'w') as out:
    jsonpickle.set_encoder_options('json', indent=3)
    out.write(jsonpickle.encode(testdata))