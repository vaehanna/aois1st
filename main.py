
import math
import re

def perevod(chislo):
    direct = ""
    inverse = ""
    additional = ""
    if (chislo<0):
        label='false'
        chislo*=(-1)
    else:
        label='true'
    while(int(chislo)>=1):
        direct+=str(chislo%2)
        chislo=chislo//2
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

def sum(chislo1, chislo2):
    final=""
    chislo2=chislo2[::-1]
    chislo1=chislo1[::-1]
    if len(chislo1)>len(chislo2):
        max=len(chislo1)
        min=len(chislo2)
    else:
        max=len(chislo2)
        min=len(chislo1)
    dop=0
    for m in range(0,min):
        temp=int(chislo1[m])+int(chislo2[m])+dop
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
    if max==len(chislo1):
        for m in range(min,max+1):
            if (m==max)&(dop==1):
                temp=1
            elif (m!=max):
                temp=dop+int(chislo1[m])
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
                temp=dop+int(chislo2[m])
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

def razn(a,b):
    final=""
    chislo1=a[::-1]
    chislo2=b[::-1]
    dop=0
    for m in range(0,len(chislo1)):
        temp=int(chislo1[m])-int(chislo2[m])+dop
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

def umn(chislo1, chislo2):
    final=""
    stolbik=""
    schet=0
    for a in range (len(chislo2)-1,-1,-1):
        for r in range(0,schet):
            stolbik+='0'
        for b in range (len(chislo1)-1,-1,-1):
            rez = str(int(chislo1[b])&int(chislo2[a]))
            stolbik += rez
        stolbik=stolbik[::-1]
        final = sum(final,stolbik)
        stolbik=""
        schet+=1
    if ((chislo1[0]=='1')&(chislo2[0]=='0'))|((chislo1[0]=='0')&(chislo2[0]=='1')):
        final=final[::-1]
        final+='1'
        final=final[::-1]
    else:
        final=final[::-1]
        final+='0'
        final=final[::-1]
    return final

def delen(chislo1, chislo2):
    final=""
    label1="true"
    label2="true"
    if (chislo1[0]=='1'):
        label1="false"
        chislo1=chislo1[1:]
    if (chislo2[0]=='1'):
        label2="false"
        chislo2=chislo1[1:]
    i=0
    while (chislo2[i]!='1')&(i<len(chislo2)):
        chislo2=chislo2[1:]
    if (compare(chislo1,chislo2)==(chislo1,chislo2)):
        final+='00000001'
        return final
    elif (compare(chislo1,chislo2)==chislo1):
        temp=""
        for j in range (0,len(chislo1)):
            temp+=chislo1[j]
            if (compare(temp,chislo2)==temp)|(compare(temp,chislo2)==(temp,chislo2)):
                final+='1'
                ch=chislo2
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
                temp=razn(temp,ch)
            elif (compare(temp,chislo2)==chislo2):
                final+='0'
    elif (compare(chislo1,chislo2)==chislo2):
        final+='0'
        temp=chislo1
    final+='.'
    for v in range (0,5):
        temp+='0'
        t=0
        while (temp[t]!='1')&(t<len(temp)-1):
            temp=temp[1:]
        if (temp=="0"):
            break
        if (compare(temp,chislo2)==temp)|(compare(temp,chislo2)==(temp,chislo2)):
                final+='1'
                ch=chislo2
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
                temp=razn(temp,ch)
        elif (compare(temp,chislo2)==chislo2):
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
    chislo1=a
    chislo2=b
    if (len(chislo1)>len(chislo2)):
        while (len(chislo1)!=len(chislo2)):
            chislo2=chislo2[::-1]
            chislo2+='0'
            chislo2=chislo2[::-1]
    elif (len(chislo2)>len(chislo1)):
        while (len(chislo2)!=len(chislo1)):
            chislo1=chislo1[::-1]
            chislo1+='0'
            chislo1=chislo1[::-1]
    if (len(chislo1)==len(chislo2)):
        for i in range(0,len(chislo1)):
            if (chislo1[i]=='1')&(chislo2[i]=='0'):
                return a
            if (chislo1[i]=='0')&(chislo2[i]=='1'):
                return b
    return a, b

def convert_to_floating_point(number: (int, float)) -> list[str, str, str]:
    if number == 0:
        return ["0", "01111111", "0" * 23]
    if number < 0:
        sign = "1"
    else:
        sign = "0"
    if isinstance(number, int):
        binary_number = int_to_binary(number)[1:]
        digit_order: int = len(binary_number) - (binary_number.find("1") + 1)
    else:
        binary_number = float_to_binary(number, bit_number=32)[1:]
        digit_order = binary_number.find(".") - (binary_number.find("1") + 1)
        if digit_order < 0:
            digit_order += 1
        else:
            digit_order += 0
        binary_number_list: list = list(binary_number)
        binary_number_list.pop(binary_number_list.index("."))
        binary_number = "".join(binary_number_list)
    exponent: str = binary_values_addition(int_to_binary(127, 9),
                                           int_to_binary(digit_order, bit_number=9))[1:]
    mantissa = binary_number[binary_number.find("1"):]
    if len(mantissa) < 23:
        mantissa += "0" * (23 - len(mantissa))
    else:
        mantissa = mantissa[:23]

    return [sign, exponent, mantissa]

