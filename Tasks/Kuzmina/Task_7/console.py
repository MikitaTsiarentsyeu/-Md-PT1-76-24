from server import Collection

def main():
    collection = Collection()

    while True:
        print("\n1. Добавить новый альбом или фильм")
        print("2. Перечислить все альбомы или фильмы")
        print("3. Найти альбом или фильм")
        print("4. Выйти из программы")
        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название: ")
            artist_or_director = input("Введите художника или режиссера: ")
            year = input("Введите год выпуска: ")
            genre = input("Введите жанр: ")
            collection.add_item(title, artist_or_director, year, genre)
            print("Альбом или фильм добавлен.")
        
        elif choice == '2':
            items = collection.list_items()
            if items:
                for idx, item in enumerate(items, start=1):
                    print(f"{idx}. {item['title']} - {item['artist_or_director']} ({item['year']}) [{item['genre']}]")
            else:
                print("Коллекция пуста.")
        
        elif choice == '3':
            search_term = input("Введите название, художника/режиссера, год или жанр для поиска: ")
            results = collection.find_items(search_term)
            if results:
                for idx, item in enumerate(results, start=1):
                    print(f"{idx}. {item['title']} - {item['artist_or_director']} ({item['year']}) [{item['genre']}]")
            else:
                print("Ничего не найдено.")
        
        elif choice == '4':
            print("Выход из программы...")
            break
        
        else:
            print("Некорректный ввод. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()