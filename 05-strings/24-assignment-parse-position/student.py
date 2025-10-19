# write your code here
def parse_position_x(string):
    # Remove parentheses
    string = string.strip("()")
    # Split into x and y
    x_str, y_str = string.split(",")
    # Convert to float and return x
    return float(x_str)


def parse_position_y(string):
    # Remove parentheses
    string = string.strip("()")
    # Split into x and y
    x_str, y_str = string.split(",")
    # Convert to float and return y (remove spaces first)
    return float(y_str.strip())
