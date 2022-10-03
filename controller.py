#модуль в котором все функции из других модулей собираются воедино 
import handbook_base as hb
import view
import handbook_functions as hf

def add_contact():
    contact_name = view.get_name()
    contact_num = view.get_phone()
    contact_about = view.get_about()

    hb.add_name(contact_name)
    hb.add_number(contact_num)
    hb.add_about(contact_about)