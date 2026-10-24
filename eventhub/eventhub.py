data = [
    {'id': 1, 'title': 'Выставка котиков', 'date': '2026-10-25', 'price': 300},
    {'id': 2, 'title': 'Мастер-класс по Python', 'date': '2026-10-30', 'price': 0},
    {'id': 3, 'title': 'Кинопоказ', 'date': '2026-11-05', 'price': 500}
]

def edit_event(data, event_id, new_title, new_date, new_price):
    for event in data:
        if event.get("id") == event_id:
            event["title"] = new_title
            event["date"] = new_date
            event["price"] = new_price
            return True
    return False



# 11  Удаление из афиши
# Требования
# 1. Создайте delete_event(data, event_id).
# 2. Найдите мероприятие через find_event и удалите весь словарь из events.
# 3. Несуществующий ID не должен останавливать программу.
def delete_event(data, event_id):
    for event in data:
        if event.get("id") == event_id:
            data.remove(event)
            return True
    return False

# 12  Популярные события
# Требования
# 1. Создайте sort_by_popularity(data).
# 2. Расположите мероприятия от самого заполненного к наименее заполненному.
# 3. Используйте количество элементов participants как ключ сортировки.
def sort_by_popularity(data):
    return sorted(data,key=lambda x:len(x.get("participants",[])),reverse=True)

# 13  Статистика EventHub
# Требования
# 1. Создайте get_statistics(data).
# 2. Посчитайте количество мероприятий, число всех броней и возможный доход от уже забронированных мест.
# 3. Найдите название события с наибольшим количеством участников и верните результаты одним словарём.
    def get_statistics(data):
        
# 14  Отчёт для организатора
# Требования
# 1. Создайте export_report(data).
# 2. Запишите статистику в текстовый файл eventhub_report.txt.
# 3. Каждый показатель должен находиться на отдельной строке, а кириллица должна сохраняться правильно.
 
# 15  Готовый EventHub
# Требования
# 1. Соберите функции в одно циклическое меню: просмотр, добавление, фильтр, сортировка, бронь, отмена, редактирование, удаление, статистика, отчёт и выход.
# 2. После каждого успешного изменения вызывайте save_db(data). Неправильное число или пункт меню не должны завершать программу.
# 3. Заполните README.md: назначение проекта, файлы, запуск и возможности.
# 4. Проверьте git status, выполните git add ., создайте итоговый commit и отправьте проект командой git push. Ветки не используйте.