try:
    file_obj = open('testfile2.txt', 'r')
    fileText = file_obj.read()
    print(fileText)
    file_obj.close()
except Exception as e:
    print(f"ExceptionType:{type(e)} Exception details:{e}")
