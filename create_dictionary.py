def read_cookbook(filename):
    """Читает данные из файла и возвращает их."""
    with open(filename, 'r', encoding="utf-8") as fp:
        data = fp.read()
    return data

def parse_recipes(data):
    """Разделяет данные на рецепты и возвращает словарь с рецептами."""
    recipes = data.strip().split("\n\n")
    cook_book = {}
    
    for recipe in recipes:
        lines = recipe.strip().splitlines()
        dish_name = lines[0]  # Название блюда
        ingredient_count = int(lines[1])  # Количество ингредиентов
        ingredients = parse_ingredients(lines[2:2 + ingredient_count])
        
        cook_book[dish_name] = ingredients
    
    return cook_book

def parse_ingredients(ingredient_lines):
    """Обрабатывает строки ингредиентов и возвращает список ингредиентов."""
    ingredients = []
    
    for line in ingredient_lines:
        ingredient_data = line.split(" | ")
        ingredient_name = ingredient_data[0].strip()  # Название ингредиента
        quantity = int(ingredient_data[1].strip())  # Количество
        measure = ingredient_data[2].strip()  # Единица измерения
        
        ingredients.append({
            'ingredient_name': ingredient_name,
            'quantity': quantity,
            'measure': measure
        })
    
    return ingredients

def main():
    """Основная функция для выполнения программы."""
    data = read_cookbook('cook_book.txt')
    cook_book = parse_recipes(data)
    print(cook_book)

if __name__ == "__main__":
    main()


