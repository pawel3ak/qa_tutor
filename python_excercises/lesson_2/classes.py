"""
Write a Person class with an instance variable, age, and a constructor that takes an integer, initialAge, as a parameter. The constructor must assign  to  after confirming the argument passed as  is not negative; if a negative argument is passed as , the constructor should set  to  and print Age is not valid, setting age to 0..
In addition, you must write the following instance methods:

    * yearPasses() should increase the  instance variable by .amIOld() should perform the following conditional actions:
        If age < 13 , print You are young..
        If age >= 13 and age < 18, print You are a teenager..
        Otherwise, print You are old..

To help you learn by example and complete this challenge, much of the code is provided for you, but you'll be writing everything in the future. The code that creates each instance of your Person class is in the main method. Don't worry if you don't understand it all quite yet!
"""


class Person:
    def __init__(self, initialAge):
        # Add some more code to run some checks on initialAge
        pass

    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        pass

    # Do some computations in here and print out the correct statement to the console
    def yearPasses(self):
        pass


# Increment the age of the person in here


def test(person_object, number_of_passed_years, expected_message, expected_age):
    for i in range(number_of_passed_years):
        person_object.yearPasses()
    if person_object.age == expected_age and person_object.amIOld() == expected_message:
        prefix = ' OK '
    else:
        prefix = '  X '
    print(
        '{prefix} got: AGE: {person_age} expected : {expected_age}, MESSAGE: {person_message} expected {expected_message}'.format(
            prefix=prefix,
            person_age=person_object.age,
            expected_age=expected_age,
            person_message=person_object.amIOld(),
            expected_message=expected_message))


if __name__ == '__main__':
    test(Person(-1), 3, "You are young.", expected_age=3)
    test(Person(10), 3, "You are teenage.", expected_age=3)
    test(Person(16), 3, "You are old.", expected_age=3)
    test(Person(18), 3, "You are old.", expected_age=3)
