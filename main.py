import math
import re

def conv(number):
    direct = ""
    inverse = ""
    additional = ""
    if (number<0):
        label='false'
        number*=(-1)
    else:
        label='true'
    while(int(number)>=1):
        direct+=str(number%2)
        number=number//2
    for m in range(len(direct),7):
        direct+='0'
    if (label=='true'):
        direct+='0'
    else:
        direct+='1'
    if (label=='false'):
        for i in range(0,len(direct)-1):
            if (direct[i]=='0'):
                inverse+='1'
            elif (direct[i]=='1'):
                inverse+='0'
        inverse+='1'
    else:
        inverse=direct
    dop=1
    if (label=='false'):
        inv=inverse[::-1]
        inv=inv[1:]
        additional=sum(inv,'1')[::-1]
        additional+='1'
    else:
        additional=inverse
    return "direct code "+direct[::-1], "inverse code "+inverse[::-1], "additional code "+additional[::-1]

def sum(number1, number2):
    final=""
    number2=number2[::-1]
    number1=number1[::-1]
    if len(number1)>len(number2):
        max=len(number1)
        min=len(number2)
    else:
        max=len(number2)
        min=len(number1)
    dop=0
    for m in range(0,min):
        temp=int(number1[m])+int(number2[m])+dop
        if (temp==3):
            dop=1
            final+='1'
        elif (temp==2):
            dop=1
            final+='0'
        elif (temp==1):
            dop=0
            final+='1'
        elif (temp==0):
            dop=0
            final+='0'
    if max==len(number1):
        for m in range(min,max+1):
            if (m==max)&(dop==1):
                temp=1
            elif (m!=max):
                temp=dop+int(number1[m])
            elif (m==max)&(dop==0):
                temp=3
            if (temp==2):
                dop=1
                final+='0'
            elif (temp==1):
                dop=0
                final+='1'
            elif (temp==0):
                dop=0
                final+='0'
    else:
        for m in range(min,max+1):
            if (m==max)&(dop==1):
                temp=1
            elif (m!=max):
                temp=dop+int(number2[m])
            elif (m==max)&(dop==0):
                temp=3
            if (temp==2):
                dop=1
                final+='0'
            elif (temp==1):
                dop=0
                final+='1'
            elif (temp==0):
                dop=0
                final+='0'
    return final[::-1]

def sub(a,b):
    final=""
    number1=a[::-1]
    number2=b[::-1]
    dop=0
    for m in range(0,len(number1)):
        temp=int(number1[m])-int(number2[m])+dop
        if (temp==0):
            final+='0'
            dop=0
        elif (temp==1):
            final+='1'
            dop=0
        elif(temp==-1):
            final+='1'
            dop=-1
        elif (temp==-2):
            final+='0'
            dop=-1
    return final[::-1]

def mul(number1, number2):
    final=""
    stolbik=""
    schet=0
    for a in range (len(number2)-1,-1,-1):
        for r in range(0,schet):
            stolbik+='0'
        for b in range (len(number1)-1,-1,-1):
            rez = str(int(number1[b])&int(number2[a]))
            stolbik += rez
        stolbik=stolbik[::-1]
        final = sum(final,stolbik)
        stolbik=""
        schet+=1
    if ((number1[0]=='1')&(number2[0]=='0'))|((number1[0]=='0')&(number2[0]=='1')):
        final=final[::-1]
        final+='1'
        final=final[::-1]
    else:
        final=final[::-1]
        final+='0'
        final=final[::-1]
    return final

