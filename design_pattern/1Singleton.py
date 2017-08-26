# coding:utf-8

class Singleton(object):
    '''
    单例模式
    '''
    class _A(object):
        '''
        真正干活的类，对外隐藏
        '''
        def __init__(self):
            pass
        def display(self):
            return id(self)

    # 类变量 用于存储_A的实例

    _instance = None

    def __init__(self):
        if Singleton._instance is None:
           # self._instance = self._A()
           Singleton._instance = Singleton._A()
    def __getattr__(self, item):
        return getattr(self._instance,item)


if __name__ =='__main__':
    s1 = Singleton();
    s2 = Singleton()
    print(id(s1),s1._instance.display())
    print(id(s2),s2._instance.display())