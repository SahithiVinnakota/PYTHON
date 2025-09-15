class A:
    def __init__(self):
        print("In a init")
    def feature_1(self):
        print("Feature 1 is working")
    def feature_2(self):
        print("Feature 2 is working")

class B(A):
    def __init__(self):
        super().__init__()
        print("in b init")
    def feature_3(self):
        print("feature 3 is working")
    def feature_4(self):
        print("feature 4 is working")

# class C(A,B):
#     def feature_5(self):
#         print("feature 5 is working")

a1=B()
a1.feature_1()
a1.feature_2()

#b1=B()
# b1.feature_3()
# b1.feature_4()
# # b1.feature_1()
# # b1.feature_2()

# c1=C()
# c1.feature_1()
