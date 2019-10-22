from examples.greeter import Greeter


def test_greeter():
    def consumer(*args):
        assert "Hello World!" == args[0]

    Greeter.greet(consumer=consumer)
    Greeter.greet("World", "Hello", "!", consumer)
