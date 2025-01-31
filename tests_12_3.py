import unittest
from runner_and_tournament import Runner, Tournament  # Импортируем тестируемые классы


def skip_if_frozen(cls):
    """Декоратор для пропуска тестов, если is_frozen == True"""
    for attr_name in dir(cls):
        if attr_name.startswith("test_"):
            method = getattr(cls, attr_name)
            setattr(cls, attr_name, unittest.skipIf(cls.is_frozen, "Тесты в этом кейсе заморожены")(method))
    return cls


@skip_if_frozen
class RunnerTest(unittest.TestCase):
    is_frozen = False  # Управляет выполнением тестов

    def test_walk(self):
        """Тестируем метод walk"""
        runner = Runner("Walker")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    def test_run(self):
        """Тестируем метод run"""
        runner = Runner("Runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    def test_challenge(self):
        """Тестируем, что два объекта после разных действий имеют разные distance"""
        runner1 = Runner("Fast Runner")
        runner2 = Runner("Slow Walker")

        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)


@skip_if_frozen
class TournamentTest(unittest.TestCase):
    is_frozen = True  # Управляет выполнением тестов

    def setUp(self):
        self.runner1 = Runner("Usain", speed=10)
        self.runner2 = Runner("Andrey", speed=9)
        self.runner3 = Runner("Nick", speed=3)

    def test_first_tournament(self):
        """Тест: Усэйн против Ника"""
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        last_position = max(results.keys())
        self.assertTrue(results[last_position] == self.runner3)

    def test_second_tournament(self):
        """Тест: Андрей против Ника"""
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        last_position = max(results.keys())
        self.assertTrue(results[last_position] == self.runner3)

    def test_third_tournament(self):
        """Тест: Усэйн, Андрей и Ник"""
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        last_position = max(results.keys())
        self.assertTrue(results[last_position] == self.runner3)


if __name__ == "__main__":
    unittest.main()
