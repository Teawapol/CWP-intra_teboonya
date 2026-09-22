def array_of_names(persons):
    names = []

    for first_name, last_name in persons.items():
        full_name = first_name.capitalize() + " " + last_name.capitalize()
        names.append(full_name)

    return names


persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))

# ข้อนี้ให้สร้าง your_namebook.py และสร้างฟังก์ชันชื่อ array_of_names() รับค่าเป็น dictionary ที่เก็บชื่อจริงกับนามสกุล แล้วรวมเป็นชื่อเต็ม พร้อมทำตัวอักษรแรกให้เป็นพิมพ์ใหญ่ครับ