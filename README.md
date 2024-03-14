# Food Lab

## Learning Goals

- Use class attributes and methods to write durable and powerful code.
- Store and access food data using class attributes and methods.
- Accomplish complex programming tasks using knowledge from previous modules.

***

## Key Vocab

- **Attribute**: variables that belong to an object.
- **Constant**: variable whose value cannot be changed.
- **Instance**: one specific working copy of a class. It is created when a
  class's `__init__` method is called.
- **Class**: a bundle of data and functionality. Can be copied and modified to
  accomplish a wide variety of programming tasks.
- **Static**: an attribute or method that cannot manipulate the class or
  instance it belongs to.
- **Exception**: an error that occurs during the execution of a program.
  Exceptions can be anticipated and handled without disrupting the execution of
  the program.

***

## Introduction

In this lab, we'll be dealing with a `Food` class. The `Food` class can produce
individual food objects / instances. Each food has a name and a price. We need our
`Food` class to be able to keep track of the food objects / instances that it creates.

```py
Food.all
# => [<__main__.Food object at 0x102961f70>, <__main__.Food object at 0x10293fd00>]
```

We need our `Food` class to be able to show us all of the names of existing food objects / instances:

```py
Food.food_names()
# => ["Flatburger", "Onion Rings", "Ice Cream", "Pizza", "Ramen"]
```

We need our `Food` class to be able to show us the average price for the existing food objects / instances:

```py
Food.average_price()
# => 7.89
```

We need our `Food` class to be able to show us the food with the highest price for the existing food objects / instances:

```py
Food.most_expensive()
# => <__main__.Food object at 0x102961f70>
```

We'll accomplish this with the use of **class attributes** and **class
methods**.

***

## Setup

1. Make sure that your current working directory (folder) contains a `Pipfile`, then run `pipenv install` in your terminal to install `pytest` and any other required packages.
2. Now that your `pipenv` virtual environment is ready to use, enter `pipenv shell` to enter the virtual environment.

## Instructions / Deliverables

Write your code in `lib/food.py` (the `food.py` file in the `lib` directory / folder)

1. Define your `Food` class such that an individual food is initialized with a
name and price.

```py
flatburger = Food("Flatburger", 7.99)

flatburger.name
# "Flatburger"

flatburger.price
# 7.99
```

2. Create a class attribute, `all` for the `Food` class. We will use this attribute to keep track of
the new `Food` instances that are created from the `Food` class. Set this
attribute equal to `[]`. Then in `__init__`, you will need to append the new `Food` instances to the list contained within the `all` class attribute for the `Food` class.

```py
Food.all
# [<__main__.Food object at 0x102961f70>, <__main__.Food object at 0x10293fd00>]
```

3. Create a class method, `food_names()` that will return a list of the names for all food objects / instances created.

```py
Food.food_names()
# => ["Flatburger", "Onion Rings", "Ice Cream", "Pizza", "Ramen"]
```

4. Create a class method, `average_price()` that will return the average price for all food objects / instances created.

```py
Food.average_price()
# => 7.89
```

## *** BONUS ***

5. Create a class method, `most_expensive()` that will return the food with the highest price for the existing food objects / instances.

```py
Food.most_expensive()
# => <__main__.Food object at 0x102961f70>
```

Hint: You can use the `max()` function where you can pass in a list as the first argument and an anonymous (`lambda`) function as the second argument to the `max()` function to get the item from the list that is the "max" depending on the criteria specified within the `lambda` function as the value to compare with the other items in the list.