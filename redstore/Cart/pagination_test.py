from django.core.paginator import Paginator

list = ['amalapoul', 'mamithabaiju', 'mahimanambyar', 'keerthisuresh']
p = Paginator(list ,2)


print('total items ',p.count)
print('num of pages ',p.num_pages)
page_1 = p.page(1)
page_2 = p.page(2)
print('page1',page_1)
print('page2',page_2)

print('items_in page 1',page_1.object_list)
print(page_1.has_next())
print(page_1.has_previous())

print(page_2.has_other_pages())

print(page_2.previous_page_number())