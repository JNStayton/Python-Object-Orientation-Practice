"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """creates initial serial number"""
        self.start = start
        self.next = self.start
    
    def __repr__(self):
        """Returns a string representation of the instance"""
        return f"SerialGenerator: start = {self.start}, next = {self.next}"

    def generate(self):
        """adds 1 to the start and returns"""
        self.next += 1
        return self.next - 1

    def reset(self):
        """resets the counter to the start"""
        self.next = self.start

