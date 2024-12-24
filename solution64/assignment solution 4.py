def reverse_string_recursive(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string_recursive(s[1:]) + s[0]

string = input("Enter a string: ")
print(f"Reversed string: {reverse_string_recursive(string)}")
