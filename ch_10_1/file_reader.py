from pathlib import Path

file_path = Path(__file__).with_name('learning_python.txt')
contents = file_path.read_text()
print(contents)

for line in contents.splitlines():
    print(line.replace("Python", "Java"))