from store.show_store import show_store
from get_user_input import get_user_input
import keyboard

def store () :
    while True :

        # ฟังก์ชั่นแสดงผล
        show_store()

        # ข้อมูลจาก user
        new_key_pressed = get_user_input()

        # รอ user กดเลือกหน้าใน store
        if new_key_pressed == "0" :
            return -1
        if new_key_pressed == "1" :
            return 1
        if new_key_pressed == "2" :
            return 2
        if new_key_pressed == "3" :
            return 3