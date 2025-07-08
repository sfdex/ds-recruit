import unittest
from src.my_greeter import MyGreeter
from unittest.mock import patch
from datetime import datetime


# 覆盖完整单元测试类的实现
class TestMyGreeter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._my_greeter = MyGreeter()

    def test_init(self):
        self.assertIsInstance(self._my_greeter, MyGreeter)

    # 测试上午
    @patch('src.my_greeter.datetime')
    def test_greeting_morning(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2025, 7, 8, 9, 0)
        self.assertEqual(self._my_greeter.greeting(), "Good morning")

    # 测试下午
    @patch('src.my_greeter.datetime')
    def test_greeting_afternoon(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2025, 7, 8, 16, 0)
        self.assertEqual(self._my_greeter.greeting(), "Good afternoon")

    # 测试晚上
    @patch('src.my_greeter.datetime')
    def test_greeting_evening(self, mock_datetime):
        mock_datetime.now.return_value = datetime(2025, 7, 8, 21, 0)
        self.assertEqual(self._my_greeter.greeting(), "Good evening")


if __name__ == '__main__':
    unittest.main()
