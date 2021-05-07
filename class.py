class Human:
    def __init__(self,n,o): # it is going to initialize the proprtiesof that particular class when we create an instance. self here means the class itself it is a syntax
        self.name=n
        self.occupation=o

    def do_work(self): # do_work is method and name and occupation are properties. n and o are arguments
        if self.occupation=="tennis player":
            print(self.name,"plays tennis")
        elif self.occupation=="actor":
            print(self.name,"shoots a film")
    
    def speaks(Self):
        print(Self.name,"says how are you?")

tom=Human("tom cruise","actor") # instances
tom.do_work()
tom.speaks()
maria=Human("maria","tennis player")
maria.do_work()
maria.speaks()