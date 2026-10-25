from functions.get_file_content import get_file_content


result = get_file_content("calculator", "lorem.txt")

x = f"lorem.txt length: {len(result)}"
print(x)

if "truncated" in result:
  print(f"lorem.txt truncated: {True}")
else:
  print(f"lorem.txt truncated: {False}")

print(get_file_content("calculator", "main.py"))
print(get_file_content("calculator", "pkg/calculator.py"))
print(get_file_content("calculator", "/bin/cat"))
print(get_file_content("calculator", "pkg/does_not_exist.py"))
