Tags: python

There are three types of method in Python classes: instance, class and static methods. Consider the following class and its instance:

```python
class Class:
    class_var = 0

    @classmethod
    def class_method_0(cls):
        print(cls.class_var)

    @classmethod
    def class_method_1(cls):
        print(cls.instance_var)

    def __init__(self, instance_var):
        self.instance_var = instance_var

    def instance_method(self):
        print(self.instance_var)

    def still_instance_method(not_self):
        print(not_self.instance_var)

    @staticmethod
    def static_method(arg):
        print(arg)


obj = Class(instance_var=1)

print(Class)  # <class '__main__.Class'>
print(obj)  # <__main__.Class object at 0x7f606c892550>
```

# Bounding

A method is bounded to an object when the object is passed implicitly as the first argument.

# Instance Method

When called by an instance, the method is bounded to the instance:

```python
print(obj.instance_method)  # <bound method Class.instance_method of <__main__.Class object at 0x7f606c892550>>

obj.instance_method()  # 1
```

When called by a class, the method is not bounded and the first argument is not passed implicitly:

```python
print(Class.instance_method)  # <function Class.instance_method at 0x7f606c889a60>

Class.instance_method()  # TypeError: instance_method() missing 1 required positional argument: 'self'
```

The first parameter `self` in instance methods is not a Python reversed word, which means it is just a convention. Indeed, the first parameter in instance methods can be named differently:

```python
print(obj.still_instance_method)  # <function Class.method at 0x7f606c889b70>
print(Class.still_instance_method)  # <function Class.method at 0x7f606c889b70>

Class.still_instance_method()  # TypeError: still_instance_method() missing 1 required positional argument: 'not_self'
```

# Class Method

When called by a class, the method is bounced to the class:

```python
print(Class.class_method_0)  # <bound method Class.class_method_0 of <class '__main__.Class'>>

Class.class_method_0()  # 0
```

When called by an instance, the method is bounced to the class of the instance:

```python
print(obj.class_method_0)  # <bound method Class.class_method of <class '__main__.Class'>>

obj.class_method_0()  # 0

obj.class_method_1()  # AttributeError: type object 'Class' has no attribute 'instance_var'
```

In the last statement, the error specifies `type object 'Class'` instead of `'Class' object`, which means the instance `obj`

# Static Method

Static methods are not bounded and the first argument is not passed implicitly:

```python
print(Class.static_method)  # <function Class.static_method at 0x7f606c889c80>
print(obj.static_method)  # <function Class.static_method at 0x7f606c889c80>

Class.static_method()  # TypeError: static_method_0() missing 1 required positional argument: 'arg'
obj.static_method()  # TypeError: static_method_0() missing 1 required positional argument: 'arg'
```

Since static methods are not bounded, they are not supposed to access its class or the instances. Therefore, static  methods can be put outside the class as a separated function.

One reason for them to stay inside a class is the convenience coming from classes' inheritance. When working with a subclass, instead of importing the function from the module including the superclass, the function can be called as an inherited static method directly from the subclass. 

There is also the polymorphism, which allows the function to be overrided based on the subclasses it is called from.
