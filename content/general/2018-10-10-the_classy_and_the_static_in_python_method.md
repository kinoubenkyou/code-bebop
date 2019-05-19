Tags: python

There are three types of method accessible in a Python class: instance, class and static methods. Consider the following class and its instances:

```python
class Animal:
    head = 1
    tail = 1

    @classmethod
    def count_head(cls):
        print(cls.head)

    def __init__(self, leg):
        self.leg = leg

    def count_leg(self):
        print(self.leg)

    @staticmethod
    def count_tail(cls):
        print(cls.tail)


bird = Animal(leg=2)
dog = Animal(leg=4)
```

Instance and class methods are bounded. When called they automatically get the instance or class passed as the first argument. Thus they can access their class or instance variables respectively.

```python
Animal.count_head()  # 1
bird.count_leg()  # 2
dog.count_leg()  # 4
```

Static method is similar to class method, except it isn't bounded and cannot access the class or instance variables. However, static method use less memory as Python doesn't have to reinitialize the method.

```python
Animal.count_tail()  # TypeError: count_tail() takes exactly 1 argument (0 given)
print(Animal.count_head is Animal.count_head)  # False
print(Animal.count_tail is Animal.count_tail)  # True
```
