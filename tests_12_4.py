import unittest
import logging
from runner import Runner  # Импортируем тестируемый класс

# Настраиваем логирование
logging.basicConfig(
    level=logging.INFO,
    filename="runner_tests.log",
    filemode="w",  # Запись с заменой файла
    encoding="utf-8",
    format="%(levelname)s: %(message)s"
)


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        """Тест на создание бегуна с отрицательной скоростью"""
        try:
            runner = Runner("Walker", speed=-5)  # Некорректное значение
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)

    def test_run(self):
        """Тест на создание бегуна с некорректным типом имени"""
        try:
            runner = Runner(12345, speed=10)  # Некорректное значение
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)


if __name__ == "__main__":
    unittest.main()
