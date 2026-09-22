def average(classroom):
    total = sum(classroom.values())
    return total / len(classroom)


class_3B = {
    "marine": 18,
    "jean": 15,
    "coline": 8,
    "luc": 9
}

class_3C = {
    "quentin": 17,
    "julie": 15,
    "marc": 8,
    "stephanie": 13
}

print("Average for class 3B:", average(class_3B))
print("Average for class 3C:", average(class_3C))

# ข้อนี้ให้สร้าง help_your_professor.py และสร้างฟังก์ชันชื่อ average() เพื่อคำนวณ ค่าเฉลี่ยคะแนนใน dictionary ครับ