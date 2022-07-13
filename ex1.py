"""
Methods, staticmethod and classmethod
"""



# mehodsEx.py

# below x will be used by static method
# if we do not define it, the staticmethod will generate error.
x = 20

class Add(object):
    x = 9  # class variable

    def __init__(self, x):
        self.x = x  # instance variable

    def addMethod(self, y):
        print("method:", self.x + y)

    @classmethod
    # as convention, cls must be used for classmethod, instead of self
    def addClass(self, y):  # sourcery skip: class-method-first-arg-name
        print("classmethod:", self.x + y)

    @staticmethod
    def addStatic(y):
        print("staticmethod:", x + y)



def main():
    # method
    m  = Add(x=4) # or m = Add(4)
    # for method, above x = 4, will be used for addition
    m.addMethod(10)  # method :  14

    # classmethod
    c = Add(4)
    # for class method, class variable x = 9, will be used for addition
    c.addClass(10)  # clasmethod : 19

    # for static method, x=20 (at the top of file), will be used for addition
    s = Add(4)
    s.addStatic(10)  # staticmethod : 30

if __name__ == '__main__':
    main()


#  Output:
    #  method: 14
    # classmethod: 19
    staticmethod: 30


