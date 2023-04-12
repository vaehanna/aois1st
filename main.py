import math
import re

def convert(num):
    direct = ""
    inverse = ""
    additional = ""
    if (num<0):
        label='false'
        num*=(-1)
    else:
        label='true'
    while(int(num)>=1):
        direct+=str(num%2)
        num=num//2
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

def sum(num1, num2):
    final=""
    num2=num2[::-1]
    num1=num1[::-1]
    if len(num1)>len(num2):
        max=len(num1)
        min=len(num2)
    else:
        max=len(num2)
        min=len(num1)
    dop=0
    for m in range(0,min):
        temp=int(num1[m])+int(num2[m])+dop
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
    if max==len(num1):
        for m in range(min,max+1):
            if (m==max)&(dop==1):
                temp=1
            elif (m!=max):
                temp=dop+int(num1[m])
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
                temp=dop+int(num2[m])
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
    num1=a[::-1]
    num2=b[::-1]
    dop=0
    for m in range(0,len(num1)):
        temp=int(num1[m])-int(num2[m])+dop
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

def mul(num1, num2):
    final=""
    stolbik=""
    schet=0
    for a in range (len(num2)-1,-1,-1):
        for r in range(0,schet):
            stolbik+='0'
        for b in range (len(num1)-1,-1,-1):
            rez = str(int(num1[b])&int(num2[a]))
            stolbik += rez
        stolbik=stolbik[::-1]
        final = sum(final,stolbik)
        stolbik=""
        schet+=1
    if ((num1[0]=='1')&(num2[0]=='0'))|((num1[0]=='0')&(num2[0]=='1')):
        final=final[::-1]
        final+='1'
        final=final[::-1]
    else:
        final=final[::-1]
        final+='0'
        final=final[::-1]
    return final

def div(num1, num2):
    final=""
    label1="true"
    label2="true"
    if (num1[0]=='1'):
        label1="false"
        num1=num1[1:]
    if (num2[0]=='1'):
        label2="false"
        num2=num1[1:]
    i=0
    while (num2[i]!='1')&(i<len(num2)):
        num2=num2[1:]
    if (compare(num1,num2)==(num1,num2)):
        final+='00000001'
        return final
    elif (compare(num1,num2)==num1):
        temp=""
        for j in range (0,len(num1)):
            temp+=num1[j]
            if (compare(temp,num2)==temp)|(compare(temp,num2)==(temp,num2)):
                final+='1'
                ch=num2
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
            elif (compare(temp,num2)==num2):
                final+='0'
    elif (compare(num1,num2)==num2):
        final+='0'
        temp=num1
    final+='.'
    for v in range (0,5):
        temp+='0'
        t=0
        while (temp[t]!='1')&(t<len(temp)-1):
            temp=temp[1:]
        if (temp=="0"):
            break
        if (compare(temp,num2)==temp)|(compare(temp,num2)==(temp,num2)):
                final+='1'
                ch=num2
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
        elif (compare(temp,num2)==num2):
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
    num1=a
    num2=b
    if (len(num1)>len(num2)):
        while (len(num1)!=len(num2)):
            num2=num2[::-1]
            num2+='0'
            num2=num2[::-1]
    elif (len(num2)>len(num1)):
        while (len(num2)!=len(num1)):
            num1=num1[::-1]
            num1+='0'
            num1=num1[::-1]
    if (len(num1)==len(num2)):
        for i in range(0,len(num1)):
            if (num1[i]=='1')&(num2[i]=='0'):
                return a
            if (num1[i]=='0')&(num2[i]=='1'):
                return b
    return a, b
def check_positive(value: (int, float)):
    return value > 0


def int_to_binary(value: int, bit_number: int = 16) -> str:
    result: str = ""
    if not check_positive(value):
        minus_bit = "1"
        value *= -1
    else:
        minus_bit = "0"
    while value != 0:
        result = str(value % 2) + result
        value = value // 2
    result = minus_bit + result
    result = result[:1] + "0" * (bit_number - len(result)) + result[1:]
    return result


