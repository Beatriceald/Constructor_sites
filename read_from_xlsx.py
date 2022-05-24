# import openpyxl
# from constructor.models import Template

# def adding():
#     DBconstructor = openpyxl.open("C:\\Users\\beatr\\OneDrive\\Рабочий стол\\Constructor_sites\\Constructor_sites\\Constructor_sites\\4constructor.xlsx", read_only=True)

#     sheet = DBconstructor.active

#     for category, sub_category in sheet.iter_rows(min_row=1, max_row=sheet.max_row+1, min_col=10, max_col=11):
#         for cell in category, sub_category:
#             #t, created = Template.objects.update_or_create(category=cell.value, sub_category=cell.value)
            
            
#             t = Template(category=cell.value, sub_category=cell.value)
#             t.save()
        
# #         print(cell.value, end='     ')
# #     print()





# # from blog.models import Blog
# # >>> b = Blog(name='Beatles Blog', tagline='All the latest Beatles news.')
# # >>> b.save()