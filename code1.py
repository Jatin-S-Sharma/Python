class dog:
    attr1="Bhutia"
    attr2=12
    #the function below is method in object/classes
    def func(self):
        print("i am a ",self.attr1)
        print("i am a ",self.attr2)
browny=dog()
print(browny.attr1)
browny.func()
