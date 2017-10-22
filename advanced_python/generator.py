"""
Generator is a python utility that allows you to partially execute a function and then return partial results
to a calling function. In this way the calling function handles the flow of control for the generator function. For
example if we have a loop through a list of elements we can stop the loop and then return the result back to the calling
 function, the calling function can then tell the generator to loop over one more element and so on.
"""

from . import SetupDemo, print_description

class Customer(object):
    def __init__(self, first, last, status):
        self.first = first
        self.last = last
        self.status = status
        self.send_email = None


class Generator(object):
    def powers_of_integer(self, base, max):
        power = 0
        while (base ** power) < max:
            result = (base ** power)
            yield result
            power = power + 1

    def process_customers(self, customers):
        for customer in customers:
            if customer.status == "Active":
                customer.send_email = True
            elif customer.status == "Inactive":
                customer.send_email = False
            yield customer

    def send_reminder_emails(self, customers):
        gen = self.process_customers(customers)
        for customer in gen:
            if customer.send_email:
                print "Send customer email to " + str(customer.first) + " " + str(customer.last)
            else:
                print "Dont send customer email to " + str(customer.first) + " " + str(customer.last)

class GeneratorDemo(SetupDemo):
    def __init__(self):
        super(GeneratorDemo, self).setup_demo(__file__)

    @print_description
    def powers_of_integer(self):
        generator = Generator()
        gen = generator.powers_of_integer(2, 1000)
        print "Getting the first 10 powers of 2"
        for i in range(1, 11):
            print next(gen)

    @print_description
    def send_reminder_emails(self):
        customer1 = Customer(first="Bob", last="Guy", status="Active")
        customer2 = Customer(first="Alice", last="Person", status="Active")
        customer3 = Customer(first="Claurice", last="Abadab", status="Inactive")
        customer4 = Customer(first="Jorge", last="Kalkan", status="Active")
        customer5 = Customer(first="Greg", last="Levy", status="Inactive")

        customer_list = [customer1, customer2, customer3, customer4, customer5]
        generator = Generator()
        generator.send_reminder_emails(customer_list)

if __name__ == "__main__":
    generator_demo = GeneratorDemo()
    demos_to_run = [generator_demo.powers_of_integer, generator_demo.send_reminder_emails]
    [func() for func in demos_to_run]