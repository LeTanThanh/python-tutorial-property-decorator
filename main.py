from person import Person

# Python Property Decorator

## Introduction to the Python property decorator

"""
In the previous tutorial, you learned how to use the property class to add a property to a class.
Here's the syntax of the property class:

The following defines a Person class with two attributes name and age:

To define a getter for the age attribute, you use the property class like this:

The property accepts a getter and returns a property object.

The following creates an instance of the Person class and get the value of the age property via the instance:
"""

john = Person("John", 25)
print(john.age)

"""
Also, you can call the get_age() method of the Person object directly like this:
"""

# print(john.get_age())

"""
So to get the age of a Person object, you can use either the age property or the get_age() method.
This creates an unnecessary redundancy.

To avoid this redundancy, you can rename the get_age() method to the age() method like this:

The property() accepts a callable(age) and returns a callable.
Therefore, it is a decorator.
Therefore, you can use the @property decorator to decorator the age() method as follows:

So by using the @property decorator, you can simplify the property definition for a class.
"""
