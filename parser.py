import token

from utlis import *
from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree
class Parser:
    def __init__(self,token_list,token_strList,line_list):
        self.token_list=token_list
        self.token_strList=token_strList
        self.line_list=line_list    #每个记号位于的行
        self.temp_str=''    #当前扫描的记号串
        self.temp_exp=[]    #当前记录的表达式
        self.temp_ASTList=[]    #当前的分析树
        self.idx=0  #当前扫描的记号id
        self.ast_list=[]    #所有的分析树
        self.error=0    #出错
        self.exp_list={'+':1,'-':1,'*':2,'/':2,'p':3,'i':4,'o':4,'a':4,'n':4,'x':4,'q':4,} #运算优先级
        self.line=0 #当前扫描的行
    def start(self):
        self.line=self.line_list[self.idx]
        if self.token_list[self.idx][0]==Token.ORIGIN.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.idx+=1
            self.originStatement()
        elif self.token_list[self.idx][0]==Token.SCALE.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.idx+=1
            self.scaleStatement()
        elif self.token_list[self.idx][0]==Token.ROT.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.idx+=1
            self.rotStatement()
        elif self.token_list[self.idx][0]==Token.FOR.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.idx+=1
            self.forStatement()
        else:
            self.error=-1

        if self.error!=0:
            return

        if self.token_list[self.idx][0]==Token.SEMICOLON.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.idx+=1
        else:
            self.error=Token.COMMA.value
    def originStatement(self):
        self.temp_ASTList.append(Token.ORIGIN.value)

        if self.token_list[self.idx][0]==Token.IS.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.idx+=1
        else:
            self.error=Token.IS.value
            return

        if self.token_list[self.idx][0]==Token.L_BRACKET.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.idx+=1
        else:
            self.error=Token.L_BRACKET.value
            return

        self.expression()
        if self.error!=0:
            return
        else:
            self.temp_ASTList.append(self.buildParseTree(self.temp_exp))
            self.temp_exp=[]
            
        if self.token_list[self.idx][0]==Token.COMMA.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.idx+=1
        else:
            self.error=Token.COMMA.value
            return

        self.expression()
        if self.error!=0:
            return
        else:
            self.temp_ASTList.append(self.buildParseTree(self.temp_exp))
            self.temp_exp=[]
        
        if self.token_list[self.idx][0]==Token.R_BRACKET.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.idx+=1
        else:
            self.error=Token.R_BRACKET.value
            return

    def scaleStatement(self):
        self.temp_ASTList.append(Token.SCALE.value)

        if self.token_list[self.idx][0]==Token.IS.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.idx+=1
        else:
            self.error=Token.IS.value
            return

        if self.token_list[self.idx][0]==Token.L_BRACKET.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.idx+=1
        else:
            self.error=Token.L_BRACKET.value
            return

        self.expression()
        if self.error!=0:
            return
        else:
            self.temp_ASTList.append(self.buildParseTree(self.temp_exp))
            self.temp_exp=[]

        if self.token_list[self.idx][0]==Token.COMMA.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.idx+=1
        else:
            self.error=Token.COMMA.value
            return

        self.expression()
        if self.error!=0:
            return
        else:
            self.temp_ASTList.append(self.buildParseTree(self.temp_exp))
            self.temp_exp=[]

        if self.token_list[self.idx][0]==Token.R_BRACKET.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.idx+=1
        else:
            self.error=Token.R_BRACKET.value
            return
    def rotStatement(self):
        self.temp_ASTList.append(Token.ROT.value)

        if self.token_list[self.idx][0]==Token.IS.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.idx+=1
        else:
            self.error=Token.IS.value
            return

        self.expression()
        if self.error!=0:
            return
        else:
            self.temp_ASTList.append(self.buildParseTree(self.temp_exp))
            self.temp_exp=[]

    def forStatement(self):
        self.temp_ASTList.append(Token.FOR.value)

        if self.token_list[self.idx][0]==Token.T.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.idx+=1
        else:
            self.error=Token.T.value
            return

        if self.token_list[self.idx][0]==Token.FROM.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.idx+=1
        else:
            self.error=Token.FROM.value
            return

        self.expression()
        if self.error!=0:
            return
        else:
            self.temp_ASTList.append(self.buildParseTree(self.temp_exp))
            self.temp_exp=[]

        if self.token_list[self.idx][0]==Token.TO.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.idx+=1
        else:
            self.error=Token.TO.value
            return

        self.expression()
        if self.error!=0:
            return
        else:
            self.temp_ASTList.append(self.buildParseTree(self.temp_exp))
            self.temp_exp=[]

        if self.token_list[self.idx][0]==Token.STEP.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.idx+=1
        else:
            self.error=Token.STEP.value
            return

        self.expression()
        if self.error!=0:
            return
        else:
            self.temp_ASTList.append(self.buildParseTree(self.temp_exp))
            self.temp_exp=[]

        if self.token_list[self.idx][0]==Token.DRAW.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.idx+=1
        else:
            self.error=Token.DRAW.value
            return

        if self.token_list[self.idx][0]==Token.L_BRACKET.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.idx+=1
        else:
            self.error=Token.L_BRACKET.value
            return

        self.expression()
        if self.error!=0:
            return
        else:
            self.temp_ASTList.append(self.buildParseTree(self.temp_exp))
            self.temp_exp=[]

        if self.token_list[self.idx][0]==Token.COMMA.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.idx+=1
        else:
            self.error=Token.COMMA.value
            return

        self.expression()
        if self.error!=0:
            return
        else:
            self.temp_ASTList.append(self.buildParseTree(self.temp_exp))
            self.temp_exp=[]

        if self.token_list[self.idx][0]==Token.R_BRACKET.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.idx+=1
        else:
            self.error=Token.R_BRACKET.value
            return
    def expression(self):
        self.term()
        if self.error!=0:
            return

        if self.token_list[self.idx][0]==Token.PLUS.value or self.token_list[self.idx][0]==Token.MINUS.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.temp_exp.append(self.token_list[self.idx][1])
            self.idx+=1
            self.term()
            if self.error!=0:
                return

    def term(self):
        self.factor()
        if self.error!=0:
            return

        if self.token_list[self.idx][0]==Token.MUL.value or self.token_list[self.idx][0]==Token.DIV.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.temp_exp.append(self.token_list[self.idx][1])
            self.idx+=1
            self.factor()
            if self.error!=0:
                return

    def factor(self):
        if self.token_list[self.idx][0]==Token.PLUS.value or self.token_list[self.idx][0]==Token.MINUS.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.temp_exp.append(self.token_list[self.idx][1])
            self.idx+=1
            self.factor()
            if self.error!=0:
                return
        else:
            self.component()
            if self.error!=0:
                return
    def component(self):
        self.atom()
        if self.error!=0:
            return

        if self.token_list[self.idx][0]==Token.POWER.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.temp_exp.append(self.token_list[self.idx][1])
            self.idx+=1
            self.component()
            if self.error!=0:
                return

    def atom(self):
        if self.token_list[self.idx][0]==Token.CONST_ID.value or self.token_list[self.idx][0]==Token.CONST_FLOAT_ID.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.temp_exp.append(self.token_list[self.idx][2])
            self.idx+=1
            if self.token_list[self.idx][0] in [Token.PLUS.value,Token.MINUS.value,Token.MUL.value,Token.DIV.value,Token.POWER.value]:
                self.temp_str+=self.token_list[self.idx][1]+" "
                self.temp_exp.append(self.token_list[self.idx][1])
                self.idx+=1
                self.expression()
                if self.error!=0:
                    return
        elif self.token_list[self.idx][0]==Token.T.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.temp_exp.append(self.token_list[self.idx][1])
            self.idx+=1
            if self.token_list[self.idx][0] in [Token.PLUS.value,Token.MINUS.value,Token.MUL.value,Token.DIV.value,Token.POWER.value]:
                self.temp_str+=self.token_list[self.idx][1]+" "
                self.temp_exp.append(self.token_list[self.idx][1])
                self.idx+=1
                self.expression()
                if self.error!=0:
                    return
        elif self.token_list[self.idx][0]==Token.FUNC.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.temp_exp.append(self.token_list[self.idx][1])
            self.idx+=1

            if self.token_list[self.idx][0]==Token.L_BRACKET.value:
                self.temp_str+=self.token_list[self.idx][1]+" "
                self.temp_exp.append(self.token_list[self.idx][1])
                self.idx+=1
            else:
                self.error=Token.L_BRACKET.value
                return

            self.expression()
            if self.error!=0:
                return

            if self.token_list[self.idx][0]==Token.R_BRACKET.value:
                self.temp_str+=self.token_list[self.idx][1]+" "
                self.temp_exp.append(self.token_list[self.idx][1])
                self.idx+=1
            else:
                self.error=Token.R_BRACKET.value
                return
        elif self.token_list[self.idx][0]==Token.L_BRACKET.value:
            self.temp_str+=self.token_list[self.idx][1]+" "
            self.temp_exp.append(self.token_list[self.idx][1])
            self.idx+=1

            self.expression()
            if self.error!=0:
                return

            if self.token_list[self.idx][0]==Token.R_BRACKET.value:
                self.temp_str+=self.token_list[self.idx][1]+" "
                self.temp_exp.append(self.token_list[self.idx][1])
                self.idx+=1
            else:
                self.error=Token.R_BRACKET.value
                return
        else:
            self.error=-2
            return

    def reportError(self):
        if self.error==-1:
            error='Unknown statement: '
        elif self.error==-2:
            error='Wrong expression: '
        else:
            error='Missing '+self.token_strList[self.error]+': '
        print("\033[0;31m"+"[line:"+str(self.line)+"]"+error+self.temp_str+"\033[0m")
    def buildParseTree(self,fplist):
        fplist.insert(0,"(")
        fplist.append(")")
        pStack = Stack()
        eTree = BinaryTree(['',None,0])
        currentTree = eTree
        for i in fplist:
            if i == '(':
                currentTree.setRootVal(['(',currentTree.key[1],-100])
                pStack.push(currentTree)
                currentTree.insertRight(['',currentTree,0])
                currentTree=currentTree.getRightChild()
            elif i not in ['+', '-', '*', '/', ')','i','o','a','n','x','q','p']:
                try:
                    currentTree.setRootVal([i,currentTree.key[1],100])
                    parent=currentTree.key[1]
                    currentTree = parent
                except ValueError:
                    raise ValueError("token '{}' is not a valid integer".format(i))
            elif i in ['+', '-', '*', '/','i','o','a','n','x','q','p']:
                if currentTree.key[0]=='':
                    currentTree.setRootVal([i,currentTree.key[1],self.exp_list.get(i)])
                    currentTree.insertRight(['',currentTree,0])
                else:
                    node=BinaryTree([i,None,self.exp_list.get(i)])
                    while 1:
                        if node.key[2]==currentTree.key[2]:
                            currentTree=currentTree.key[1]
                            break
                        elif node.key[2]>currentTree.key[2]:
                            if currentTree.getRightChild().key[0]=='':
                                break
                            if node.key[2]>=currentTree.getRightChild().key[2]:
                                currentTree=currentTree.getRightChild()
                            else:
                                break
                        else:
                            if currentTree.key[1].key[0]=='' or currentTree.key[1].key[1] is None:
                                currentTree=currentTree.key[1]
                                break
                            if node.key[2]<currentTree.key[1].key[2]:
                                currentTree=currentTree.key[1]
                            else:
                                currentTree=currentTree.key[1]
                                break

                    node.setRootVal([node.key[0],currentTree,node.key[2]])
                    if currentTree is None:
                        node.insertLeft(eTree)
                        node.insertRight(['',node,0])
                        eTree=node
                        currentTree=node
                    else:
                        node.insertLeft(currentTree.getRightChild())
                        node.insertRight(['',node,0])
                        currentTree.rightChild=node
                        currentTree=node

                currentTree = currentTree.getRightChild()
            elif i == ')':
                currentTree=pStack.pop()
                currentTree.setRootVal([currentTree.key[0],currentTree.key[1],100])
            else:
                raise ValueError

        eTree=self.deleteBracket(eTree,0)
        return eTree

    def deleteBracket(self,tree,flag):
        if tree is None:
            return
        if tree.key[0]=='(':
            if tree.key[1] is None: #上一层为空
                tree=tree.rightChild
                tree.setRootVal([tree.key[0],None,tree.key[2]])
            # elif flag==1: #当前为上一层树的左孩子
            #     nTree=tree.key[1]
            #     tree.rightChild.setRootVal([tree.rightChild.key[0],nTree,tree.rightChild.key[2]])
            #     tree.key[1].leftChild=tree.rightChild
            #     tree=nTree.leftChild
            # else:
            #     nTree=tree.key[1]
            #     tree.rightChild.setRootVal([tree.rightChild.key[0],nTree,tree.rightChild.key[2]])
            #     tree.key[1].rightChild=tree.rightChild
            #     tree=nTree.rightChild
            else:
                tree=tree.rightChild
        else:
            flag=-1

        if flag==-1:
            nTree=self.deleteBracket(tree.leftChild,1)
            if nTree:
                nTree.setRootVal([nTree.key[0],tree,nTree.key[2]])
            tree.leftChild=nTree
            nTree=self.deleteBracket(tree.rightChild,2)
            if nTree:
                nTree.setRootVal([nTree.key[0],tree,nTree.key[2]])
            tree.rightChild=nTree
        else:
            tree=self.deleteBracket(tree,flag)

        return tree
    def getAstTree(self):
        while self.token_list[self.idx][0]!=Token.EOF.value:
            self.start()
            if self.error==0:
                self.ast_list.append(self.temp_ASTList)
            else:
                while self.token_list[self.idx][0] not in [Token.ORIGIN.value,Token.ROT.value,Token.SCALE.value,Token.FOR.value,Token.EOF.value]:
                    self.temp_str+=self.token_list[self.idx][1]+" "
                    self.idx+=1
                self.reportError()
                self.error=0

            self.temp_str=''
            self.temp_ASTList=[]
        return self.ast_list




