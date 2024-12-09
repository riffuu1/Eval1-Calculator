from src.MathRequest import MathRequest



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
        if(MathRequest.get_oper() == 'add'):
            MathRequest.set_res(MathRequest.get_ope1() + MathRequest.get_ope2())
