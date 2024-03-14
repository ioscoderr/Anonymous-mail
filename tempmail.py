#https://t.me/andrdevvv
#https://t.me/andrdevvv
#https://t.me/andrdevvv
#https://t.me/andrdevvv
#https://t.me/andrdevvv


import requests

def get_random_email():
    api_url = "https://www.1secmail.com/api/v1/?action=genRandomMailbox&count=1"

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        if isinstance(data, list) and len(data) > 0:
            email = data[0]
            return email
        else:
            print("Неверный формат ответа от API.")
            return None
    else:
        print(f"Ошибка при выполнении запроса. Код состояния: {response.status_code}")
        return None

def get_messages(email):
    login, domain = email.split("@")
    while True:
        api_url = f"https://www.1secmail.com/api/v1/?action=getMessages&login=" + login + "&domain=" + domain
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()
            if isinstance(data, list) and len(data) > 0:
                for message in data:
                    print("НОВОЕ ПИСЬМО:")
                    print("ID: ", message["id"])
                    print("От: ", message["from"])
                    print("Тема: ", message["subject"])
                    read_message(login, domain, str(message["id"]))
            else:
                print("Почтовый ящик пуст. " + "Ваша почта: " + email)
        else:
            print(f"Ошибка при выполнении запроса. Код состояния: {response.status_code}")


#https://t.me/andrdevvv
#https://t.me/andrdevvv
#https://t.me/andrdevvv
#https://t.me/andrdevvv
#https://t.me/andrdevvv


def read_message(login, domain, message_id):
    api_url = f"https://www.1secmail.com/api/v1/?action=readMessage&login={login}&domain={domain}&id={message_id}"
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        print(" ---- DATA ---- ")
        print(data)
        print(" ---- DATA ---- ")
        print("От:", data['from'])
        print("id:", data['id'])
        print("Тема:", data['subject'])
        print("Дата:", data['date'])
        print("Тело:", data['body'])

        print(" ---- MESSAGE ---- ")
        print(" ")
        print("Текстовое тело:", data['textBody'])
        print(" ---- MESSAGE ---- ")
        print(" ")
        print("HTML-тело:", data['htmlBody'])
        print("----------")
        print("----------")
        print("----------")
        print("----------")
        print("----------")
    else:
        print(f"Ошибка при выполнении запроса для чтения сообщения. Код состояния: {response.status_code}")

random_email = get_random_email()
if random_email:
    print(f"Случайный адрес электронной почты: {random_email}")
    get_messages(random_email)
else:
    print("Не удалось получить случайный адрес электронной почты.")


#https://t.me/andrdevvv
#https://t.me/andrdevvv
#https://t.me/andrdevvv
#https://t.me/andrdevvv
#https://t.me/andrdevvv
