from datetime import datetime


# MyGreeter类的实现
class MyGreeter:
    def __init__(self):
        pass  # 不需要初始化属性

    def greeting(self):
        hour = datetime.now().hour
        if 6 <= hour < 12:  # 上午
            return "Good morning"
        elif 12 <= hour < 18:  # 下午
            return "Good afternoon"
        else:  # 晚上
            return "Good evening"


if __name__ == '__main__':
    greeter = MyGreeter()
    greeting = greeter.greeting()
    print(greeting)
