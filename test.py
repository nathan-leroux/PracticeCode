def write_reversed_file(input_filename, output_filename):
    """blah"""
    input_file = open(input_filename, 'r')
    input_data = input_file.readlines()
    input_file.close()

    output_file = open(output_filename, 'w')
    for line in reversed(input_data):
        output_file.write(line)
    output_file.close()