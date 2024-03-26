lenth = 56
width = 33
height = 30.5
x = lenth * width * height
print('volume =',x )


my_list = [ "First", "Second", "Third", "Fourth"]
print(my_list[3])

lst   =   ["a", "b", "c", "d", "e", "f"]
print(lst[2:])

lst = [1, "string", True, None, True]
print(lst.remove(True))

line = "welcome to the class"
x = line.split()
print(x)

'From firstname.surname@unsw.edu.au Mon Feb 19 10:10:15 2024'
domain_name = 'From firstname.surname@unsw.edu.au Mon Feb 19 10:10:15 2024'.split('@')[1].split()[0]
print(domain_name)

s = {1, 2, 3, 3, 3, 3}
print(s)

prc_dic = {
  '2020-01-02': 7.1600,
  '2020-01-03': 7.1900,
  '2020-01-06': 7.0000,
  '2020-01-07': 7.1000,
  '2020-01-08': 6.8600,
  '2020-01-09': 6.9500,
  '2020-01-10': 7.0000,
  }
prc_dic['2020-01-02']
print(prc_dic['2020-01-02'])

weird_case = "My fUnNy tYpEcAsE sTrInG"
weird_case_lower = weird_case.upper().lower()
print(weird_case_lower)

original_str = "hello"
centered_str_with_star = original_str.center(10, '*')
print(centered_str_with_star)

a = 5
b = True
print(f'the value of a is {a} and the value of b is {b}')

lst_a = [1]
lst_a.append(2)
print(lst_a)

str_=' some text '.strip()
print(str_)

line = "welcome to the class"
x = line.split()
print(x)

line = 'From nickname.surname@unsw.edu.au Mon Feb 19 10:10:15 2024'
domain = line.split()[1]
print(domain)
domain_name = domain.split('@')[1]
print(domain_name)

s = {1, 2, 5,3,3,9,6}
print(s)

s = set()
s.add("QAN.AX")
s.add("CBA.AX")
print(f's is {s}')

s = set()
s.add("QAN.AX")
s.add("WES.AX")
s.add("CBA.AX")
s.add("CBA.AX")
print(f"After adding objects, s is {s}")
s.remove("CBA.AX")
print(f"After removing objects, s is {s}")

s = {1, 2, 3}
print(1 in s)
print(4 in s)
print(1 not in s)
print(4 not in s)
print(4 not in s)

s = {1,2,3,4,5,6,7,8,9}
no_of_s = len(s)
print(f"The number of s is {no_of_s}")

prc_dic = {
'2020-01-02': 7.1600,
'2020-01-03': 7.1900,
'2020-01-06': 7.0000,
'2020-01-07': 7.1000,
'2020-01-08': 6.8600,
'2020-01-09': 6.9500,
'2020-01-10': 7.0000,
 }
pd = prc_dic['2020-01-02']
print(f'The stock price of the company on 2020-01-02 is {pd}')

prc_dic = {'2020-01-02': 7.1600,'2020-01-03': 7.1900,'2020-01-06': 7.0000}
prc_dic['2020-01-02'] = 1.0000
prc_dic['2020-01-07'] = 1.9999
prc_dic.pop('2020-01-02')
print(f'prc_dic after removing the stock price on 2020-01-02 is {prc_dic.pop('2020-01-02')}')

prc_dic = {'2020-01-02': 7.1600, '2020-01-03': 7.1900, '2020-01-06': 7.0000}
prc_dic['2020-01-02'] = 1.0000
prc_dic['2020-01-07'] = 1.9999
prc_dic.pop('2020-01-02')
print(f'prc_dic after removing the stock price on 2020-01-02 is {prc_dic}')

d = {'a': 1, 'b': 2,'c':3 }
d.pop('a')
print(f"After popping 'a', d is now {d}")
