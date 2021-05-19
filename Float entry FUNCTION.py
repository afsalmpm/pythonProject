def float_entry(float_input):  # Float entry function
    loop_exit_value = "value error"
    while loop_exit_value == "value error":
        try:
            float_input = float(input(f'Enter {float_input} '))
            return float_input
        except ValueError:
            print(f"invalid {float_input} entry")
            loop_exit_value = "value error"
    return float_input


number = "whatever number "
number = float_entry(number)
print(number)
