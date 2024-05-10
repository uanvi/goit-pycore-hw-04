def total_salary(path):
    total_salary = 0
    num_developers = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                name, salary = line.strip().split(',')
                total_salary += int(salary)
                num_developers += 1

        if num_developers == 0:
            return 0, 0

        average_salary = total_salary / num_developers
        return total_salary, average_salary

    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return 0, 0
    except ValueError:
        print(f"Wrong data pls check the file '{path}'")
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0, 0
