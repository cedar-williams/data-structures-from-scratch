# Data Structures from Scratch

This project is my implementation of data structures I've learned during my degree.  I'm creating the structures from scratch for review and to solidify concepts taught in my courses.

While it's written in Python, it doesn't rely on Python's built-in data structures and their implementations.

# What is implemented
So far I have implemented:
* Deque
* Dynamic Array
* Linked List
* Stack

# Goals
* Implement the data structure's underlying logic and functionality without relying on Python's prebuilt classes
* Create the appropriate python dunder methods and iterator
* Handle edge cases
* Understand constraints and strengths of each data structure

# Testing / CI

I have created comprehensive tests with a goal of covering all behaviors, and a secondary goal of complete code coverage.

To this end, there's a testing workflow I've added to the project that runs pytest and tests for coverage.  This is triggered on pushes and pull requests.

# Getting Started
* Python version: `3.12`
* Dependencies: `pip install -r requirements.txt`
* Tests/Coverage: `pytest --cov --cov-report=term-missing`
