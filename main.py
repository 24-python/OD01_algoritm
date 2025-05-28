def is_palindrome(s: str) -> bool:
    # Очищаем строку: оставляем только буквы и цифры (пробелы и пунктуация игнорируются)
    cleaned = ''.join(c for c in s.lower() if c.isalnum())
    left, right = 0, len(cleaned) - 1

    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1

    return True


def main():
    print("🔍 Проверка строки на палиндром (для выхода введите 'exit' или нажмите Ctrl+C)")

    while True:  # Бесконечный цикл
        user_input = input("\nВведите фразу: ").strip()

        if user_input.lower() in ('exit', 'выход', ''):  # Условие выхода
            print("🛑 Программа завершена.")
            break

        if not user_input:
            print("❌ Ошибка: Пустая строка! Попробуйте снова.")
            continue

        if is_palindrome(user_input):
            print("✅ Да, это палиндром!")
        else:
            print("❌ Нет, это не палиндром.")


if __name__ == "__main__":
    main()