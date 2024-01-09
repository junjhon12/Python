class NegativeValueError(ValueError):
    pass

def steps_to_miles(steps):
    try:
        steps = int(steps)
        if steps < 0:
            raise NegativeValueError("Exception: Negative Step Count Entered.")
        return f'{steps / 2000:.2f} miles'
    except ValueError:
        raise ValueError("Exception: Non-Numeric Value Entered.")

# Getting input from the user
try:
    steps_input = input("Enter # of Steps: ")
    result = steps_to_miles(steps_input)
    print(result)
except (ValueError, NegativeValueError) as e:
    print(e)
