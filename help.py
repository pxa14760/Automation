def base_top_border():
    print('+----', end=""),

def base_side_border():
    print('/    ', end=""),

def twobytwo_top_border():
    base_top_border()
    base_top_border()
    print('+')

def base_side_box():
    base_side_border()
    base_side_border()
    print('/')

def side_box():
    base_side_box()
    base_side_box()
    base_side_box()
    base_side_box()


def twobytwo_grid():
    twobytwo_top_border()
    side_box()
    twobytwo_top_border()
    side_box()
    twobytwo_top_border()

twobytwo_grid()
    

    
