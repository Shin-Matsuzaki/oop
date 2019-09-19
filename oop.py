class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return f'{self.name}は{self.age}歳です'


def main():
    # インスタンス化
    bob = Person(name='Bob', age=18)
    tom = Person(name='Tom', age=30)
    # print(bob)
    # print(bob.name)
    # print(bob.age)
    print(bob.info())
    print(tom.info())


if __name__ == '__main__':
    main()
