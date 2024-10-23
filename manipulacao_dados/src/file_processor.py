def process_file(input_path, output_path):
    with open(input_path, 'r') as infile:
        lines = infile.readlines()

    # Remove duplicatas e ordena as linhas
    unique_lines = sorted(set(lines))

    with open(output_path, 'w') as outfile:
        outfile.writelines(unique_lines)
