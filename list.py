#การแสดงต่าในlist
fruits = ["apple","banana","cherry","watermelon","blueberry"]
print(fruits[1])
#การเปลี่ยนค่าในlist
fruits[1] = "blackcurrant"
print(fruits[1])
#เปลี่ยนคำในlistหลายตำแหน่ง
fruits[1:3] = ["kiwi","mango"]
print(fruits)
#เพิ่มคำในlist
fruits.append("orange")
print(fruits)
fruits.insert(3,"grape")
print(fruits)
tropical = ["mango","pineapple","papaya"]
fruits.extend(tropical)
print(fruits)
#ลบค่าในlist
fruits.remove("watermelon")
fruits.pop(1)
#del fruits
fruits.sort(reverse=True)
print(fruits)
#ชนิกานต์ กิจประเสริฐ ม.6/14 เลขที่ 36