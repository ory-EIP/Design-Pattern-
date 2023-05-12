from abc import ABC, abstractmethod

class Template(ABC):
    
    def __init__(self):
        pass

    @abstractmethod
    def func1(self):
        pass

    @abstractmethod
    def func2(self):
        pass

    @staticmethod
    def comm_fun(self):
        print("Run func1 and func2")

    def execute(self):
        self.comm_fun()
        self.func1()
        self.func2()


class TemplateImpl1(Template):

    def func1(self):
        print("TemplateImplementation1.func1() called")
    
    def func2(self):
        print("TemplateImplementation1.func2() called")

class TemplateImpl2(Template):
    def func1(self):
        print("TemplateImplementation1.func1() called")
    
    def func2(self):
        print("TemplateImplementation1.func2() called")