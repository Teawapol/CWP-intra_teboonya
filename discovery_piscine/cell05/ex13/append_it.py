import sys

if len(sys.argv) == 1:
    print("none")
else:
    for word in sys.argv[1:]:
        if not word.endswith("ism"):
            print(word + "ism")

# ข้อนี้ให้สร้าง append_it.py รับ parameter หลายตัว แล้วเติม "ism" ต่อท้ายทีละคำครับ
# python .\cell05\ex13\append_it.py "parallel" "egoism" "human"