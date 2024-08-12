with open('cook_book.txt', 'r', encoding="utf-8") as fp:
    data = fp.read()

# Разделяем данные по пустым строкам
    recipes = data.strip().split("\n\n")
    cook_book = {}

    for recipe in recipes:
        lines = recipe.strip().splitlines()
        dish_name = lines[0]  # Название блюда
        ingredient_count = int(lines[1])  # Количество ингредиентов
        ingredients = []

        # Обрабатываем каждый ингредиент
        for i in range(2, 2 + ingredient_count):
            ingredient_data = lines[i].split(" | ")
            ingredient_name = ingredient_data[0].strip()  # Название ингредиента
            quantity = int(ingredient_data[1].strip())  # Количество
            measure = ingredient_data[2].strip()  # Единица измерения
            
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })

        cook_book[dish_name] = ingredients


print(cook_book)
