class Publisher(object):
    pgno = 10

    def available_pgno(cls):
        print(cls.pgno)

class Book(Publisher):
    pass
class Tape(Publisher):
    time = 8
    
    def available_time(cls):
        print(cls.time)


a = Book()
a.available_pgno()
s = Tape()
s.available_time()
