import LoggerNew
import Model
import user_unterface as view


def run ( ):
    while True:
        mod = view.choosemode()
        if mod =='1': # создание контакта
            contact = view.newcontact()
            LoggerNew.addnew(contact)
        elif mod =='2': # поиск контакта
            contact = view.contact_to_s()
            base = LoggerNew.getbase()
            result = Model.serchcontact(base, contact)
            view.show_found(result)
        elif mod =='3': # редактирование контакта
            contact = view.contact_to_s()
            base = LoggerNew.getbase()
            result = Model.serchcontact(base, contact)
            view.show_found(result)
            result = Model.edit_str(base, result)


        elif mod =='4': # удаление контакта
            contact = view.contact_to_s()
            base = LoggerNew.getbase()
            result = Model.serchcontact(base, contact)
            base = LoggerNew.del_base()
            # contact = delete_contact()
            # LoggerNew.delete_contact
