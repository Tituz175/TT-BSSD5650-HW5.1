class Singleton:
    __instance = None
    __name = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def set__name(self, name):
        self.__name = name

    def get__name(self):
        return self.__name


def main():
    person_1 = Singleton()
    person_1.set__name("Tife")
    person_2 = Singleton()
    print(person_2.get__name())
    print(person_1.get__name())



if __name__ == "__main__":
    main()


