
def main():
    MathRequest=ask_user_input()
    MathRequest.get_res= Mathlib.execute(MathRequest)
    display_result(MathRequest.get_res)


class MathRequest:

    def __init__ (self, ope1, oper, ope2,):
        self.ope1 = ope1
        self.oper = oper
        self.ope2 = ope2
        self.res = None

    def get_ope1(self):
        return self.ope1

    def get_oper(self):
        return self.oper
    def get_ope2(self):
        return self.ope2
    def get_res(self):
        return self.res

    def set_res(self, value):
        self.res = value

    def to_string(self):
        raise NotImplementedError







def ask_user_input():
    # Get first operand from the user

    operand1 = ask_user_float_input("Enter the first operand: ")


    # Get the operator from the user
    operator = input("Enter an operator (add, sub, mul, div,pow,square): ")


    # Get second operand from the user
    operand2 = ask_user_float_input("Enter the second operand: ")
    return MathRequest(operator, operand1, operand2)

def ask_user_float_input(msg):
    return float(input(msg))

class Mathlib:
    def __init__(self):
        self.MathRequest = MathRequest

    def get_variable(self,MathRequest):
        ope1=MathRequest.get_ope1()
        ope2=MathRequest.get_ope2()
        oper=MathRequest.get_oper()
        return ope1,ope2,oper

    @classmethod
    def execute(self, MathRequest):
        match MathRequest.get_oper() :
            case "add":
                MathRequest.set_res(MathRequest.get_ope1() + MathRequest.get_ope2())

            case 'sub':
                MathRequest.set_res(MathRequest.get_ope1() - MathRequest.get_ope2())

            case 'mul':
                MathRequest.set_res(MathRequest.get_ope1() * MathRequest.get_ope2())

            case 'div':
                MathRequest.set_res(MathRequest.get_ope1() / MathRequest.get_ope2())

            case "pow":
                MathRequest.set_res(MathRequest.get_ope1() ** MathRequest.get_ope2())

            case "square":
                MathRequest.set_res(round(MathRequest.get_ope1() ** (1/MathRequest.get_ope2()),2))

def display_result( res):
    print(str(res))

# Call the main function to run the program
main()