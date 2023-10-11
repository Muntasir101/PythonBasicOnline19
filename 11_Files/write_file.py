try:
    file_obj = open('testfile.txt', 'w')
    fileText = file_obj.write('Demo Text')
    file_obj.close()
except Exception as e:
    print(f"ExceptionType:{type(e)} Exception details:{e}")