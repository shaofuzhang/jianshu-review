import time
from selenium import webdriver

driver = webdriver.Firefox()

black_list = ['DuYang_ZXM']

white_list = ['咖喱py']

driver.get('http://www.jianshu.com')

time.sleep(40)
driver.get('http://www.jianshu.com/notifications#/collections/NEt52a/submissions')
time.sleep(8)

note_list = driver.find_element_by_class_name('note-list')
li_list = note_list.find_elements_by_tag_name('li')

for li_obj in li_list:
    content = li_obj.find_element_by_class_name('content')
    name = content.find_element_by_class_name('name')
    name_val = name.find_element_by_tag_name('a')
    # print(name_val.text)
    if name_val in black_list:
        btn_gray = li_obj.find_element_by_class_name('btn-gray')
        # print(btn_gray.text)
        btn_gray.click()
    elif name_val in white_list:
        btn_hollow = li_obj.find_element_by_class_name('btn-hollow')
        # print(btn_gray.text)
        btn_hollow.click()
