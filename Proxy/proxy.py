"""
    Structural: (There are design patterns that focus on how classes interact with each other)
        Proxy:
            The proxy design pattern is used when we have a large
            and sensitive class that I don't want every request to be sent to, so we use the proxy design pattern
            and create a representative so that it can filter the requests and send them to our class.

        Sample => Proxy design pattern is used in ORMs
"""


class Db:
    def work(self):
        print('You are admin so you can work with database...')


class Proxy:
    _admin_password = 'admin'

    def check_admin(self, password):
        if password == self._admin_password:
            db = Db()
            db.work()
        else:
            print('You are not admin so cant work with database...')


proxy = Proxy()
proxy.check_admin('admin')  # You are admin so you can work with database...
proxy.check_admin('wrong')  # You are not admin so cant work with database...
