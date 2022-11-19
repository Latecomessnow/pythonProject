'''list_info1 =[("aaa",1.71,88),("bbb",1.71,21),("ccc",1.71,99),("ddd",1.71,6)]
list_info2 =[("e",1.71,88),("ff",1.71,21),("ggg",1.71,99),("hhhh",1.71,6)]
def fun_bmi_update(  list_info1 , list_info2  ):
    list_info = list_info1 + list_info2    #将两个列表合并成一个列表
    print (list_info )
    for person_info in list_info:
        print(person_info)
        person = person_info[0]
        height  = person_info[1]
        weight  = person_info[2]
        print(person + "的身高：" + str(height) + "米 \t 体重：" + str(weight) + "千克")
        bmi=weight/(height*height)                  # 用于计算BMI指数，公式为“体重/身高的平方”
        print(person + "的BMI指数为："+str(bmi))   # 输出BMI指数
        # 判断身材是否合理
        if bmi<18.5:
            print("您的体重过轻\n")
        if bmi>=18.5 and bmi<24.9:
            print("正常范围，注意保持\n")
        if bmi>=24.9 and bmi<29.9:
            print("您的体重过重 \n")
        if bmi>=29.9:
            print("肥胖\n")
            #将list_info1,list_info2两个元素合成一个元素再进行调用
fun_bmi_update( list_info1,list_info2 )'''


'''height = input("请输入您的身高:")
weight = input("请输入您的体重:")
bmi = weight / (height * height)
print("您的bmi指数为: "+str(bmi))
if bmi < 18.5:
    print("您的体重过轻\n")
if 18.5 <= bmi < 24.9:
    print("正常范围，注意保持\n")
if 24.9 <= bmi < 29.9:
    print("您的体重过重\n")
if bmi >= 29.9:
    print("您真的太重了,该减肥了")'''


'''# BMI指数计算
height, weight = eval(input("请输入身高(米)和体重(公斤)[逗号隔开]: "))
bmi = weight / pow(height, 2)
print("BMI 数值为：{:.2f}".format(bmi))
who, nat = "", ""
if bmi < 18.5:
    who, nat = "偏瘦", "偏瘦"
elif 18.5 <= bmi < 24:
    who, nat = "正常", "正常"
elif 24 <= bmi < 25:
    who, nat = "正常", "偏胖"
elif 25 <= bmi < 28:
    who, nat = "偏胖", "偏胖"
elif 28 <= bmi < 30:
    who, nat = "偏胖", "肥胖"
else:
    who, nat = "肥胖", "肥胖"
print("BMI 指标为:国际'{0}', 国内'{1}'".format(who, nat))'''


name = str(input("请输入你的姓名："))
height = eval(input("请输入你的身高（m）:"))
weight = eval(input("请输入你的体重（kg）:"))
 
BMI = weight / pow(height, 2)
print("BMI值为：{:.2f}".format(BMI))    # {:.2f} 调用方法保留小数点后两位
if BMI < 18.5:
    print("偏瘦")
else:
    if 18.5 < BMI < 25:
        print("正常")
    else:
        if 25 < BMI < 28:
            print("偏胖")
        else:
            if 28 < BMI < 32:
                print("肥胖")
            else:
                if BMI > 32:
                    print("严重肥胖！")


