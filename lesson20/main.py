import random

num = random.randint(1, 100)

print(num)

# flag = True
# while flag:
#     guess = int(input("请输入您猜测的数字:"))
#     if guess == num:
#         flag = False
#         print("猜测结束")
#     else:
#         if guess > num:
#             print("猜大了")
#         else:
#             print("猜小了")

flag = True
while flag:
    guess = int(input("请输入您猜测的数字:"))

    if guess == num:
        flag = False
        print("猜测结束")
    else:
        if guess > num:
            print("铺大了")
        else:
            print("猜小了")
