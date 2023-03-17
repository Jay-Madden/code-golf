
from challenge import challenge

challenge_input_lines = []
with open("input.txt") as f:
    while s := f.readline():
        challenge_input_lines.append(s.strip())

inputs = []
for i in [challenge_input_lines[i:i + 2] for i in range(0, len(challenge_input_lines), 2)]:
    input_line = i[0].split("=")[1]
    res = i[1].split("=")[1].replace("%", "")
    inputs.append((input_line, res))


def main():
    for input, res in inputs:
        print(int(challenge(input) * 100), res)

if __name__ == "__main__":
    main()