def div(number1, number2):
    final=""
    label1="true"
    label2="true"
    if (number1[0]=='1'):
        label1="false"
        number1=number1[1:]
    if (number2[0]=='1'):
        label2="false"
        number2=number1[1:]
    i=0
    while (number2[i]!='1')&(i<len(number2)):
        number2=number2[1:]
    if (compare(number1,number2)==(number1,number2)):
        final+='00000001'
        return final
    elif (compare(number1,number2)==number1):
        temp=""
        for j in range (0,len(number1)):
            temp+=number1[j]
            if (compare(temp,number2)==temp)|(compare(temp,number2)==(temp,number2)):
                final+='1'
                ch=number2
                if len(ch)<len(temp):
                    while (len(ch)<len(temp)):
                        ch=ch[::-1]
                        ch+='0'
                        ch=ch[::-1]
                if len(temp)<len(ch):
                    while (len(temp)<len(ch)):
                        temp=temp[::-1]
                        temp+='0'
                        temp=temp[::-1]
                temp=sub(temp,ch)
            elif (compare(temp,number2)==number2):
                final+='0'
    elif (compare(number1,number2)==number2):
        final+='0'
        temp=number1
    final+='.'
    for v in range (0,5):
        temp+='0'
        t=0
        while (temp[t]!='1')&(t<len(temp)-1):
            temp=temp[1:]
        if (temp=="0"):
            break
        if (compare(temp,number2)==temp)|(compare(temp,number2)==(temp,number2)):
                final+='1'
                ch=number2
                if len(ch)<len(temp):
                    while (len(ch)<len(temp)):
                        ch=ch[::-1]
                        ch+='0'
                        ch=ch[::-1]
                if len(temp)<len(ch):
                    while (len(temp)<len(ch)):
                        temp=temp[::-1]
                        temp+='0'
                        temp=temp[::-1]
                temp=sub(temp,ch)
        elif (compare(temp,number2)==number2):
            final+='0'
    if ((label1=="false")&(label2=="true"))|((label1=="true")&(label2=="false")):
        final=final[1:]
        final=final[::-1]
        final+='1'
        final=final[::-1]
    if final[len(final)-1]=='.':
        final=final[:-1]
    return final

def compare(a,b):
    number1=a
    number2=b
    if (len(number1)>len(number2)):
        while (len(number1)!=len(number2)):
            number2=number2[::-1]
            number2+='0'
            number2=number2[::-1]
    elif (len(number2)>len(number1)):
        while (len(number2)!=len(number1)):
            number1=number1[::-1]
            number1+='0'
            number1=number1[::-1]
    if (len(number1)==len(number2)):
        for i in range(0,len(number1)):
            if (number1[i]=='1')&(number2[i]=='0'):
                return a
            if (number1[i]=='0')&(number2[i]=='1'):
                return b
    return a, b

def sum_plav(number1,por1,number2,por2):
    final=""
    por1=por1[2:]
    por2=por2[2:]
    mant1=re.split(" ", conv(number1)[0])[2][1:]
    zn1=re.split(" ", conv(number1)[0])[2][0]
    mant2=re.split(" ", conv(number2)[0])[2][1:]
    zn2=re.split(" ", conv(number2)[0])[2][0]
    ed="1"
    if (compare(por1,por2)==por1):
        while (por2!=por1):
            mant1+='0'
            if (len(ed)<len(por1)):
                while len(ed)<len(por1):
                    ed=ed[::-1]
                    ed+='0'
                    ed=ed[::-1]
            por1=sub(por1,ed)
    if (compare(por1,por2)==por2):
        while (por1!=por2):
            mant2+='0'
            if (len(ed)<len(por2)):
                while len(ed)<len(por2):
                    ed=ed[::-1]
                    ed+='0'
                    ed=ed[::-1]
            por2=sub(por2,ed)
    if (compare(por1,por2)==(por1,por2)):
        if (zn1==zn2):
            final=zn1+'.'+por1+'.'+sum(mant1,mant2)
        elif (zn1=='1'):
            final=zn2+'.'+por1+'.'+sub(mant2,mant1)
        elif (zn2=='1'):
            final=zn1+'.'+por1+'.'+sub(mant1,mant2)
        return final

def float_to_binary(num):
    # Check if the number is negative
    sign = 1
    if num < 0:
        sign = -1
        num = -num

    # Split the number into integer and fractional parts
    integer_part = int(num)
    fractional_part = num - integer_part

    # Convert the integer part to binary
    integer_binary = ""
    while integer_part > 0:
        integer_binary = str(integer_part % 2) + integer_binary
        integer_part //= 2

    # Convert the fractional part to binary
    fractional_binary = ""
    while fractional_part > 0:
        if len(fractional_binary) >= 32: # limit the number of bits to 32
            break
        fractional_part *= 2
        if fractional_part >= 1:
            fractional_binary += "1"
            fractional_part -= 1
        else:
            fractional_binary += "0"

    # Combine the binary parts with the sign and return the result
    binary_string = ""
    if sign == -1:
        binary_string += "1"
    else:
        binary_string += "0"
    binary_string += integer_binary + "." + fractional_binary
    return binary_string
