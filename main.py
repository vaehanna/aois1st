import re
import struct
import math

def floating_point_new(number):
    # proverka na osobie sluchai
    if number == 0:
        return '00000000000000000000000000000000'
    elif number == float('inf'):
        return '01111111100000000000000000000000'
    elif number == float('-inf'):
        return '11111111100000000000000000000000'
    elif math.isnan(number):
        return '01111111110000000000000000000000'

    # znak
    if number < 0:
        sign = '1'
        number = abs(number)
    else:
        sign = '0'

    # float_to_2
    number_int = struct.unpack('!I', struct.pack('!f', number))[0]
    number_bin = bin(number_int)[2:].zfill(32)

    # iee754
    exponent = number_bin[1:9]
    mantissa = number_bin[9:]
    exponent_dec = int(exponent, 2) - 127
    mantissa_dec = sum(int(mantissa[i]) * 2 ** (-(i + 1)) for i in range(len(mantissa)))
    value = (-1) ** int(sign) * (1 + mantissa_dec) * 2 ** exponent_dec

    return number_bin

number1 = float(input("enter 1st floating point number\n"))
number2 = float(input("enter 2nd floating point number\n"))

bin1 = floating_point_new(number1)
bin2 = floating_point_new(number2)
bin_sum = floating_point_new(number1 + number2)

print(f"The IEE754 binary representation of {number1} is: {bin1}")
print(f"The IEE754 binary representation of {number2} is: {bin2}")
print(f"The IEE754 binary sum of {number1} and {number2} is: {bin_sum}")

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

# def add_floats(a, b):
#     # extract sign, exponent, and mantissa bits from a
#     a_sign = 0 if a >= 0 else 1
#     a_bits = abs(a).as_integer_ratio()
#     a_int = a_bits[0]
#     a_exp = 0
#     while a_int > 1:
#         a_int >>= 1
#         a_exp += 1
#     a_exp_bits = a_exp + 127
#     a_mantissa_bits = bin(a_bits[0] - (1 << a_exp) | (1 << 23))[3:]
#
#     # extract sign, exponent, and mantissa bits from b
#     b_sign = 0 if b >= 0 else 1
#     b_bits = abs(b).as_integer_ratio()
#     b_int = b_bits[0]
#     b_exp = 0
#     while b_int > 1:
#         b_int >>= 1
#         b_exp += 1
#     b_exp_bits = b_exp + 127
#     b_mantissa_bits = bin(b_bits[0] - (1 << b_exp) | (1 << 23))[3:]
#
#     # align exponents
#     if a_exp < b_exp:
#         a_exp_bits, b_exp_bits = b_exp_bits, a_exp_bits
#         a_mantissa_bits, b_mantissa_bits = b_mantissa_bits, a_mantissa_bits
#     while len(b_mantissa_bits) < len(a_mantissa_bits):
#         b_mantissa_bits += '0'
#     while len(a_mantissa_bits) < len(b_mantissa_bits):
#         a_mantissa_bits += '0'
#
#     # add mantissas
#     carry = 0
#     sum_mantissa_bits = ''
#     for i in range(len(a_mantissa_bits) - 1, -1, -1):
#         a_bit = int(a_mantissa_bits[i])
#         b_bit = int(b_mantissa_bits[i])
#         sum_bit = a_bit + b_bit + carry
#         if sum_bit >= 2:
#             carry = 1
#             sum_bit -= 2
#         else:
#             carry = 0
#         sum_mantissa_bits = str(sum_bit) + sum_mantissa_bits
#
#     # handle carry-out
#     if carry == 1:
#         a_exp_bits += 1
#         sum_mantissa_bits = '1' + sum_mantissa_bits[:-1]
#
#     # combine bits for sum
#     sum_sign = a_sign if a_exp_bits > b_exp_bits else b_sign
#     sum_exp_bits = a_exp_bits if a_exp_bits > b_exp_bits else b_exp_bits
#     sum_mantissa_bits = sum_mantissa_bits[:23]
#     sum_bits = (sum_sign << 31) | (sum_exp_bits << 23) | int(sum_mantissa_bits, 2)
#
#     # convert sum bits to float
#     sum_float = struct.unpack('!f', struct.pack('!I', sum_bits))[0]
#
#     return sum_float
# import struct
# import math
#
# def floating_point_new(number):
#     # Check for special cases
#     if number == 0:
#         return '00000000000000000000000000000000'
#     elif number == float('inf'):
#         return '01111111100000000000000000000000'
#     elif number == float('-inf'):
#         return '11111111100000000000000000000000'
#     elif math.isnan(number):
#         return '01111111110000000000000000000000'
#
#     # Extract the sign bit
#     if number < 0:
#         sign = '1'
#         number = abs(number)
#     else:
#         sign = '0'
#
#     # Convert the float to binary
#     number_int = struct.unpack('!I', struct.pack('!f', number))[0]
#     number_bin = bin(number_int)[2:].zfill(32)
#
#     # Separate the binary representation into sign, exponent, and mantissa bits
#     exponent = number_bin[1:9]
#     mantissa = number_bin[9:]
#
#     # Convert the exponent from bias notation to decimal
#     exponent_dec = int(exponent, 2) - 127
#
#     # Convert the mantissa to decimal
#     mantissa_dec = sum(int(mantissa[i]) * 2 ** (-(i + 1)) for i in range(len(mantissa)))
#
#     # Calculate the value of the float
#     value = (-1) ** int(sign) * (1 + mantissa_dec) * 2 ** exponent_dec
#
#     return number_bin
#
#
# # Test the function with 1.5 and 2.25
# number1 = float(input("enter 1st floating point number\n"))
# number2 = float(input("enter 2nd floating point number\n"))
#
# bin1 = floating_point_new(number1)
# bin2 = floating_point_new(number2)
# bin_sum = floating_point_new(number1 + number2)
#
# print(f"The binary representation of {number1} is: {bin1}")
# print(f"The binary representation of {number2} is: {bin2}")
# print(f"The binary sum of {number1} and {number2} is: {bin_sum}")


# print("enter floating point number")
# num=float(input())
# binary_string = converting_float_to_binary(num)
# print(f"The binary representation of {num} is: {binary_string}")

# print("enter 1st floating point number")
# a = float(input())
# print("enter 2nd floating point number")
# b = float(input())
# binary_sum = add_floats(a, b)
# print(f"The binary sum of {a} and {b} is: {binary_sum}")

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