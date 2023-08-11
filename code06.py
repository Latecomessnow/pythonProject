choice = input("输入1表示认真学习, 输入2表示躺平摆烂: ")
# 注意输入的是字符串类型的, 进行比较时需要和字符串类型的数字进行比较
if choice == '1':
    print("好, 认真学习毕业就能够拿好offer了~~")
elif choice == '2':
    print("摆烂, 毕业的时候是找不到工作")
else:
    print("非法输入")