def add_floats(num1, num2):
    # Convert the numbers to binary
    binary1 = float_to_binary(num1)
    binary2 = float_to_binary(num2)

    # Extract the sign, integer, and fractional parts of each number
    sign1, int1, frac1 = binary1[0], binary1[2:binary1.index(".")], binary1[binary1.index(".") + 1:]
    sign2, int2, frac2 = binary2[0], binary2[2:binary2.index(".")], binary2[binary2.index(".") + 1:]

    # Pad the integer parts with zeros to make them the same length
    max_len = max(len(int1), len(int2))
    int1 = int1.rjust(max_len, "0")
    int2 = int2.rjust(max_len, "0")

    # Pad the fractional parts with zeros to make them the same length
    max_len = max(len(frac1), len(frac2))
    frac1 = frac1.ljust(max_len, "0")
    frac2 = frac2.ljust(max_len, "0")

    # Combine the integer and fractional parts into two binary strings
    binary_int = ""
    binary_frac = ""
    carry = 0
    for i in range(max_len - 1, -1, -1):
        bit1 = int(int1[i]) if i < len(int1) else 0
        bit2 = int(int2[i]) if i < len(int2) else 0
        sum_ = bit1 + bit2 + carry
        carry = 0
        if sum_ >= 2:
            carry = 1
            sum_ -= 2
        binary_int = str(sum_) + binary_int

        bit1 = int(frac1[i]) if i < len(frac1) else 0
        bit2 = int(frac2[i]) if i < len(frac2) else 0
        sum_ = bit1 + bit2 + carry
        carry = 0
        if sum_ >= 2:
            carry = 1
            sum_ -= 2
        binary_frac = str(sum_) + binary_frac

    # If there is a carry left over after adding the fractional parts, add it to the integer part
    if carry > 0:
        binary_int = bin(int(binary_int, 2) + 1)[2:]

    # Combine the sign, integer, and fractional parts into the final binary string
    binary_sum = sign1 + binary_int + "." + binary_frac

    return binary_sum


# print("enter floating point number")
# num=float(input())
# binary_string = float_to_binary(num)
# print(f"The binary representation of {num} is: {binary_string}")

print("enter 1st floating point number")
num1 = float(input())
print("enter 2nd floating point number")
num2 = float(input())
binary_sum = add_floats(num1, num2)
print(f"The binary sum of {num1} and {num2} is: {binary_sum}")


print("number 4 ",conv(4))
print("number 19 ",conv(19))
print("number -4 ",conv(-4))
print("number -19 ",conv(-19))

a=re.split(" ", conv(4)[0])[2]
b=re.split(" ", conv(19)[0])[2]
c=re.split(" ", conv(-4)[0])[2]
d=re.split(" ", conv(-19)[0])[2]

print("4+19 =",sum(a,b))
print("4-19 = ",sub(a,b))
print("19-4 = ",sub(b,a))
print("-4-19 = ",sum(c,d))

print("4*19 ",mul(a,b))
print("4*(-19) ",mul(a,d))
print("-4*19 ",mul(a,d))
print("-4*(-19) ",mul(a,b))

print("19/4 ",div(b,a))
print("-19/4 ",div(d,a))
print("19/-4 ",div(b,c))
print("-19/(-4) ",div(c,d))

print("reverse")
a=re.split(" ", conv(4)[1])[2]
b=re.split(" ", conv(19)[1])[2]
c=re.split(" ", conv(-4)[1])[2]
d=re.split(" ", conv(-19)[1])[2]

print("4+(-19) = ",sum(a,d))
print("19+(-4) = ",sum(b,c))
print("-4-19 = ",sum(c,d))

print("4*19 ",mul(a,b))
print("4*(-19) ",mul(a,d))
print("-4*19 ",mul(c,b))
print("-4*(-19) ",mul(c,d))

print("19/4 ",div(b,a))
print("-19/4 ",div(d,a))
print("19/-4 ",div(b,c))
print("-19/(-4) ",div(c,d))


print("additional")
a=re.split(" ", conv(4)[2])[2]
b=re.split(" ", conv(19)[2])[2]
c=re.split(" ", conv(-4)[2])[2]
d=re.split(" ", conv(-19)[2])[2]

print("4+(-19) = ",sum(a,d))
print("19+(-4) = ",sum(b,c))
print("-4-19 = ",sum(c,d))