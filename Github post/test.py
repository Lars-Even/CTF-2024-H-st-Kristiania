
def add_binary(bin1, bin2):

    num1 = int(bin1, 2)
    num2 = int(bin2, 2)


    sum_num = num1 + num2


    return bin(sum_num)[2:]


bin1 = "10110111"
bin2 = "11010001"

result = add_binary(bin1, bin2)
print(f"The sum of {bin1} and {bin2} is: {result}")
