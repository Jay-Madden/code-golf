def clamp(num):
    return max(min(num, 1), -1)

acceleration_map = {
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
                prob.append(1)
            else:
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
