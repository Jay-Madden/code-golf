import random
import typing as t

challenge_input = r"/\.|__/\."

direction = 0

acceleration_map: dict[str, t.Callable[[int], list[int]]] = {
    "\\": lambda x: [1],
    "/": lambda x: [-1],
    "_": lambda x: [x],
    "|": lambda x: [0] if abs(x) > 0 else [1, -1],
    ".": lambda x: [-99]
}

probability_list: list[int | float] = []


def main():
    final_prob = []
    for position, char in enumerate(challenge_input):
        program_counter = position

        accel = 0
        init_accel = acceleration_map[challenge_input[program_counter]](accel)

        prob = []
        for accel in init_accel:
            program_counter = position + accel

            accel = does_hit_hole(accel, program_counter)
            if accel == -99:
                print(f"Position: {position}: '{char}' found a hole")
                prob.append(1)
            else:
                print(f"Position: {position}: '{char}' did not find a hole")
                prob.append(0)

        final_prob.append(sum(prob) / len(init_accel))

    print(final_prob)


def does_hit_hole(accel: int, program_counter: int):
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
