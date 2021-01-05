
try:
    print("inside 1")
    try:
        print(1/0)
    except Exception as exc:
        print("int exc")
    else:
        print("go")
except Exception as exc:
    print("out")
else:
    print("yo")