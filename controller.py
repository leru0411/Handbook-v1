#модуль в котором все функции из других модулей собираются воедино 
import handbook_base as hb
import view

def working():
    act = view.action()
    match act:
        case 'add':
            contact_name = view.get_name()
            contact_num = view.get_phone()
            contact_about = view.get_about()

            hb.add_name(contact_name)
            hb.add_number(contact_num)
            hb.add_about(contact_about)
        case 'read':
            print(hb.read_file())
        case 'find':
            contact_name = view.get_name()
            book = hb.read_file().split('\n')
            count = 0
            for i in book:
                if contact_name in i:
                    count += 1
                    print(i)

            if count == 0:
                print('contact not found')
  