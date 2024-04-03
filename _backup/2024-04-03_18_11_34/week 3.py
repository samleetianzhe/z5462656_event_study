lst1 = ['a']

lst3 = ['b', ['a']]

lst3[1].append('c')
print(f'{lst1} and {lst3}')

var1 = 'a'
var2 = 'a'
var3 = ['a']
var4 = ['a']
if var1==var2:
    print('var1=var2')
if var1 is var2:
    print('var1 is var2')
if var3==var4:
    print('var3==var4')
if var3 is var4:
    print('var3 is var4')

name = input('Who are you?')
print('Welcome to the class,', name)

working_hours = float(input('What are your weekly working hours :'))
if working_hours <= 35:
    payments = working_hours*51.45
else:
    payments = working_hours*88.9
print(f'Your weekly payments are {payments}')

import yfinance
start = '2020-01-01'
end = None
tickers = ["QAN.AX", "WES.AX"]
for tic in tickers:
    df = yfinance.download(tic, start, end, ignore_tz=True)
    tic_base = tic.lower().split('.')[0]
    df.to_csv(f'{tic_base}_stk_prc.csv')

for i in range(0,6,5):
    print(f'i is now {i}')

letters = ["a", "b", "c", "d", "e"]
for i, x in enumerate(letters):
    print(f"letters[{i}] --> {x}")

numbers = [-2, 3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15, 10]
max_value = numbers[0]
for num in numbers:
    if num > max_value:
        max_value = num
print(f"The max value in 'numbers' is : {max_value}")

years = [2018, 2019, 2020]
months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
    ]
for year in years:
   for month in months:
       print("Year: {}, Month: {}".format(year, month))

for i in range(1, 4):
    for j in range(i, 4):
        print(i, j)

for i in range(1,4):
    for j in range(1,4):
         print(i, j)

t = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
slice_t = t[:-5]  #
print(slice_t)

dic0 = {'a': 1, 'b': 2, 'c': 3}
dic1 = dic0.update({'a': 0, 'd': 4})
print(dic0)

f_suburbs = {"Randwick": 29986, "Kensington": 15004, "Frenchs Forest": 13473, "Flemington": None}
f_suburbs.pop("Randwick","Kensington")
f_suburbs = {'Fairfield': 18081,
     'Fairfield East': 5273,
     'Fairfield Heights': 7517,
     'Fairfield West': 11575,
     'Fairlight': 5840,
     'Fiddletown': 233,
     'Five Dock': 9356,
     'Flemington': None,
     'Forest Glen': None,
     'Forest Lodge': 4583,
     'Forestville': 8329,
     'Freemans Reach': 1973,
     'Frenchs Forest': 13473,
     'Freshwater': 8866,
}
print(f_suburbs)