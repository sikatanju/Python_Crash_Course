# *** Trying to read contents from a text file

# from pathlib import Path

# path = Path('contents/pi_digits.txt')
# pi = path.read_text()
# lines = pi.split('\n')
# c_lines = [line.rstrip() for line in lines if line.strip()]
# clean_text = '\n'.join(c_lines)
# print(pi)

# ** Relative and Absolute paths

# * Accessing a files lines:

# lines = pi.splitlines()

# for line in lines:
#     print(line.rstrip())


# ** Working with a file's content: after storing a file's content into the memory, we can modify it however we want

# * Here creating a single line string with all the digits in the file

# lines = pi.splitlines()
# pii = lines[0]
# for i in range(1, len(lines)):
#     pii += lines[1].strip()

# print(pii)


# * Large files: One Million Digits, there isn't any limit to how much data you can work with.

# large_path = Path('contents/pi_million_digits.txt')
# large_pi = large_path.read_text()

# print(large_pi[:51])
# print(len(large_pi))

# lines = large_pi.splitlines()

# pi_str = ''
# for line in lines:
#     pi_str += line.strip()

# print(pi_str)
# birthday = input("Enter your birthday (ddmmyyyy): ")

# if birthday in pi_str:
#     print("Yay!!!, You're birthday is in PI")
# else:
#     print("Nayy!!!, You're dumb")



# * Using `replace` method:

# print(pi.replace('9', '0'))