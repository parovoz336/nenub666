import time

print("🐍 Проверка интерпретатора Python в VS Code...\n")

# 1. Простая математика
a = 15
b = 27
result = a + b
print(f"1. Математика работает: {a} + {b} = {result}")

# 2. Работа со списками
languages = ["Python", "JavaScript", "C++", "Rust"]
print(f"2. Список загружен: {', '.join(languages)}")

# 3. Небольшая анимация в консоли
print("\nЗапуск теста цикла:")
for i in range(1, 4):
    print(f"   Шаг {i}... ⏳")
    time.sleep(0.5)

print("\n🎉 Все отлично! Python настроен и работает корректно!")