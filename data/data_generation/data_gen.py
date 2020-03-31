
# some functions that I threw together to generate some test data
# for the sushi database. Writes data to a csv file. Headers must be the
# same as whatever column names are in the ddl file your using or else
# youll get big errors.

import random
import string
import csv
from random import choice, randint
from random import randrange
from datetime import datetime
from datetime import timedelta

random.seed(100)  # seed for reproducability

# DATA
# ========================

USER_HEADERS = [['username', 'first_name', 'last_name', 'password', 'phone_number',
                'address', 'dob', 'date_hired',
                'manager_id', 'salary', 'specialty', 'license_number',
                'license_expiration', 'pos_logon'
                ]]

ITEM_HEADERS = [[
    'item_id', 'name', 'cost', 'type'
]]

FIRST_NAMES = [
    'Tim', 'Bob', 'Stacy', 'Chad', 'Karen', 'Jim', 'Walter',
    'Erica', 'Lucy', 'Kim', 'James', 'David', 'John', 'Mary'
               ]

LAST_NAMES = [
    'Smith', 'Nguyen', 'Goldberg', 'Baker', 'Davis', 'Cook', 'Flores',
    'Bell', 'Moore', 'Taylor', 'Rivera', 'Nelson', 'Hill', 'Price'
]

STREET_PREFIX = [
    'Main', 'Green', 'Yellow', 'Blue', 'Corn', 'Flower', 'Leaf',
    'Garden', 'Hose', 'Oak', 'Tree', 'Yam'
]

STREET_SUFFIX = [
    'Street', 'Lane', 'Road', 'Way'
]

SPECS = [
    'Sushi', 'Salads', 'Soups'
]

# id, name, cost type (three letter code)
# taken from Nori Loyola Menu
# https://www.norichicago.com/menus/edgewater-menu

ITEMS = [
    ['0', 'Edamame', '5.00', 'app'],
    ['1', 'Takoyaki', '7.50', 'app'],
    ['2', 'Gyoza', '6.50', 'app'],
    ['3', 'Age-Dashi Tofu', '6.50', 'app'],
    ['4', 'Crab Rangoon', '6.50', 'app'],
    ['5', 'Mixed Greens Salad', '6.00', 'sal'],
    ['6', 'Tuna Avocado Salad', '9.00', 'sal'],
    ['7', 'Miso Soup', '2.50', 'sop'],
    ['8', 'Tom Kha Soup', '5.95', 'sop'],
    ['9', 'Tonkotsu Ramen', '12.95', 'sop'],
    ['10', 'Shrimp Tempura', '13.95', 'ent'],
    ['11', 'Chicken Katsu', '13.95', 'ent'],
    ['12', 'Panang Curry', '14.95', 'ent'],
    ['13', 'Salmon Roll', '8.00', 'ent'],
    ['14', 'Philly Maki', '8.50', 'ent'],
    ['15', 'Spicy Tuna Maki', '9.50', 'ent'],
    ['16', 'Dragon Maki', '15.00', 'ent'],
    ['17', 'Soft Drink', '1.75', 'drk'],
    ['18', 'Thai Iced Tea', '2.50', 'drk'],
    ['19', 'Green Tea', '1.75', 'drk'] 
]

def random_date():
    start = datetime.strptime('1/1/1980', '%m/%d/%Y')
    end = datetime.strptime('1/1/2020', '%m/%d/%Y')
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    d = start + timedelta(seconds=random_second)
    return f'{d.year}-{d.month}-{d.day}'

def random_address():
    num = ''.join(str(randint(0, 9)) for _ in range(0, 3))
    return f'{num} {choice(STREET_PREFIX)} {choice(STREET_SUFFIX)}'


def make_users(num_customers=10, num_cooks=3, num_drivers=4, num_servers=4):
    users, total_users = [], sum([num_customers, num_cooks, num_drivers, num_servers])
    cust_index = num_customers -1
    cook_index = cust_index + num_cooks
    driver_index = cook_index + num_drivers
    serv_index = driver_index + num_servers
    print(cook_index, 'iiiii')
    manager = randint(num_customers, serv_index)

    # make everyone as if was a customer
    for i in range(total_users):
        new_user = []
        first, last = choice(FIRST_NAMES), choice(LAST_NAMES)
        username = f'{first}_{last}_{i}'
        password = ''.join([choice(string.ascii_letters) for i in range(7)])
        phone_num = ''.join([str(randint(0, 9)) for _ in range(10)])
        address = random_address()                    
        users.append([username, first, last, password, phone_num, address] + ['NULL'] * 8)
    
    for i in range(num_customers, serv_index+1):
        DOB, date_hire, salary = random_date(), random_date(), randint(10, 20)
        users[i][6], users[i][7], users[i][8], users[i][9] = DOB, date_hire, users[manager][0], salary
        # assign all attributes that staff must have
        if i <= cook_index:      
            users[i][10] = choice(SPECS)  # assign cook attribute
        elif i <= driver_index:
            license_number = ''.join([str(randint(0, 9)) for _ in range(5)])
            exp_date = random_date()
            users[i][11], users[i][12] = license_number, exp_date
        else:
            users[i][13] = ''.join([choice(string.ascii_letters) for i in range(7)])

    man = users.pop(manager)
    return USER_HEADERS + [man] + users
    # make sure manager is first 

# CSV File Writing

def write_csv_file(data, file_name):
    with open(file_name, 'w') as csv_out:
        writer = csv.writer(csv_out)
        for row in data:
            writer.writerow(row)
u = make_users()
write_csv_file(ITEM_HEADERS + ITEMS, './items.csv')
write_csv_file(make_users(), './users.csv')