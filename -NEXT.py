import time
from bs4 import BeautifulSoup
import requests
import re
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_captchasolver as vc
import requests
from vk_api.upload import VkUpload
from twocaptcha import TwoCaptcha
ownerbot = YOUR_VK_ID  #Твой id в vk
def captcha_handler(captcha):
    captcha_link = captcha.get_url()
    print("module anticaptcha!")
    response = requests.get(captcha_link)
    with open(f'captcha.jpg', 'wb') as file:
        file.write(response.content)
    captchacode = vc.solve(image='captcha.jpg')
    global anticapt
    time.sleep(2.8)
    print(f"luck: {captchacode}, {anticapt}")
    return captcha.try_again(captchacode)
token = 'VK ADMIN TOKEN  vk1.a.....'
vk_session = vk_api.VkApi(token=f"{token}", captcha_handler=captcha_handler)
vk = vk_session.get_api()
longpool = VkLongPoll(vk_session)
try:
    f = open('token_rabstvo_next.txt', 'r') # Чтение токена рабство next с файла
    tokenRABSTVONEXT = f.readline()         # Reading slavery next token from a file
    f.close()
    print(f'ok read: {tokenRABSTVONEXT}')
except:
    tokenRABSTVONEXT = 'null'                 # Если файла нету, то пропуск
    print('error read, token edited to null') # If there's no file, then skip