def float_to_binary(value: float, bit_number: int = 16) -> str:
    if not check_positive(value):
        minus_bit = "1"
        value *= -1
    else:
        minus_bit = "0"
    int_part = int(value)
    float_part: float = value - float(int_part)
    result: str = int_to_binary(int_part)[1:]
    if "1" not in result:
        result = minus_bit + "0."
    else:
        result = minus_bit + result[result.find("1"):] + "."
    for i in range(bit_number - len(result) - 1):
        float_part *= 2
        if int(float_part) == 0:
            result += "0"
        else:
            result += "1"
        float_part = float_part - float(int(float_part))
    return result


def to_decimal_value(binary_value: str) -> int:
    number: int = 0
    for i in range(1, len(binary_value)):
        number += 2 ** (len(binary_value) - 1 - i) * int(binary_value[i])
    if int(binary_value[0]) == 0:
        return number
    else:
        return -number


def is_binary_value_positive(binary_value: str) -> bool:
    return binary_value[0] == "0"


def binary_absolute(binary_value: str) -> str:
    return "0" + binary_value[1:]


def binary_module_greater_than(first_value: str, second_value: str) -> bool:
    for i in range(len(first_value)):
        if first_value[i] == "1" and second_value[i] == "0":
            return True
        elif first_value[i] == "0" and second_value[i] == "1":
            return False
    return False


def binary_equality(first_value: str, second_value: str) -> bool:
    return first_value == second_value


def binary_greater_than(first_value: str, second_value: str) -> bool:
    if first_value[0] == "0" and second_value[0] == "1":
        return True
    elif first_value[0] == "1" and second_value[0] == "0":
        return False
    elif first_value[0] == "0" and second_value[0] == "0":
        return binary_module_greater_than(first_value[1:], second_value[1:])
    else:
        return not binary_module_greater_than(first_value[1:], second_value[1:])


def binary_values_addition(first_value: str, second_value: str) -> str:
    binary_first: str = ""
    binary_second: str = ""
    if is_binary_value_positive(first_value) and is_binary_value_positive(second_value):
        return addition(first_value, second_value)
    if first_value[0] == "0":
        binary_first: str = first_value
    if first_value[0] == "1":
        binary_first = full_complement(first_value)
    if second_value[0] == "0":
        binary_second: str = second_value
    if second_value[0] == "1":
        binary_second = full_complement(second_value)
    return full_complement(addition(binary_first,
                                    binary_second))


def binary_int_sum(first_int_value: int, second_int_number: int) -> str:
    binary_first_value: str = int_to_binary(first_int_value)
    binary_second_value: str = int_to_binary(second_int_number)
    return binary_values_addition(binary_first_value, binary_second_value)


def binary_difference(first_number: int, second_number: int) -> str:
    return binary_int_sum(first_number, -second_number)


def addition(first_value: str, second_value: str) -> str:
    if len(first_value) < len(second_value):
        first_value = "0" * (len(second_value) - len(first_value)) + first_value
    else:
        second_value = "0" * (len(first_value) - len(second_value)) + second_value
    additional_value: bool = False
    binary_result = ""
    for i in range(len(first_value) - 1, -1, -1):
        if first_value[i] == "0" and second_value[i] == "0":
            if additional_value:
                binary_result = "1" + binary_result
            else:
                binary_result = "0" + binary_result
            additional_value = False
        elif ((first_value[i] == "1" and second_value[i] == "0")
              or (first_value[i] == "0" and second_value[i] == "1")):
            if additional_value:
                binary_result = "0" + binary_result
            else:
                binary_result = "1" + binary_result
        else:
            if additional_value:
                binary_result = "1" + binary_result
            else:
                binary_result = "0" + binary_result
            additional_value = True
    return binary_result


def neg_complement(binary_number: str) -> str:
    if binary_number[0] == "0":
        return binary_number
    result = []
    for item in binary_number[1:]:
        if item == ".":
            result.append(item)
        elif item == "0":
            result.append("1")
        elif item == "1":
            result.append("0")
    ones_complement = "1" + "".join(result)
    return ones_complement


def full_complement(binary_number: str) -> str:
    if binary_number[0] == "0":
        return binary_number
    binary_number = neg_complement(binary_number)
    return addition(binary_number,
                    int_to_binary(1, bit_number=len(binary_number)))


