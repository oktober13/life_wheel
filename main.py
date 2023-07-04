import matplotlib.pyplot as plt
import numpy as np

def draw_life_wheel():
    categories = ["Друзья", "Тело и здоровье", "Личность и духовное",
                  "Отдых и природа", "Финансы и карьера", "Быт и физическое окружение",
                  "Сеть контактов", "Семья"]
    ratings = []

    for category in categories:
        while True:
            try:
                rating = int(input(f"Сфера \"{category}\", укажите оценку от 1 до 10 насколько вы удовлетворены текущим её состоянием? "))
                if 1 <= rating <= 10:
                    ratings.append(rating)
                    break
                else:
                    print("Пожалуйста, введите число от 1 до 10.")
            except ValueError:
                print("Пожалуйста, введите число.")

    # Цвета для секторов и столбцов
    colors = ['tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:purple', 'tab:brown', 'tab:pink', 'tab:gray']

    # Строим круговую диаграмму
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))  # Создаем две области для диаграмм

    # Круговая диаграмма
    explode = [0.1] * len(categories)
    wedges, text, autotexts = ax1.pie(ratings, labels=categories, startangle=90,
                                     autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'},
                                     explode=explode, colors=colors)

    ax1.axis('equal')  # Это для того, чтобы круг был кругом, а не овалом.

    # Добавляем оценки внутри секторов
    for i, autotext in enumerate(autotexts):
        autotext.set_text(str(ratings[i]))

    ax1.set_title("Колесо жизни - Колесо жизненного баланса")

    # Гистограмма
    x = np.arange(len(categories))
    ax2.bar(x, ratings, align='center', color=colors, width=0.6)

    ax2.set_xticks(x)
    ax2.set_xticklabels(categories, rotation=45)
    ax2.set_xlabel("Сферы")
    ax2.set_ylabel("Оценки")

    ax2.set_title("Оценки по сферам")

    plt.tight_layout()  # Автоматически настраивает расположение элементов на графике
    plt.savefig('life_wheel.png')  # Сохраняем диаграмму в файл


if __name__ == "__main__":
    draw_life_wheel()
