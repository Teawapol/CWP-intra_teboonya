import sys

if len(sys.argv) != 2:
    print("none")
else:
    count = 0

    for letter in sys.argv[1]:
        if letter == "z":
            count += 1

    if count == 0:
        print("none")
    else:
        print("z" * count)

# ข้อนี้ให้สร้าง string_are_arrays.py รับ parameter 1 ตัว แล้วดูว่ามีตัวอักษร z ตัวเล็กกี่ตัว จากนั้นแสดง z ตามจำนวนที่เจอครับ

# python .\cell05\ex12\string_are_arrays.py "The character z is found in this string"