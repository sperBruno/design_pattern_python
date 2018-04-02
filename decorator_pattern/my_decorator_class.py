
class MyDecoratorClass:

    def __init__(self):
        print("Creating Decorator Class")
        f()

    def __call__(self, *args, **kwargs):
        print("inside Decorator Method")