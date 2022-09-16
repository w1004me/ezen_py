item_name = ["레쓰비","TOP","펜","종이컵","우유","콜라","사이다"]
my_items = {item_name[0]:13, item_name[1]:7, item_name[2]:4, item_name[3]:17, item_name[4]:5, item_name[5]:6, item_name[6]:8}
def cur_info():
    for item, value in my_items.items():
        print(item,":",value)
def inven_input():
    user_input_key = input("입력될 항목의 이름:")
    user_input_value = int(input("입력될 항목의 개수:"))
    my_items[user_input_key] = my_items[user_input_key]+user_input_value
def inven_output():
    user_input_key = input("출고될 항목의 이름:")
    user_input_value = int(input("출고될 항목의 개수:"))
    if(my_items[user_input_key]-user_input_value) < 0 :
        print("재고의 개수가 맞지 않습니다. 다시 입력해주세요")
    else:
        my_items[user_input_key] = my_items[user_input_key]-user_input_value
def inven_new():
    user_input_key = input("입력될 항목의 이름:")
    user_input_value = int(input("입력될 항목의 개수:"))
    my_items[user_input_key] = +user_input_value
while True:
    user_input = int(input("재고 입력(1), 출고(2), 신상품 입고(3), 현재 재고 출력(4), 종료(5)"))
    if user_input == 1:
        inven_input()
    elif user_input == 2:
        inven_output()
    elif user_input == 3:    
        inven_new()
    elif user_input == 4:
        cur_info()
    elif user_input == 5:
        break
