import unittest
from runner import Runner  # Импортируем класс Runner из файла runner.py


class RunnerTest(unittest.TestCase):

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


if __name__ == "__main__":
    unittest.main()
