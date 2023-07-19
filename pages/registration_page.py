

class UserPageFillForm:
    def __init__(self,
                 first_name='Ivan',
                 last_name='Ivanov',
                 email = 'ivan@co.com',
                 gender = 'Male',
                 phone = '9999999999',
                 year_birthday = '1989',
                 month_birthday = 'November',
                 day_birthday = '28',
                 subject ='Maths',
                 hobby = 'Sports',
                 picture = 'picture.jpeg',
                 address = 'Москва, ул. Тверская, дом 1',
                 state = 'NCR',
                 city = 'Delhi',
                 ):
        self.name_image = 'picture.jpeg'
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.year_birthday = year_birthday
        self.month_birthday = month_birthday
        self.day_birthday = day_birthday
        self.subject = subject
        self.hobby = hobby
        self.picture = picture
        self.phone = phone
        self.address = address
        self.state = state
        self.city = city
