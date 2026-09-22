import sys

if len(sys.argv) == 1:
    print("none")
else:
    print("parameters:", len(sys.argv) - 1)

    for word in sys.argv[1:]:
        print(word + ":", len(word))

# ข้อนี้ให้สร้าง count_it.py แล้วทำ 2 อย่างครับ นับว่ามี parameter กี่ตัว และบอกความยาวของแต่ละ parameter โดยโจทย์กำหนดให้ใช้ for

# python .\cell05\ex11\count_it.py "Game" "of" "Thrones"