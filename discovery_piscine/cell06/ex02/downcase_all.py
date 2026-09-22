import sys

def downcase_it(text):
    return text.lower()

if len(sys.argv) == 1:
    print("none")
else:
    for text in sys.argv[1:]:
        print(downcase_it(text))

# ข้อนี้ให้สร้าง downcase_all.py และต้องมีฟังก์ชันชื่อ downcase_it สำหรับแปลงข้อความเป็นตัวพิมพ์เล็ก แล้วนำฟังก์ชันนี้ไปใช้กับ parameter ทุกตัวครับ

# python .\cell06\ex02\downcase_all.py "HELLO WORLD" "I understood Arrays well!"