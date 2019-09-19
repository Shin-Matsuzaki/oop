class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def main():
    # インスタンス化
    bob = Person(name='Bob', age=18)
    print(bob)
    print(bob.name)
    print(bob.age)

    tom = Person(name='Tom', age=40)
    print(tom)
    print(tom.name)


if __name__ == '__main__':
    main()
