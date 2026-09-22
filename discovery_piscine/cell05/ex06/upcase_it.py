import sys

if len(sys.argv) == 2:
    print(sys.argv[1].upper())
else:
    print("none")

# รับ parameter แค่ 1 ตัว แล้วแปลงเป็นตัวพิมพ์ใหญ่ทั้งหมดครับ ถ้าจำนวน parameter ไม่ใช่ 1 ให้แสดง none

# python .\cell05\ex06\upcase_it.py "initiation"
# python .\cell05\ex06\upcase_it.py "hello" "world"