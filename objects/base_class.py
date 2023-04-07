class AbstractFactory:
    def create_hero(self):
        raise NotImplementedError

    def create_monster(self):
        raise NotImplementedError
