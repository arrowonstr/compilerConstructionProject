from enum import Enum
import math
class Token(Enum):
    ERROR=0
    ID=1
    CONST_ID=2
    CONST_FLOAT_ID=3
    MUL=4
    POWER=5
    MINUS=6
    NOTE=7
    DIV=8
    PLUS=9
    L_BRACKET=10
    R_BRACKET=11
    COMMA=12
    SEMICOLON=13
    T=14
    ORIGIN=15
    SCALE=16
    ROT=17
    IS=18
    FOR=19
    FROM=20
    TO=21
    STEP=22
    DRAW=23
    FUNC=24
    EOF=25

class Operator:
    @staticmethod
    def plus(a,b):
        return a+b

    @staticmethod
    def minus(a,b):
        return a-b

    @staticmethod
    def mul(a,b):
        return a*b

    @staticmethod
    def div(a,b):
        if b==0:
            return 'Division error:divisor is 0'
        return a/b

    @staticmethod
    def power(a,b):
        return a**b

    @staticmethod
    def sin(a,b):
        return math.sin(b)

    @staticmethod
    def cos(a,b):
        return math.cos(b)

    @staticmethod
    def tan(a,b):
        return math.tan(b)

    @staticmethod
    def ln(a,b):
        if b<=0:
            return 'Logarithmic error:antilogarithm less than or equal 0'
        return math.log(b)

    @staticmethod
    def exp(a,b):
        return math.exp(b)

    @staticmethod
    def sqrt(a,b):
        if b<0:
            return 'Sqrt Error:number less than 0'
        return math.sqrt(b)
def GetSpace(num):
    space=" "
    buf=str()
    num=int(num)
    for i in range(num):
        buf+=space
    return buf

def printTree(head,height=0,to='',spacelen=10): #打印二叉树
    to=''
    if head is None:
        return
    printTree(head.rightChild,height+1,'right',spacelen)
    val=to+'"'+str(head.key[0])+'"'+to
    lenM=len(val)
    lenL=(spacelen-lenM)/2
    lenR=spacelen-lenM-lenL
    val=GetSpace(lenL)+val+GetSpace(lenR)
    print(GetSpace(height*spacelen)+val)
    printTree(head.leftChild,height+1,"left",spacelen)