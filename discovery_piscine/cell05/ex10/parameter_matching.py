import sys

if len(sys.argv) == 2:
    word = input("What was the parameter? ")

    if word == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
else:
    print("none")

# รับ parameter 1 ตัว แล้วถามผู้ใช้ให้พิมพ์คำเพื่อเทียบกับ parameter นั้นครับ

# python .\cell05\ex10\parameter_matching.py "Hello"