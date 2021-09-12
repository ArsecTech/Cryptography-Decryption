my_string = input('Enter string:')

nums = []

for char in my_string:
    nums.append(str(ord(char)+12))

secret_string = ','.join(nums)
print(secret_string)

string_list = []
for num_str in secret_string.split(','):
    string_list.append(chr(int(num_str)-12))

print(''.join(string_list))