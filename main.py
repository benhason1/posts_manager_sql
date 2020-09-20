from abc import ABC, abstractmethod


class Parent(ABC):
    # @abstractmethod
    def foo(self):
        print("ben")


class Child(Parent):
    def foo(self):
        print("ben")


def main():
    a = Parent()
    a.foo()


if __name__ == "__main__":
    main()
