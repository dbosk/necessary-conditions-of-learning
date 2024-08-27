def append_element(lst=[], element=1):
    lst.append(element)
    return lst

def non_mutable(default=1):
    default += 1
    return default

class Test:
    def __init__(self, msg="Test"):
        print(f"konstruktor för Test: {msg}")
        self.__msg = msg

    def set_msg(self, msg):
        self.__msg = msg

    def __str__(self):
        return self.__msg

def test_class(default=Test()):
    print("test_class anropad")
    return default

def test_class_mod(default=Test("Test2")):
    print("test_class2 anropad")
    default.set_msg("Test2 modifiering")
    return default

def test_class_mod2(default=Test("Test3")):
    default = Test("Test4")
    return default