def additional_full_complement(binary_value: str) -> str:
    if binary_value[0] == "0":
        return "0" + binary_value
    binary_value = neg_complement(binary_value)
    return "1" + addition(binary_value,
                          int_to_binary(1, bit_number=len(binary_value)))


# def shift_left(value):
#     result = value[1:]
#     result.append("0")
#     return result


# def complement(value):
#     result = []
#     invert = False
#     for i in reversed(value):
#         if i == "0" and invert is False:
#             result.append("0")
#         elif i == "1" and invert is False:
#             invert = True
#             result.append("1")
#         elif i == "1":
#             result.append("0")
#         else:
#             result.append("1")
#     result.reverse()
#     return result


# def list_addition(first_value, second_value):
#     summary = ["0", "0", "0", "0", "0", "0", "0", "0"]
#     carry = 0
#     for i in range(7, -1, -1):
#         if first_value[i] == "0" and second_value[i] == "0" and carry == 0:
#             summary[i] = "0"
#             carry = 0
#         elif first_value[i] == "0" and second_value[i] == "0" and carry == 1:
#             summary[i] = "1"
#             carry = 0
#         elif first_value[i] == "0" and second_value[i] == "1" and carry == 0:
#             summary[i] = "1"
#             carry = 0
#         elif first_value[i] == "0" and second_value[i] == "1" and carry == 1:
#             summary[i] = "0"
#             carry = 1
#         elif first_value[i] == "1" and second_value[i] == "0" and carry == 0:
#             summary[i] = "1"
#             carry = 0
#         elif first_value[i] == "1" and second_value[i] == "0" and carry == 1:
#             summary[i] = "0"
#             carry = 1
#         elif first_value[i] == "1" and second_value[i] == "1" and carry == 0:
#             summary[i] = "0"
#             carry = 1
#         elif first_value[i] == "1" and second_value[i] == "1" and carry == 1:
#             summary[i] = "1"
#             carry = 1
#     return summary


# def get_binary(value_str):
#     parts = value_str.split('.')
#     int_part = int(parts[0])
#     bin_int_part = []
#     if int_part == 0:
#         bin_int_part.append('0')
#     if int_part != 0:
#         while int_part != 0:
#             bin_int_part.append(str(int_part % 2))
#             int_part = int(int_part / 2)
#         bin_int_part.reverse()
#     return bin_int_part





# def fixed_point_to_decimal(fixed_point_number: str) -> float:
#     fraction: str = fixed_point_number[3:]
#     result: float = 0
#     for i in range(len(fraction)):
#         result += int(fraction[i]) * (2 ** (-(i + 1)))
#     if fixed_point_number[0] == "1":
#         return -result
#     else:
#         return result


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


def move_the_mantissa(mantissa: str, mantissa_moves: int) -> str:
    if mantissa_moves == 0:
        return mantissa
    return "0" * mantissa_moves + mantissa[:-mantissa_moves]


def mantissa_sum(floating_first: list[str, str, str],
                 floating_second: list[str, str, str]) -> list[str, str, str]:
    first_mantissa = additional_full_complement(floating_first[0] + floating_first[2])
    second_mantissa = additional_full_complement(floating_second[0] + floating_second[2])
    order: str = floating_first[1]
    new_mantissa = addition(first_mantissa, second_mantissa)
    if new_mantissa[:2] in ("10", "01"):
        order = addition(order, "00000001")
        new_mantissa = new_mantissa[0] + new_mantissa[:len(new_mantissa) - 1]
    if new_mantissa[:2] == "00":
        sign: str = "0"
    else:
        sign: str = "1"
    new_mantissa = full_complement(new_mantissa[1:])[1:]
    new_mantissa = new_mantissa[1:] + "0"
    new_floating_point = [sign, order, new_mantissa]
    return new_floating_point


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


def floating_point_to_decimal(floating_point_number: list[str, str, str]):
    decimal_degree: int = to_decimal_value("0" + floating_point_number[1]) - 127
    digit_degree = 0
    mantissa_result: float = 0
    floating_point_number[2] = "1" + floating_point_number[2]
    for digit in floating_point_number[2]:
        mantissa_result += int(digit) * 2 ** digit_degree
        digit_degree -= 1
    if floating_point_number[0] == "1":
        return -1 * mantissa_result * 2 ** decimal_degree
    else:
        return mantissa_result * 2 ** decimal_degree


