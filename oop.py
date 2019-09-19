class Person:
    def __init__(self, name):
        self.name = name


def main():
    # インスタンス化
    bob = Person(name='Bob')
    print(bob)
    print(bob.name)


if __name__ == '__main__':
    main()