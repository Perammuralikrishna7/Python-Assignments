def func_1(*argv):
    for argv in argv:
        print(argv)
func_1("hello","welcome","to","python","programming")

def func_2(**kwargs):
    for key,value in kwargs.items():
        print("%s==%s" %(key,value))
func_2(A="hello",B="to",C="all")
