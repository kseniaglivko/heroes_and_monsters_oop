import unittest
from unittest.mock import patch
from io import StringIO

from game import game
from objects.character_class import Warrior, Archer, Mage, MeleeMonster, ArcherMonster, MagicMonster
from objects.hero_class import HeroFactory
from objects.item_class import spawn_item


class TestGame(unittest.TestCase):

    def test_hero_creation(self):
        warrior = Warrior()
        archer = Archer()
        mage = Mage()

        self.assertEqual(warrior.health, 100)
        self.assertEqual(warrior.attack, 15)

        self.assertEqual(archer.health, 80)
        self.assertEqual(archer.attack, 10)

        self.assertEqual(mage.health, 60)
        self.assertEqual(mage.attack, 20)

    def test_monster_creation(self):
        melee_monster = MeleeMonster()
        archer_monster = ArcherMonster()
        magic_monster = MagicMonster()

        self.assertEqual(melee_monster.health, 30)
        self.assertEqual(melee_monster.attack, 10)

        self.assertEqual(archer_monster.health, 20)
        self.assertEqual(archer_monster.attack, 8)

        self.assertEqual(magic_monster.health, 25)
        self.assertEqual(magic_monster.attack, 12)

    def test_hero_factory(self):
        hero_factory = HeroFactory()

        warrior = hero_factory.create_hero("warrior")
        self.assertIsInstance(warrior, Warrior)

        archer = hero_factory.create_hero("archer")
        self.assertIsInstance(archer, Archer)

        mage = hero_factory.create_hero("mage")
        self.assertIsInstance(mage, Mage)

    def test_spawn_item(self):
        item = spawn_item()
        self.assertIn(item.item_type, ["bow", "sword", "spellbook", "arrows", "apple", "totem"])

    @patch('builtins.input', side_effect=['1'])
    def test_game_hero_selection(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            hero_factory = HeroFactory()
            hero = hero_factory.create_hero("warrior")
            self.assertIsInstance(hero, Warrior)

    @patch('builtins.input', side_effect=['2'])
    def test_game_hero_selection_2(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            hero_factory = HeroFactory()
            hero = hero_factory.create_hero("archer")
            self.assertIsInstance(hero, Archer)

    @patch('builtins.input', side_effect=['3'])
    def test_game_hero_selection_3(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_output:
            hero_factory = HeroFactory()
            hero = hero_factory.create_hero("mage")
            self.assertIsInstance(hero, Mage)


if __name__ == "__main__":
    unittest.main()
