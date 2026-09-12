# static method are those which does not use self params


class Student:
    @staticmethod  # its a decorator
    def college():
        print("IIT Delhi")


Student.college()
