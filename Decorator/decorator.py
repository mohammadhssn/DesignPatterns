"""
    Structural: (There are design patterns that focus on how classes interact with each other)
        decorator:
            The decorator design pattern allows us to add behaviors to the classes
             we have already created without having to change that class.

        decorator patterns != python decorator
"""


class Article:

    def show(self):
        print('Show All Articles...')


class Login:

    def check_login(self, username, password):
        if username == 'admin' and password == 'admin':
            return True


def outer_login(func):
    def inner_login():
        username = input('Enter Username: ')
        password = input('Enter Password: ')
        login = Login()
        result = login.check_login(username, password)
        if result:
            func()
        else:
            print('Wrong Username Or Password')

    return inner_login


@outer_login
def show_all_articles():
    article = Article()
    article.show()


show_all_articles()
