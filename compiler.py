from scanner import *
from parser import *

class Compiler:
    def __init__(self):
        self.data=''
        self.id_list={'pi':[3,3.1415926,None],'e':[3,2.71828,None],'t':[14,0,None],  #ID的符号表
                      'origin':[15,0,None],'scale':[16,0,None],'rot':[17,0,None],
                      'is':[18,0,None],'for':[19,0,None],'from':[20,0,None],
                      'to':[21,0,None],'step':[22,0,None],'draw':[23,0,None],
                      'sin':[24,0,math.sin],'cos':[24,0,math.cos],'tan':[24,0,math.tan],
                      'ln':[24,0,math.log],'exp':[24,0,math.exp],'sqrt':[24,0,math.sqrt]}
        self.token_strList=['ERROR','ID','CONST_ID','CONST_FLOAT_ID','MUL','POWER','MINUS','NOTE',  #记号含义（下标为状态的值）
                            'DIV','PLUS','L_BRACKET','R_BRACKET','COMMA','SEMICOLON','T','ORIGIN',
                            'SCALE','ROT','IS','FOR','FROM','TO','STEP','DRAW',
                            'FUNC','EOF']
        self.scanner=None
        self.parser=None
    def run(self,file_name):
        with open(file_name,"r",encoding='utf-8') as f:  #打开文本
            data=f.read()  #读取文本
        self.data=data.lower()
        self.scanner=Scanner(self.data,self.id_list,self.token_strList)
        token_list,line_list,errorLine_list=self.scanner.getToken()
        # for i in token_list:
        #     print(f"{self.token_strList[i[0]]:<15}"+f"{i[1]:<10}"+f"{str(i[2]):<10}"+f"{str(i[3]):<10}")
        idx=0
        for i in range(0,len(line_list)):
            if line_list[idx] in errorLine_list or token_list[idx][0]==Token.NOTE.value:
                del line_list[idx]
                del token_list[idx]
            else:
                idx=idx+1

        self.parser=Parser(token_list,self.token_strList,line_list)
        #self.parser.buildParseTree(['3','+','a','(','10','+','o','(','1','+','t','*','2','p','2',')','*','6',')','+','5'])
        return self.parser.getAstTree()
