![img](https://assets.imaginablefutures.com/media/images/ALX_Logo.max-200x150.png)

> Python inheritance quizes

#### Question #0

What do these lines print?

```python
class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """
    pass

b = Base()
u = User()
print(u.id)
```

- [x] 2
- [ ] 0
- [ ] 1
- [ ] 3

#### Question #1

What do these lines print?

```python
class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """

    def __init__(self):
        self.id = 89
        super().__init__()

u = User()
print(u.id)
```

- [x] 1
- [ ] 89
- [ ] 90

#### Question #2

What do these lines print?

```python
class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """

    def __init__(self):
        super().__init__()

u = User()
print(u.id)
```

- [x] 1
- [ ] None
- [ ] 0
- [ ] 2

#### Question #3

What do these lines print?

```python
class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

for i in range(3):
    b = Base()
print(b.id)
```

- [ ] 4
- [ ] None
- [x] 3
- [ ] 2

#### Question #4

What do these lines print?

```python
class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

class User(Base):
    """ My User class """
    pass

u = User()
print(u.id)
```

- [x] 1
- [ ] None
- [ ] 0
- [ ] 2

#### Question #5

What do these lines print?

```python
class Base():
    """ My base class """

    __nb_instances = 0

    def __init__(self):
        Base.__nb_instances += 1
        self.id = Base.__nb_instances

b = Base()
print(b.id)
```

- [x] 1
- [ ] None
- [ ] 0
