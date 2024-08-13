files = ['1.txt', '2.txt']
file_data = []

# Читаем содержимое файлов и собираем информацию
for filename in files:
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        line_count = len(lines)
        file_data.append((filename, line_count, lines))

# Сортируем информацию по количеству строк
file_data.sort(key=lambda x: x[1])

# Записываем объединенное содержимое в новый файл
with open('result.txt', 'w', encoding='utf-8') as result_file:
    for filename, line_count, lines in file_data:
        result_file.write(f"{filename}\n{line_count}\n")
        result_file.writelines(lines)

print("Объединение завершено. Результат записан в 'result.txt'.")


# Вариант 2
def merge_files(file_names):
    sorted_file_data = sorted(((name, len(open(name, encoding='utf-8').readlines())) for name in file_names), key=lambda x: x[1])

    with open('result.txt', 'w', encoding='utf-8') as result_file:
        for file_name, line_count in sorted_file_data:
            file_content = open(file_name, encoding='utf-8').read()
            result_file.write(f'Имя файла: {file_name}\\n')
            result_file.write(f'Количество строк: {line_count}\\n')
            result_file.write(file_content + '\\n\\n')

