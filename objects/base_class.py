class AbstractFactory:
    def create_hero(self) -> None:
        raise NotImplementedError

    def create_monster(self) -> None:
        raise NotImplementedError
