#8 function
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person
musician = build_person('jimi', 'hendrix')
print(musician)

def build_person(first_name, last_name, age=''):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)
'''
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

def make_pizza(*toppings):
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
'''
def user_profile(first,last,**else_info):
	name_file = {}
	name_file['first_name'] = first
	name_file['last_name']  = last
	for k ,v in else_info.items():
		name_file[k] = v
	return name_file

user_a = user_profile('ma','yun',company = 'TaoBao',Sex = 'man')
print(user_a)
user_b = user_profile('1','2',Sex = 'man')
print(user_b)


def car_msg(manufacturer, model, **else_info):
    bas_msg = {}
    bas_msg['manufacturer'] = manufacturer
    bas_msg['model'] = model
    for k, v in else_info.items():
        bas_msg[k] = v
    return bas_msg


car = car_msg('subaru', 'outback', color='blue', tow_package=True)
print(car)