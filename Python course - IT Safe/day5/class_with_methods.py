class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __call__(self, *args, **kwargs):
        print ("something important")

    def __del__(self):
        print ("we are done")

    def __str__(self):
        return "my name is {0} my age is {1}".format(self.name, self.age)

p1 = Person("roman", 30)
print (p1)
p1()