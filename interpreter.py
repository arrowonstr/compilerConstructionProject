import math
import matplotlib as mpl
import matplotlib.pyplot as plt
from utlis import *
import numpy

class Interpreter:
    def __init__(self):
        self.origin_x=0
        self.origin_y=0
        self.scale_x=1
        self.scale_y=1
        self.rot=0
        self.for_start=0
        self.for_end=0
        self.for_step=0
        self.for_x=[]
        self.for_y=[]
        self.t=0
        self.operator_dic={'+':Operator.plus,'-':Operator.minus,'*':Operator.mul,'/':Operator.div,
                           'p':Operator.power,'i':Operator.sin,'o':Operator.cos,'a':Operator.tan,
                           'n':Operator.ln,'x':Operator.exp,'q':Operator.sqrt}
        self.error=0
    def calAstTree(self,parseTree):
        if parseTree is None:
            return None

        leftC=parseTree.getLeftChild()
        rightC=parseTree.getRightChild()
        if leftC or rightC:
            fn=self.operator_dic[parseTree.key[0]]
            result=fn(self.calAstTree(leftC),self.calAstTree(rightC))
            if isinstance(result,str):
                print("\033[0;31m"+result+"\033[0m")
                exit()
            else:
                return result
        else:
            if parseTree.key[0]=='t':
                return self.t
            return float(parseTree.key[0])

    def run(self,ast_list):
        plt.figure()
        ax=plt.gca()
        ax.set_aspect(1)
        for i in ast_list:
            if i[0]==Token.ORIGIN.value:
                self.t=1
                self.origin_x=self.calAstTree(i[1])
                self.origin_y=self.calAstTree(i[2])
            elif i[0]==Token.SCALE.value:
                self.t=1
                self.scale_x=self.calAstTree(i[1])
                self.scale_y=self.calAstTree(i[2])
            elif i[0]==Token.ROT.value:
                self.t=1
                self.rot=self.calAstTree(i[1])
            else:
                self.for_start=self.calAstTree(i[1])
                self.for_end=self.calAstTree(i[2])
                self.for_step=self.calAstTree(i[3])

                t_list=numpy.arange(self.for_start,self.for_end,self.for_step)
                t_list=numpy.append(t_list,self.for_end)
                for j in t_list:
                    self.t=j
                    tempx=self.calAstTree(i[4])*self.scale_x
                    tempy=self.calAstTree(i[5])*self.scale_y
                    self.for_x.append(tempx*math.cos(self.rot)+tempy*math.sin(self.rot)-self.origin_x)
                    self.for_y.append(tempy*math.cos(self.rot)-tempx*math.sin(self.rot)-self.origin_y)

                plt.plot(self.for_x,self.for_y)

                self.for_x=[]
                self.for_y=[]

        plt.show()



