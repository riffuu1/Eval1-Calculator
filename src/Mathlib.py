from MathRequest import MathRequest

class Mathlib():
    def __init__(self):
        self.MathRequest = MathRequest

    def get_variable(self,MathRequest):
        op1=MathRequest.get_ope1()
        op2=MathRequest.get_ope2()
        oper=MathRequest.get_oper()
        return op1,op2,oper

    def calculator(self):
        o





