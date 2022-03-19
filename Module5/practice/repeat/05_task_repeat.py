# Дано общее количество объектов для отображения на веб-сайте и количество объектов на каждой странице.
# Вычислите, сколько объектов будет отображаться на последней странице сайта.

def last_page(num_items, items_on_page):
    return num_items % items_on_page

print(last_page(3,3))
print(last_page(5,3))
print(last_page(1,3))
print(last_page(11,3))
print(last_page(101,4))
