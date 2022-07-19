# -*- coding:utf-8 -*-
# @Time : 2022/7/18 9:14 下午
# @Author : Bin Bin Xue
# @File : 12_regularExpression
# @Project : python_basic

'''
    12.1 正则表达式
        用于检索、替换那些符合某个规则的文本。（指定数据筛选规则）
        '.'，代替处了换行符以外的任意字符
        '\'，转义字符
        '[abcd]，匹配任意字母
        '[0-9]'，匹配任一数字
        '[\u4e00-\u9fa5]'，匹配任意一个汉子
        '[^..]'，匹配除了..以外的任意字符
        \d，匹配任意一个数字
        \D，匹配任意非数字字符
        \s，匹配任意字符
        \S，匹配任意非字符
        \w，匹配任意字母、数字或下划线
        *，匹配前一个字符0次或无限次
        +，匹配前一个字符1次或无限次
        ？，匹配前一个字符0次或无限次
        {m}，匹配前一个字符m次
        {m,n}，匹配前一个字符m到n次
        ^abc，匹配开头
        abc$，匹配结尾
        \A，匹配字符串的开始位置
        \Z，匹配字符串的结束位置
        ｜，或关系匹配
        ()，匹配分组
        ..

        12.2 re模块的应用（过滤数据）
            re.search(pattern,string) - 匹配字符串
            re.compile('') - 编译表达式，提高查询效率
            re.findall() - 遍历匹配，查询字符串中所有匹配的字符串（不重复）
            re.finditer() - 遍历匹配，迭代式
            re.split() - 字符串分割
            re.sub(pattren,repl,string,count) - 用pattern替换sting中每一个匹配的子串后返回替换后的字符串
            re.subn() - 替换并返回次数
        
        12.3 常用正则表达式
            12.3.1 常用数字表达式的校验
            (1) ^[0-9]*$ - 匹配任意个数字
            (2) ^\d{n}$ - 匹配n位数字
            (3) ^\d{n,}$ - 匹配至少n位数字
            (4) ^\d{m,n}$ - 匹配m到n的数字
            (5) ^([1-9][0-9]*)+(.[0-9]{1,2})?$ - 匹配非0开头，且最多带两位小数的数字
            (6) ^[0-9]+(.[0-9]{1,3})?$ - 匹配1-3位的小数的正实数
            (7) ^[1-9]\d*$ - 匹配非0正整数

            12.3.2 常用字符表达式的校验
            (1) 汉字匹配 - [\u4e00-\u9fa5]
            (2) 英文和数字匹配 - [^A-Za-z0-9]+$
            (3) 中文、英文、数字和某些字符的匹配 - 。。。

            12.3.3 特殊需求表达式的校验
            (1)E-mail地址(@) - ^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$
            (2)域名(baidu.com) - (?i)^([a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,}$
            (3)手机号码(前两位限制，号码位限制) - 1[3458]\\d{9}
            (4)身份证号 - (^[1-9]\d{5}(18|19|([23]\d))\d{2}((0[1-9])|(10|11|12))
                                   (([0-2][1-9])|10|20|30|31)\d{3}[0-9Xx]$)|(^[1-9]\d{5}\d
                                   {2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)\d{2}$)
            (5)邮政编码 - [1-9]\d{5}(?!\d)
            (6)首尾空白行(用于删除首尾空白) - ^|s*|\s*$



'''
import re
print('----------查看re的版本和属性+方法----------')
print(re.__version__)
print(re.__all__)

print('----------re.search()测试----------')
import re
pattern = '模块'
string = '如何学习re模块？多多实践和操作！'

match = re.search(pattern, string)
print(match.start())
print(match.end())
print(string[6:8])
print(match)

print('----------re.findall()测试----------')
string = 'abbababababbbbbabaabababababbab'
pattern = 'ab'
match = re.findall(pattern,string)
print(match)

print('----------re.finiter()测试----------')
match = re.finditer(pattern,string)
for i in match:
        print(i)
        print(i.group)
        print(i.span)

print('----------re模块分割、替换测试----------')
print(re.split('\d+','wo1men2shi3hao4peng5you'))
string = '学 无 止 境'
print(re.sub(r'\s+','-',string))

print('----------常用正则表达式测试----------')
num = re.search('^[0-9]*$','123')
print(num.group())

test = 'my name is 你好吗，how are you?'
result = re.findall('[\u4e00-\u9fa5]{1,3}',test)
print(result)

# test2 ='nontom@gmail'
# result = re.match('^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$',test2)
# print(result.group)

rest = '          好好学习，天天向上      '
result = re.sub('\s*|\s*',' ',rest)
print(result)
