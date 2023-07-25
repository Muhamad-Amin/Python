""" Method resolution order """


class A:
    def show(self):
        print("ini adalah show A")


class B:
    def show(self):
        print("ini adalah show B")


class C(A, B):
    pass


object = C()
object.show()
# help(object) # untuk melihat urutan eksekusi
