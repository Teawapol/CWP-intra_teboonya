import sys

if len(sys.argv) < 3:
    print("none")
else:
    for text in reversed(sys.argv[1:]):
        print(text)

# ข้อนี้ให้สร้าง aff_rev_params.py แล้วแสดง parameter ย้อนลำดับจากตัวสุดท้ายมาตัวแรก ทีละบรรทัด
# python .\cell05\ex08\aff_rev_params.py "Python" "piscine" "hello"