var1 = 'a'
var2 = ['a']
print(var1 == var2)

# Import the yfinance module
import yfinance
# Set the dates parameters
start = '2020-01-01'
end = None
# Download Qantas stock prices
tic = "QAN.AX" # (Q1)
df = yfinance.download(tic, start, end, ignore_tz=True) # (Q2)
print(df) # (Q3)
df.to_csv('qan_stk_prc.csv') # (Q4)
# Download Wesfarmers stock prices
tic = "WES.AX" # (W1)
df = yfinance.download(tic, start, end, ignore_tz=True) # (W2)
print(df) # (W3)
df.to_csv('wes_stk_prc.csv')

d = {
 "beauty": True,
 "truth": True,
 "red wheelbarrow": 100000,
 5: "fingers",
}
for val in d.values():
 print(val)


 def qan_tic():  # (1)
  tic = "QAN.AX"  # (2)
  print(tic)  # (3)
  return tic  # (4)
 print(tic)


 def qan_tic():  # (1)
  tic = "QAN.AX"  # (2)
  print(tic)  # (3)
  return tic  # (4)

tic = "WES.AX"  # (5)
print(tic)  # (6)
qan_tic()


def mk_csv_name(tic):  # (1)
 tic = tic.lower()  # (2)
 tic_base = tic.split('.')[0]  # (3)
 return f'{tic_base}_stk_prc.csv'  # (4)

name = mk_csv_name('QAN.AX')  # (5)
print(name)  # (6)

def get_even_numbers(numbers_list):
 return [n for n in numbers_list if n % 2 == 0]
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 22, 23, 25, 29, 30, 31]
even_numbers = get_even_numbers(lst)
print(even_numbers)

lst = [2, 3, 10, 14, 20, 21, 25, 13, 15]
squares_over_150 = [x**2 for x in lst if x**2 > 150]
print(squares_over_150)

numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]
lst = list(set(numbers))
def num_divisible_by_2(numbers_list):
 return [x for x in numbers_list if x % 2 == 0]
divisible_by_2 = num_divisible_by_2(lst)
print(divisible_by_2)

numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]
result = [x for x in set(numbers) if x % 2 == 0]
print(result)

def qan_tic(): # (1)
 tic = "QAN.AX" # (2)
 print(tic) # (3)
 return tic
qan_tic()

def qan_tic(): # (1)
 tic = "QAN.AX" # (2)
 print(tic) # (3)
 return tic # (4)
print(qan_tic)

def qan_tic(): # (1)
 print(tic) # (3)
 return tic # (4)
tic = "WES.AX" # (5)
print(tic) # (6)
qan_tic() # (7)

def qan_tic():
 tic = "QAN.AX" # <-- local # (1)
 print(tic) # (2)
 return tic
tic = "WES.AX" # <-- global
qan_tic()

def mk_csv_name(tic): # (1)
 tic = tic.lower() # (2)
 tic_base = tic.split('.')[0] # (3)
 return f'{tic_base}_stk_prc.csv' # (4)
name = mk_csv_name('QAN.AX') # (5)
print(name)

# Some data (list of tuples)
data = [
 ('a', 1),
 ('b', 2),
 ('c', 3),
 ]
# Create a dict comprehension
dic = {k:v for k, v in data}
print(f'`dic` is {dic}')
print(f'type(dic) is: {type(dic)}')
# Create a list comprehension
lst = [(k, v) for k, v in data]
print(f'`lst` is {lst}')
print(f'type(lst) is {type(lst)}')
# Create a set comprehension
st = {k for k, v in data}
print(f'`st` is {st}')
print(f'type(st) is {type(st)}')

numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]
result = [i for i in set(numbers) if i % 2 == 0]
print(result)