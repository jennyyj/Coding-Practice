# p1_jacob_jenny.py

def line_number(input_file: str, output_file: str) -> None:
   
    try:
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for i, line in enumerate(infile, start=1):
                outfile.write(f"{i}. {line}")
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        raise

def parse_functions(file_name: str) -> tuple:
    
    try:
        with open(file_name, 'r') as file:
            functions = []
            lines = file.readlines()

            i = 0
            while i < len(lines):
                line = lines[i].strip()

                if line.startswith("def "):
                    func_name = line.split("(")[0][4:].strip()
                    func_args = line.split("(")[1].split(")")[0].strip()

                    j = i + 1
                    while j < len(lines) and not lines[j].strip().startswith("def "):
                        j += 1

                    func_code = ''.join(lines[i + 1:j]).strip()
                    func_code = '\n'.join(line for line in func_code.split('\n') if line and not line.startswith("#"))

                    functions.append((i + 1, func_name, func_args, func_code))

                    i = j
                else:
                    i += 1

            return tuple(sorted(functions, key=lambda x: x[1]))  # Sort by function name
    except FileNotFoundError:
        print(f"Error: {file_name} not found.")
        raise

def main():
    try:
        line_number("p1_jacob_jenny.py", "p1_jacob_jenny_output.txt")

        function_info = parse_functions("p1_jacob_jenny.py")
        for func in function_info:
            print(func)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
