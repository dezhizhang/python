
f = open("../text.txt", "r", encoding="utf-8")

content = f.read()
print(content.count("tom"))
f.close()








