from posts.models import User
from datetime import date

users = [
    {
        'email': 'georgina@gmail.com',
        'first_name': 'Georgina',
        'last_name': 'Rodriguez',
        'password': '123456789',
        'birthdate':  date(1994, 1, 27),
        'bio': 'Hello people',
        'country': 'Argentina',
        'city': 'Buenos Aires',
    },
    {
        'email': 'ronaldo@gmail.com',
        'first_name': 'Cristiano',
        'last_name': 'Aveiro',
        'password': 'ihavemoney',
        'birthdate':  date(1984, 2, 5),
        'bio': 'i have money and you do not have',
        'country': 'Portugal',
        'city': 'Funchal',
    },
    {
        'email': 'leonardo@gmail.com',
        'first_name': 'Leonardo',
        'last_name': 'DiCaprio',
        'password': 'MYOSCAR!',
        'birthdate':  date(1974, 11, 11),
        'bio': 'Where is my second oscar',
        'country': 'Estates Unites',
        'city': 'California',
    }
]


for user in users:
    obj = User(**user)
    obj.save()
    print(obj.pk, ":", obj.email)
