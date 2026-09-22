import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    print(text + "Z" * (8 - len(text)))

for text in sys.argv[1:]:
    if len(text) > 8:
        shrink(text)
    elif len(text) < 8:
        enlarge(text)
    else:
        print(text)

# ข้อนี้ให้สร้าง methods_everywhere.py และมี 2 ฟังก์ชัน คือ shrink() กับ enlarge() ครับ
# หลักการคือ text[:8] เอาแค่ 8 ตัวแรก ส่วน "Z" * (8 - len(text)) จะคำนวณว่าขาดอีกกี่ตัวถึงจะครบ 8 แล้วเติม Z เข้าไป เช่น "hello" มี 5 ตัว จึงเติม Z อีก 3 ตัว → helloZZZ ครับ

# python .\cell06\ex04\methods_everywhere.py "hello" "abcdefgh" "abcdefghijkl"