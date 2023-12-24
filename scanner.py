import math


class Scanner:
    def __init__(self,data,id_list,token_strList):
        self.data=data+" "
        self.move_list=[{'a':1,'0':2,'*':4,'-':6,'/':8,'+':9,'(':10,')':11,',':12,';':13},  #转移函数
                        {'a':1,'0':1},
                        {'0':2,'.':3},
                        {'0':3},
                        {'*':5},{},
                        {'-':7},{},
                        {'/':7},
                        {},{},{},{},{}]
        self.id_list=id_list
        self.token_strList=token_strList
        self.line_list=[]
        self.errorLine_list=[]
    def move(self,state,ch):
        if ch.isdigit():
            ch='0'
        elif ch.isalnum():
            ch='a'

        return self.move_list[state].get(ch,-1)

    def preTreat(self,ch,token_list,token_str,state,is_error,is_note,line,i_inLine,flag):  #输入字符若为回车 返回1 若为空格 返回2
        ch_flag=0
        is_continue=0
        if ch=='\n' or ch=='\f' or ch=='\v':
            ch_flag=1
        elif ch.isspace():
            ch_flag=2

        if ch_flag!=0:  #如果是空格/回车
            if flag==0:  #如果第一次遇到空格/回车 记录记号
                if ch_flag==1:
                    is_note=0

                if is_note==0:
                    is_error,state=self.record(token_list,token_str,state,is_error,line)
                    token_str=''
                    state=0
                if is_error:
                    self.reportError(state,token_str,line,i_inLine,is_error)

            is_error=0
            flag=1  #已经遇到过空格或者回车
            is_continue=1
            if ch_flag==1:
                line+=1
                i_inLine=0
        return token_str,state,is_error,is_note,line,i_inLine,flag,is_continue

    def record(self,token_list,token_str,state,is_error,line):   #记录记号
        value=0 #值
        fun=None   #函数指针
        if state==1:    #如果是ID类型记号
            check=self.id_list.get(token_str,-1)    #查符号表
            if check==-1:   #未命中
                state=0 #错误
                is_error=2
            else:
                state=check[0]
                value=check[1]
                fun=check[2]
        elif state==2 or state==3:  #如果是const_id
            value=float(token_str)

        if state==5:
            token_str='p'
        elif state==24:
            token_str=token_str[1]
        token_list.append([state,token_str,value,fun])
        self.line_list.append(line)
        return is_error,state

    def reportError(self,state,token_str,line,i_inLine,is_error):
        error=""
        if is_error==1:
            error="Illegal Input: "+token_str
        if is_error==2:
            i_inLine-=len(token_str)
            error="Misspelling: "+token_str
        if state==0:
            print("\033[0;31m"+"[line:"+str(line)+",index:"+str(i_inLine)+"]"+error+"\033[0m")

        if not line in self.errorLine_list:
            self.errorLine_list.append(line)
    @staticmethod
    def isFinish(state):
        if state==0:
            return 0
        return 1

    def getToken(self):
        token_list=[]  #字符流
        token_str=''  #记号字符串
        line=1  #当前扫描的文本行数
        i_inLine=0  #当前扫描的字符在当前行的位置
        state=0  #当前状态
        flag=1  #是否已经遇到空格或回车
        is_note=0  #是否为注释
        is_error=0  #是否非法输入
        i=0

        while i<len(self.data):
            ch=self.data[i]
            i+=1
            if is_error==0:   #当报错时，锁定i_inLine的值
                i_inLine+=1
            token_str,state,is_error,is_note,line,i_inLine,flag,is_continue=self.preTreat(ch,token_list,token_str,state,is_error,is_note,line,i_inLine,flag)
            if is_continue:
                continue

            flag=0
            token_str+=ch

            if is_error or is_note:
                continue

            next_state=self.move(state,ch)  #状态转移
            if next_state==-1:  #转移失败
                if self.isFinish(state):    #如果处于终态
                    token_str=token_str[:-1]    #回退
                    i-=1
                    i_inLine-=1
                    is_error,state=self.record(token_list,token_str,state,is_error,line)
                    if is_error:
                        self.reportError(state,token_str,line,i_inLine,is_error)
                    token_str=''
                    state=0
                    is_error=0
                    is_note=0
                else:
                    is_error=1
            else:
                state=next_state
                if state==7:
                    is_note=1
        self.record(token_list,'EOF',25,0,self.line_list[-1]+1)
        return token_list,self.line_list,self.errorLine_list
