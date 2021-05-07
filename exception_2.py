# try:
#     raise MemoryError('memory error')
# except MemoryError as e:
#     print(e)

# class Accident(Exception):
#     def __init__(self,msg):
#         self.msg=msg
#     def print_exception(self):
#         print("User defined exception:",self.msg)
 
# try:
#     raise Accident('crash between two cars')
# except Accident as e:
#     e.print_exception()

# class Accident(Exception):
#     def __init__(self,msg):
#         self.msg=msg
#     def handle(self):
#         print("accident occured take detour")
 
# try:
#     raise Accident('crash between two cars')
# except Accident as e:
#     e.handle()

def process_file():
    try:
        f=open("C:\\datas\\mine.txt")
        x=1/0
    except FileNotFoundError as e:
        print("inside except")
    finally:
        print("cleaningg up files")
        f.close()

process_file()