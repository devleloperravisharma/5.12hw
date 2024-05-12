numberchosen =  input("Give a number")

numbers = {
   "1" : 0,
   "2" : 0,
   "3" : 0,
   "4" : 0,
   "5" : 0,
   "6" : 0,
   "7" : 0,
   "8" : 0,
   "9" : 0,
   "0" : 0,

}

for numba in numberchosen:
    if numba in numbers:
        numbers[numba] +=1

print(numbers)

pangramnumbers = True
for valueee in numbers.values():
    if valueee == 0:
        pangramnumbers = False

if pangramnumbers:
    print("WHOOOO YOU WROTE A PANGRAM NUMBER !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
else:
    print("your stupid.")