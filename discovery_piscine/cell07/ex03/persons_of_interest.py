def famous_births(persons):
    sorted_people = sorted(
        persons.values(),
        key=lambda person: int(person["date_of_birth"])
    )

    for person in sorted_people:
        print(
            person["name"],
            "is a great scientist born in",
            person["date_of_birth"] + "."
        )


women_scientists = {
    "ada": {
        "name": "Ada Lovelace",
        "date_of_birth": "1815"
    },
    "cecilia": {
        "name": "Cecila Payne",
        "date_of_birth": "1900"
    },
    "lise": {
        "name": "Lise Meitner",
        "date_of_birth": "1878"
    },
    "grace": {
        "name": "Grace Hopper",
        "date_of_birth": "1906"
    }
}

famous_births(women_scientists)

# ให้สร้าง persons_of_interest.py ใน ex03 มีฟังก์ชัน famous_births() รับ dictionary แล้วเรียงคนตามปีเกิด ก่อนแสดงชื่อกับปีเกิดออกมา