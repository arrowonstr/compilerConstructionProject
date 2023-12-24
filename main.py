from compiler import *
from interpreter import *
def main():
    my_compiler=Compiler()
    ast_List=my_compiler.run('program/test8.txt')
    my_interpreter=Interpreter()
    my_interpreter.run(ast_List)


if __name__ == '__main__':
    main()
