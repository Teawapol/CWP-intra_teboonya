import sys

if len(sys.argv) == 3:
    count = sys.argv[2].count(sys.argv[1])

    if count > 0:
        print(count)
    else:
        print("none")
else:
    print("none")

"""
ข้อนี้ให้สร้าง scan_it.py เพื่อรับ 2 parameters
ตัวแรก = คำที่ต้องการค้นหา
ตัวที่สอง = ข้อความที่ต้องการค้น
- ถ้าคำที่หาไม่เจอ หรือใส่ parameter ไม่ครบ 2 ตัว → แสดง none
"""

# python .\cell05\ex09\scan_it.py "the" "the quick brown fox jumps over the lazy dog"
# python .\cell05\ex09\scan_it.py
# python .\cell05\ex09\scan_it.py "cat" "the quick brown fox"