def normalizing(floating_first: list[str, str, str], floating_second: list[str, str, str]) -> tuple:
    if binary_module_greater_than(floating_first[1], floating_second[1]):
        point_moves: int = 0
        while not binary_equality(floating_first[1], floating_second[1]):
            floating_second[1] = addition(floating_second[1], "00000001")
            point_moves += 1
        floating_second[2] = move_the_mantissa(floating_second[2], point_moves)
    else:
        point_moves: int = 0
        while not binary_equality(floating_first[1], floating_second[1]):
            floating_first[1] = addition(floating_first[1], "00000001")
            point_moves += 1
        floating_first[2] = move_the_mantissa(floating_first[2], point_moves)
    return floating_first, floating_second

def floating_point_summary(first_number: (int, float),
                           second_number: (int, float)) -> list[str, str, str]:
    floating_first: list[str, str, str] = convert_to_floating_point(first_number)
    floating_second: list[str, str, str] = convert_to_floating_point(second_number)
    floating_first, floating_second = normalizing(floating_first, floating_second)
    new_floating_point = mantissa_sum(floating_first, floating_second)
    return new_floating_point
# def sum_plav(chislo1,por1,chislo2,por2):
#     final=""
#     por1=por1[2:]
#     por2=por2[2:]
#     mant1=re.split(" ", perevod(chislo1)[0])[2][1:]
#     zn1=re.split(" ", perevod(chislo1)[0])[2][0]
#     mant2=re.split(" ", perevod(chislo2)[0])[2][1:]
#     zn2=re.split(" ", perevod(chislo2)[0])[2][0]
#     ed="1"
#     if (compare(por1,por2)==por1):
#         while (por2!=por1):
#             mant1+='0'
#             if (len(ed)<len(por1)):
#                 while len(ed)<len(por1):
#                     ed=ed[::-1]
#                     ed+='0'
#                     ed=ed[::-1]
#             por1=razn(por1,ed)
#     if (compare(por1,por2)==por2):
#         while (por1!=por2):
#             mant2+='0'
#             if (len(ed)<len(por2)):
#                 while len(ed)<len(por2):
#                     ed=ed[::-1]
#                     ed+='0'
#                     ed=ed[::-1]
#             por2=razn(por2,ed)
#     if (compare(por1,por2)==(por1,por2)):
#         if (zn1==zn2):
#             final=zn1+'.'+por1+'.'+sum(mant1,mant2)
#         elif (zn1=='1'):
#             final=zn2+'.'+por1+'.'+razn(mant2,mant1)
#         elif (zn2=='1'):
#             final=zn1+'.'+por1+'.'+razn(mant1,mant2)
#         return final

print("Число 11 ",perevod(11))
print("Число 26 ",perevod(26))
print("Число -11 ",perevod(-11))
print("Число -26 ",perevod(-26))

a=re.split(" ", perevod(11)[0])[2]
b=re.split(" ", perevod(26)[0])[2]
c=re.split(" ", perevod(-11)[0])[2]
d=re.split(" ", perevod(-26)[0])[2]

print("11+26 =",sum(a,b))
print("11-26 = ",razn(a,b))
print("26-11 = ",razn(b,a))
print("-11-26 = ",sum(c,d))

print("11*26 ",umn(a,b))
print("11*(-26) ",umn(a,d))
print("-11*26 ",umn(c,b))
print("-11*(-26) ",umn(c,d))

print("26/11 ",delen(b,a))
print("-26/11 ",delen(d,a))
print("26/-11 ",delen(b,c))
print("-26/(-11) ",delen(c,d))

print("11*2^0.100+26*2^0.101 = ",sum_plav(11,"0.100",26,"0.101"))
print("-11*2^0.100+26*2^0.101 = ",sum_plav(-11,"0.100",-26,"0.101"))

print("Обратный код")
a=re.split(" ", perevod(11)[1])[2]
b=re.split(" ", perevod(26)[1])[2]
c=re.split(" ", perevod(-11)[1])[2]
d=re.split(" ", perevod(-26)[1])[2]

print("11+(-26) = ",sum(a,d))
print("26+(-11) = ",sum(b,c))
print("-11-26 = ",sum(c,d))

print("11*26 ",umn(a,b))
print("11*(-26) ",umn(a,d))
print("-11*26 ",umn(c,b))
print("-11*(-26) ",umn(c,d))

print("26/11 ",delen(b,a))
print("-26/11 ",delen(d,a))
print("26/-11 ",delen(b,c))
print("-26/(-11) ",delen(c,d))
print("11*2^0.100+26*2^0.101 = ",sum_plav(11,"0.100",26,"0.101"))
print("-11*2^0.100+26*2^0.101 = ",sum_plav(-11,"0.100",-26,"0.101"))

print("Дополнительный код")
a=re.split(" ", perevod(11)[2])[2]
b=re.split(" ", perevod(26)[2])[2]
c=re.split(" ", perevod(-11)[2])[2]
d=re.split(" ", perevod(-26)[2])[2]

print("11+(-26) = ",sum(a,d))
print("26+(-11) = ",sum(b,c))
print("-11-26 = ",sum(c,d))