print('login succesful!')
while True:
    #try:
        for event in longpool.listen():     
            if event.type == VkEventType.MESSAGE_NEW:
                words = event.text.lower().split(' ')
                command = words[0]
                message = event.message
                message_list = message.split()

                try:
                    idowner = vk.messages.getById(message_ids=event.message_id)['items'][0]['from_id']
                except:
                    pass

                if idowner == ownerbot:
                    if len(message_list) > 0:
                        cmd = message_list[0]
                        if cmd == f"аа":
                            if len(message_list) > 1:
                                command = message_list[1]
                                if len(message_list) > 2:
                                    twoword = message_list[2]
                                
                                if command == '-токен':
                                    tokenRABSTVONEXT = 'null'
                                    vk.messages.send(message_id=event.message_id, peer_id=event.peer_id , message=f"Токен успешно удален",random_id=0, captcha_handler=captcha_handler)
                                if command == 'токен':
                                    try:
                                        vk.messages.send(message_id=event.message_id, peer_id=event.peer_id , message=f"TOKEN: {tokenRABSTVONEXT}",random_id=0, captcha_handler=captcha_handler)
                                    except:
                                        vk.messages.send(message_id=event.message_id, peer_id=event.peer_id , message=f"Ты забыл установить токен?, его нету..",random_id=0, captcha_handler=captcha_handler)
                                if command == '+токен':
                                    try:
                                        tokenRABSTVONEXT = twoword
                                        vk.messages.edit(message_id=event.message_id, peer_id=event.peer_id , message=f"Проверяю...",random_id=0, captcha_handler=captcha_handler)
                                        headers = {
                                                'Token': f'{tokenRABSTVONEXT}',
                                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
                                                }
                                        date = {'user_id': 454204598}
                                        response = requests.post('https://rabstvonext.ru/getuser', headers=headers, data=date)
                                        data = response.json()
                                        token_file = open("token_rabstvo_next.txt", "w")
                                        token_file.write(f'{tokenRABSTVONEXT}')
                                        token_file.close()
                                        vk.messages.edit(message_id=event.message_id, peer_id=event.peer_id , message=f"Новый токен подключен и работает успешно!\nTOKEN: {tokenRABSTVONEXT[0:8]}**************\nСохранил в файл",random_id=0, captcha_handler=captcha_handler)        
                                        
                                    except:
                                        vk.messages.send(message_id=event.message_id, peer_id=event.peer_id , message=f"Токен который ввели не работает -_-",random_id=0, captcha_handler=captcha_handler)
                                if command == 'пинг':
                                    if twoword == 'рабство':
                                        try:
                                            headers = {
                                                'Token': f'{tokenRABSTVONEXT}',
                                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit'
                                                }
                                            date = {'user_id': ownerbot}
                                            response = requests.post('https://rabstvonext.ru/getuser', headers=headers, data=date)
                                            data = response.json()
                                            vk.messages.send(message_id=event.message_id, peer_id=event.peer_id , message=f"Понг, токен активный)",random_id=0, captcha_handler=captcha_handler)
                                        except:
                                            vk.messages.send(message_id=event.message_id, peer_id=event.peer_id , message=f"Обнови токен, ошибка авторизации",random_id=0, captcha_handler=captcha_handler)

                                    else:
                                        vk.messages.send(message_id=event.message_id, peer_id=event.peer_id , message=f"понг!",random_id=0, captcha_handler=captcha_handler)
                                    
                                if command == 'инфо':
                                    match = re.search(r"@", twoword)
                                    if match:
                                        twoword = re.findall(r"id(\d+)", twoword)
                                        word = str(twoword)
                                        link = word.replace("'", '').replace('[', '').replace('[', '').replace(']', '')
                                        linkk = f'id{link}'
                                    else:
                                        linkk = twoword
                                        pass
                                    data = {'link': linkk,
                                            'button': 'Определить ID'}
                                    headers = {
                                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit'
                                    }
                                    response = requests.post('https://regvk.com/id/', headers=headers, data=data)
                                    bs = BeautifulSoup(response.text,"lxml")
                                    temp = bs.find('div', 'info')
                                    text = temp.text
                                    user_id = re.findall(r"ID пользователя: (\d+)", text)
                                    uuser_id_for_get_info = f'{user_id[0]}'
                                    try:
                                        headers = {
                                            'Token': f'{tokenRABSTVONEXT}',
                                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit'
                                            }
                                        date = {'user_id': uuser_id_for_get_info}
                                        response = requests.post('https://rabstvonext.ru/getuser', headers=headers, data=date)
                                        data = response.json()
                                        try:
                                            имя = data["item"]["name"]
                                        except:
                                            vk.messages.send(message_id=event.message_id, peer_id=event.peer_id , message=f"Игрок не играет в рабство next",random_id=0, captcha_handler=captcha_handler)
                                            break
                                        фамилия = data["item"]["last_name"]
                                        стоит = data["item"]["first_price"]
                                        всегорабов = data["item"]["rabs_count"]
                                        доход = data["item"]["rabs_sum_first_zarabotok"]
                                        продажа = data["item"]["price_sell"]
                                        втопе = data["item"]["position"]
                                        баланс = data["item"]["money_osn"]
                                        idrabstvonext = data["item"]["user_id"]
                                        try:
                                            кланссылка = data["item"]["clan"]["group_id"]
                                            кланимя = data["item"]["clan"]["name"]
                                        except:
                                            кланссылка = '❌❌❌'
                                            кланимя = 'null'
                                        try:
                                            владелец = data["item"]["master"]["id_vk"]
                                            vk.messages.send(message_id=event.message_id, peer_id=event.peer_id , message=f"==Инфо==\n\nЭто: {имя} {фамилия}\nVk: @id{uuser_id_for_get_info}\nRabstvo ID: {idrabstvonext}\nБаланс: {баланс}\nПокупка: {стоит}\nПродажа: {продажа}\nРабов: {всегорабов}\nДоход: {доход}\nВ топе на: {втопе}\nВладелец: @id{владелец}\nКлан: {кланимя}\nhttps://vk.com/public{кланссылка}",random_id=0, captcha_handler=captcha_handler)
                                        except:
                                            vk.messages.send(message_id=event.message_id, peer_id=event.peer_id , message=f"==Инфо==\n\nЭто: {имя} {фамилия}\nVk: @id{uuser_id_for_get_info}\nRabstvo ID: {idrabstvonext}\nБаланс: {баланс}\nПокупка: {стоит}\nПродажа: {продажа}\nРабов: {всегорабов}\nДоход: {доход}\nВ топе на: {втопе} месте\nВладелец: нету❌\nКлан: {кланимя}\nhttps://vk.com/public{кланссылка}",random_id=0, captcha_handler=captcha_handler)
                                    except:
                                        vk.messages.edit(message_id=event.message_id, peer_id=event.peer_id , message=f"Ошибочка получилась",random_id=0, captcha_handler=captcha_handler)
    #except: 
        #pass
