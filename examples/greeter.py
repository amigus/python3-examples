class Greeter(object):
    @staticmethod
    def greet(entity="World", greeting="Hello", punctuation="!", consumer=print):
        consumer(f"{greeting} {entity}{punctuation}")
