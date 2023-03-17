import random
import typing as t
import math

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
        print(math.trunc(challenge(input) * 100), res)

# --------------------------------

def clamp(num):
    return max(min(num, 1), -1)

acceleration_map: dict[str, t.Callable[[int], list[int]]] = {
    "\\": lambda x: [clamp(x + 1)],
    "/": lambda x: [clamp(x + (-1))],
    "_": lambda x: [x],
    "|": lambda x: [0] if abs(x) > 0 else [1, -1],
    ".": lambda x: [-99]
}

probability_list: list[int | float] = []

def challenge(challenge_input) -> int:
    final_prob = []
    for position, char in enumerate(challenge_input):
        program_counter = position

        accel = 0
        init_accel = acceleration_map[challenge_input[program_counter]](accel)

        prob = []
        for accel in init_accel:
            program_counter = position + accel

            accel = does_hit_hole(accel, program_counter, challenge_input)
            if accel == -99:
                #print(f"Position: {position}: '{char}' found a hole")
                prob.append(1)
            else:
                #print(f"Position: {position}: '{char}' did not find a hole")
                prob.append(0)

        final_prob.append(sum(prob) / len(init_accel))

    return sum(final_prob)/len(challenge_input)


def does_hit_hole(accel: int, program_counter: int, challenge_input: str):
    while accel != 0 and accel != -99:
        if program_counter < 0 or program_counter >= len(challenge_input):
            accel = 0
            break

        try:
            if accel:
                accel_temp = acceleration_map[challenge_input[program_counter]](accel)[0]
            else:
                accel_temp = acceleration_map[challenge_input[program_counter]](0)[0]
        except Exception as e:
            accel = 0
            break

        if accel_temp == -99:
            accel = -99
            break

        if accel_temp == 0:
            accel = 0
            break

        accel = accel_temp
        program_counter += accel

    return accel


if __name__ == "__main__":
    main()
