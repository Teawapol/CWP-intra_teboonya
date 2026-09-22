def add_one(number):
    number = number + 1

number = 10

print(number)
add_one(number)
print(number)

"""
ข้อนี้สอนเรื่อง scope ของตัวแปร ครับ จุดสำคัญคือค่าที่แก้ในฟังก์ชันจะไม่ไปเปลี่ยนตัวแปรข้างนอก
แต่ number ข้างนอกยังเป็น 10 เหมือนเดิม เพราะ number ที่อยู่ในฟังก์ชันเป็นตัวแปรคนละ scope กับตัวแปรด้านนอกครับ
"""