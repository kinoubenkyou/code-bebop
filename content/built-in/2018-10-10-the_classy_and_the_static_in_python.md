Tags: python
Status: draft

There are three types of method accessible in a Python class: instance, class and static methods. Consider the following class and its instances:

```python
class Human:
    class_v = "homo sapiens"

    @classmethod
    def class_m(cls):
        print(cls.class_v)

    def __init__(self, race):
        self.instance_v = race

    def instance_m(self):
        print(self.instance_v)
        print(self.class_v)

    @staticmethod
    def static_m():
        print("human yet not human")


weeb = Human("weeaboo")
duck = Human("viet")
```

If instance methods are accessed from their instance, a bound method object is returned.

```python
print(weeb.instance_m)
# <bound method Human.instance_m of <__main__.Human object at 0x7f6cec860320>>
```

Bound methods implicitly get the bounded object passed as its first argument, and can be omitted when calling.

```python
weeb.instance_m()
# weeaboo
# homo sapiens
```

If instance methods are accessed from their class, an unbound method is returned instead.

```python
print(Human.instance_m)
# <function Human.instance_m at 0x7f6cec85f620>
```

If instance methods are called from their class, an error regarding the implicit first argument is thrown.

```python
Human.instance_m()
# TypeError: instance_m() missing 1 required positional argument: 'self'
```

Class methods, on the other hand, are bounded to a class.

```python
print(Human.class_m)
# <bound method Human.class_m of <class '__main__.Human'>>
```

Class methods can be accessed from both the instances and the class.

```python
print(weeb.class_m)
# <bound method Human.class_m of <class '__main__.Human'>>
print(duck.class_m)
# <bound method Human.class_m of <class '__main__.Human'>>
```

Therefore, they can also be called from both and return the same result.

```python
weeb.class_m()
# homo sapiens
duck.class_m()
# homo sapiens
Human.class_m()
# homo sapiens
```

Finally, static methods are not bounded to anything, yet they can be accessed from both the instances and the class, just like class methods.

```python
print(weeb.static_m)
# <function Human.static_m at 0x7f6cec85f6a8>
print(Human.static_m)
# <function Human.static_m at 0x7f6cec85f6a8>
```

Therefore, static methods can also be called from both and return the same result.

```python
weeb.static_m()
# human yet not human
Human.static_m()
# human yet not human
```

Since static methods are not bounded to anything, they cannot access both instance and class variables, and thus, have their usage is the same as global functions. Such type of method seems redundant, but is still useful for functions related to a class semantically, yet not accessing any instance or class variable.
