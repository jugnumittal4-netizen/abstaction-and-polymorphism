from abc import ABC,abstractmethod
class abcclass(ABC):
    def print(self,x):
        print("passed value is:",x)
    @abstractmethod
    def task(self):
        print("this is abstract method")
class test_method(abcclass):
    def task(self):
        print("we are inside test_method class")
test_obj = test_method()
test_obj.task()
test_obj.print(100)

