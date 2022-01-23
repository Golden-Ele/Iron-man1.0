#TempConvert.py
TempStr = input("请输入带有符号的温度值: ")  
if TempStr[-1] in ['F','f']:
    C = (eval(TempStr[0:-1]) - 32)/1.8        
    print("转换后的温度是{:.2f}C".format(C))  #print()函数的格式化：{}表示槽，后续变量填充到槽中，{:.2f}表示将变量C填充到这个位置时取小数点后2位
elif TempStr[-1] in ['C','c']:                
    F = 1.8*eval(TempStr[0:-1])+32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入格式错误")

    # !       python 注意缩进！！！
    # ?       Python中使用函数的方式：函数名+（）
    # *       冒号:表示条件为True则执行冒号后语句
    # todo    print()函数的基本使用格式：  print(<拟输出字符串或者字符串变量>)   
    #         eval() 去掉参数最外侧引号并执行余下语句的函数（评估函数） 
    # ?       使用[]获取字符串中一个或多个字符：1.索引，返回字符串中单个字符 <字符串>[M]    2.切片：返回字符串中一段字符子串 <字符串>[M:N]
    # *       双引号，单引号输出字符串时没有区别。当字符串中存在单引号或双引号时，直接打印可能会出错

""" 
Python中的保留字： and  elif  import  global  as  else  in  return  except 
                  try  True  break  finally  lambda  while  False  for  not 
                  None  continue  from     or   def   if      pass   del
 """


