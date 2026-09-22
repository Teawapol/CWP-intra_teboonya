import sys

if len(sys.argv) == 3:
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    numbers = list(range(start, end + 1))
    print(numbers)
else:
    print("none")

# ข้อนี้ให้สร้าง free_range.py รับ ตัวเลข 2 ตัว แล้วสร้าง array ตั้งแต่เลขตัวแรกไปจนถึงเลขตัวที่สอง รวมเลขปลายทางด้วยครับ

# python .\cell05\ex14\free_range.py 10 14