class classss:
    def init(self):
        self.string= ""

    def getString(self):
        self.string= input("输入string: ")

    def printString(self):
        print(self.string.upper())

obj = classss()
obj.getString()
obj.printString()