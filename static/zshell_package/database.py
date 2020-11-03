#现在正在做一个views html 的联动
#测试
import zshell_package.shellTools as st
import re
class views_html:
    pass



def modification_start(pattern,repl):
    with open(st.TEMPLATES+'/start','r') as file_read:
        outcome = file_read.read(4096)
        result = re.sub(pattern,repl,outcome,1)
    with open(st.TEMPLATES+'/start','w') as file_write:
        file_write.write(result)


def modification_view(pattern,repl):
    with open(st.VIEWS,'r') as file_read:
        outcome = file_read.read(4096)
        result = re.sub(pattern,repl,outcome,1)
    with open(st.VIEWS,'w') as file_write:
        file_write.write(result)

def put_a_variable():
    modification_view(r'#def1!','def start(request):')
    modification_view(r'#content1_1!','print("nihao")')
    # modification_view(r'#content1_2!','def start(request):')
    # modification_view(r'#content1_3!','def start(request):')
    # modification_view(r'#content1_4!','def start(request):')
    # modification_view(r'#content1_5!','def start(request):')




if __name__ == '__main__':
    put_a_variable()

