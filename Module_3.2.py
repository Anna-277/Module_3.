# Домашняя работа по уроку "Способы вызова функции"
# Задача "Рассылка писем"

def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    variants = (".com", ".ru", ".net")

# Проверка на корректность "@" и домены
    if ("@" not in sender or not sender.endswith(variants)
            or "@" not in recipient or not recipient.endswith(
            variants)):
        print(f'Невозможно отправить письмо с адреса {sender} на адрес {recipient}.')
        return
# Проверка на отправку самому себе
    if sender == recipient:
        print(f'Нельзя отправить письмо самому себе!')
        return
# Проверка на отправителя по умолчанию
    if sender == "university.help@gmail.com":
        print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.')


send_email("Hello", "mail@mail.ru")
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender = 'urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender = 'urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender = 'urban.teacher@mail.ru')

