# try except
try:
    my_list = [1, 2, 3]
    print(my_list[4])
except Exception as e:
    print(f"ExceptionType:{type(e)} Exception details:{e}")

print("hello world")