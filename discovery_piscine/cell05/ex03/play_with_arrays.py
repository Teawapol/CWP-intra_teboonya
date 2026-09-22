original = [2, 8, 9, 48, 8, 22, -12, 2]
new_array = set()

for number in original:
    if number > 5:
        new_array.add(number + 2)

print(original)
print(new_array)

# ข้อนี้ต่อจากข้อเดิมครับ แต่เพิ่มเงื่อนไขว่า ผลลัพธ์ต้องไม่มีค่าซ้ำ โดยโจทย์ใบ้ให้ใช้ set