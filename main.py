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
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0, 0

# # Приклад використання:
# total, average = total_salary("resources/salaries.txt")
# print("Total salary:", total)
# print("Average salary:", average)


def get_cats_info(path):
    """Function return list of dictionaries with info about cat
    """
    cats_info = []

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_id, name, age = line.strip().split(',')
                cat_info = {
                    "id": cat_id,
                    "name": name,
                    "age": int(age)
                }
                cats_info.append(cat_info)

    except FileNotFoundError:
        print(f"File '{path}' not found.")
    except ValueError:
        print(f"Wrong data pls check the file '{path}'")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return cats_info

# # Приклад використання:
# cats = get_cats_info("resources/cats_file.txt")
# #for cat in cats:
# print(cats)
