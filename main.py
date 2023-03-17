import random

challenge_input = r"/\.|__/\."

direction = 0

acceleration_map = {
    "\\": lambda x: [x + 1],
    "/": lambda x: [x + (-1)],
    "_": lambda x: [x + 0],
    #"|": lambda x: [0] if abs(x) > 0 else [1, -1],
    "|": lambda x: [0] if abs(x) > 0 else [-1],
    ".": lambda x: [-99]
}

probability_list: list[int | float] = []
for position, char in enumerate(challenge_input):
    program_counter = position

    accel = None
    while accel != 0 and accel != -99:
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

        if accel:
            accel += accel_temp
        else:
            accel = accel_temp
        program_counter += accel

        if program_counter < 0 or program_counter >= len(challenge_input):
            accel = 0

    if accel == -99:
        print(f"Position: {position}: '{char}' found a hole")
    else:
        print(f"Position: {position}: '{char}' has an acceleration of: {accel}")







