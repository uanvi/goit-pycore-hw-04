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
