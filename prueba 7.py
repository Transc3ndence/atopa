def rutina():
    def sub_rutina():
        global a
        print(a)
        a = 1
        return
    global a
    a = 3
    sub_rutina()
    print(a)
    return
a = 5
rutina()
print(a)