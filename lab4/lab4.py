def add_method(cls):
    if hasattr(cls, "say_hello"):
        print("Method say_hello already exist \n")
    else:
        def say_hello(self):
            return "Hello!"

        setattr(cls, "say_hello", say_hello)
        print("sayHello is not exist, so I will add it for you :) \n")

    return cls

@add_method
class MyClass:
    # def say_hello(self):
    #     return "Hello!"
    pass

obj = MyClass()
print(obj.say_hello())
