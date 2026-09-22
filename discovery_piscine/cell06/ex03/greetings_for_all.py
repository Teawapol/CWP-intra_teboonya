def greetings(name="noble stranger"):
    if isinstance(name, str):
        print("Hello,", name + ".")
    else:
        print("Error! It was not a name.")

greetings("Alexandra")
greetings("Will")
greetings()
greetings(42)

# ข้อนี้ให้สร้าง greetings_for_all.py และสร้างฟังก์ชันชื่อ greetings() ครับ โดยมีค่าเริ่มต้นเป็น "noble stranger"
