from logic import load_movies, save_movies, add_movie, mark_watched, find_by_year

DATA_FILE = "movies.json"

def main():
    movies = load_movies(DATA_FILE)

    while True:
        print("\nКаталог фильмов")
        print("1. Показать все фильмы")
        print("2. Добавить фильм")
        print("3. Отметить фильм как просмотренный")
        print("4. Найти фильмы по году")
        print("0. Выход")

        choice = input("Выберите пункт: ")

        if choice == "1":
            if not movies:
                print("Нет фильма в катологе")
            else:
                for movie in movies:
                    status = "Просмотрен" if movie["watched"] else "Не просмотрен"
                    print(f'ID: {movie["id"]}| {movie["title"]} ({movie["year"]}) — {status}')


        elif choice == "2":
            title = input("Ведите название фильма: ").strip()
            if not title:
                print("Введите название: ")
                continue
            try:
                year =  int(input("Введите год выпуска фильма: ").strip())
                movies = add_movie(movies, title, year)
                save_movies(DATA_FILE, movies)
                print(f"Фильм добавлен!!!")
            except ValueError:
                print("Год должен быть целым числом")

        elif choice == "3":
            if not movies:
                print("Нет фильмов")
                continue
            try:
                movie_id = int(input("Введите ID фильма: ").strip())
                if not any(m["id"] == movie_id for m in movies):
                    print("Фильма с таким ID не существует")
                    continue
                movie = mark_watched(movies, movie_id)
                save_movies(DATA_FILE, movie)
                print("Фильм отмечен!!!!")
            except ValueError:
                print("ID должен быть целым числом")

        elif choice == "4":
            try:
                year = int(input("Введите год для поиска фильма: ").strip())
                result = find_by_year(movies, year)
                if result:
                    print(f"Найдено {len(result)} фильм(ов) за {year} год:")
                    for movie in result:
                        status = status = "✅" if movie["watched"] else "⏳"
                        print(f'  ID: {movie["id"]} | {movie["title"]} — {status}')
                else:
                    print(f"Нет фильмов, выпущенных в {year} году.")
            except ValueError:
                print("Год должен быть целым числом.")

        elif choice == "0":
            save_movies(DATA_FILE, movies)
            print("До свидания!")
            break

        else:
            print("Неверный пункт меню.")

if __name__ == "__main__":
    main()