# def multiplication(first_num, sec_num):
#     answer = ["0" for _ in range(16)]
#     if (first_num < 0) or (sec_num < 0):
#         answer[0] = '1'
#     if (first_num < 0) and (sec_num < 0):
#         answer[0] = '0'
#     first_num, sec_num = abs(int(first_num)), abs(int(sec_num))
#     if abs(first_num * sec_num) > 32767:
#         raise Exception("You are out of range")
#     else:
#         len_array = len(convert(sec_num))
#         first_num, sec_num = to_straight_code(first_num), to_straight_code(sec_num)
#         for i in range(len_array):
#             additional_array = ['0' for i in range(16)]
#             overload = 0
#             for index in range(15):
#                 index = 15 - index
#                 additional_array[index] = int(sec_num[15 - i]) * int(first_num[index])
#                 first_additional_value, second_additional_value = int(answer[index - i]), int(additional_array[index])
#                 if first_additional_value + second_additional_value + overload < 2:
#                     answer[index - i] = str(first_additional_value + second_additional_value + overload)
#                     overload = 0
#                 elif first_additional_value + second_additional_value + overload == 2:
#                     answer[index - i] = '0'
#                     overload = 1
#                 else:
#                     answer[index - i] = '1'
#                     overload = 1
#         return "".join(answer)


# def convert(n, base_system=2, head_system=10):
#     value = '0123456789'
#     if isinstance(n, str):
#         n = float(n, head_system)
#     if n >= base_system:
#         return convert(n // base_system, base_system) + value[n % base_system]
#     else:
#         return value[n]


# def to_straight_code(number):
#     str_code = ["0" for i in range(16)]
#     if number < 0:
#         number = abs(number)
#         str_code[0] = "1"
#     number = list(str(convert(number)))
#     for item in range(len(number)):
#         str_code[len(str_code) - (item + 1)] = number[len(number) - (item + 1)]
#     return str_code

def test_floating_point_addition(x, y) -> None:
    print("Floating point")
    result = floating_point_to_decimal(floating_point_summary(x, y))
    print(floating_point_summary(x, y))
    print(result)

x = input("Enter the first float number: ")
y = input("Enter the second float number: ")
test_floating_point_addition(float(x), float(y))


print("Число 10 ",convert(10))
print("Число 23 ",convert(23))
print("Число -10 ",convert(-10))
print("Число -23 ",convert(-23))

a=re.split(" ", convert(10)[0])[2]
b=re.split(" ", convert(23)[0])[2]
c=re.split(" ", convert(-10)[0])[2]
d=re.split(" ", convert(-23)[0])[2]

print("10+23 =",sum(a,b))
print("10-23 = ",sub(a,b))
print("23-10 = ",sub(b,a))
print("-10-23 = ",sum(c,d))

print("10*23 ",mul(a,b))
print("10*(-23) ",mul(a,d))
print("-10*23 ",mul(c,b))
print("-10*(-23) ",mul(c,d))

print("23/10 ",div(b,a))
print("-23/10 ",div(d,a))
print("23/-10 ",div(b,c))
print("-23/(-10) ",div(c,d))

print("Обратный код")
a=re.split(" ", convert(10)[1])[2]
b=re.split(" ", convert(23)[1])[2]
c=re.split(" ", convert(-10)[1])[2]
d=re.split(" ", convert(-23)[1])[2]

print("10+(-23) = ",sum(a,d))
print("23+(-10) = ",sum(b,c))
print("-10-23 = ",sum(c,d))

print("10*23 ",mul(a,b))
print("10*(-23) ",mul(a,d))
print("-10*23 ",mul(c,b))
print("-10*(-23) ",mul(c,d))

print("23/10 ",div(b,a))
print("-23/10 ",div(d,a))
print("23/-10 ",div(b,c))
print("-23/(-10) ",div(c,d))

print("Дополнительный код")
a=re.split(" ", convert(10)[2])[2]
b=re.split(" ", convert(23)[2])[2]
c=re.split(" ", convert(-10)[2])[2]
d=re.split(" ", convert(-23)[2])[2]

print("10+(-23) = ",sum(a,d))
print("23+(-10) = ",sum(b,c))
print("-10-23 = ",sum(c,d))