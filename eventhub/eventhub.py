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