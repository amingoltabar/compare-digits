def compare(x):#this function returns 'yes' for integers with same first and last digits.
    count=0
    z=x #making a copy of integer
    lastdigit=x%10
    while(x!=0):#calculating the number of digits
        r_1=x%10
        count+=1
        x=int(x/10)
    while(z!=0):#finding first digit of integer
        r_2=z%10
        count-=1
        z=int(z/10)
        if count==0:
            firstdigit=r_2
    if firstdigit==lastdigit:
        return('yes')
count_1=0
for i in range(5):
    a=int(input('Enter the integer '))
    y=compare(a)
    if y=='yes':
        count_1+=1
if count_1=1:
    print('You entered',count_1,'number with same first and last digits.' )
elif count_1=0:
    print('You entered',count_1,'number with same first and last digits.' )
else:
    print('You entered',count_1,'numbers with same first and last digits.' )
