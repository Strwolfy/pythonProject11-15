import unittest
from runner_and_tournament import Runner, Tournament  # Импортируем классы Runner и Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Создание общего словаря результатов для всех тестов"""
        cls.all_results = {}

    def setUp(self):
        """Создание бегунов перед каждым тестом"""
        self.runner1 = Runner("Усэйн", speed=10)
        self.runner2 = Runner("Андрей", speed=9)
        self.runner3 = Runner("Ник", speed=3)

    @classmethod
    def tearDownClass(cls):
        """Вывод результатов всех тестов после их завершения"""
        for result in cls.all_results.values():
            print(result)

    def run_tournament_test(self, participants, expected_last_place):
        """Общий метод для тестирования турниров"""
        tournament = Tournament(90, *participants)
        results = tournament.start()

        # Сохранение результата в общий словарь
        self.__class__.all_results[len(self.__class__.all_results) + 1] = results

        # Получаем последнее место в соревнованиях
        last_position = max(results.keys())
        self.assertTrue(results[last_position] == expected_last_place)

    def test_tournament_usain_nick(self):
        """Тест: Усэйн против Ника"""
        self.run_tournament_test([self.runner1, self.runner3], self.runner3)

    def test_tournament_andrey_nick(self):
        """Тест: Андрей против Ника"""
        self.run_tournament_test([self.runner2, self.runner3], self.runner3)

    def test_tournament_usain_andrey_nick(self):
        """Тест: Усэйн, Андрей и Ник"""
        self.run_tournament_test([self.runner1, self.runner2, self.runner3], self.runner3)


if __name__ == "__main__":
    unittest.main()
