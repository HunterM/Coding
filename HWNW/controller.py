import logger
import model
import view



def run ():
    while True:
        mod = view.choice_mode()
        if mod =='1': # создание контакта
            contact = view.addcontact()
            logger.addcontact_new(contact)
        elif mod =='2': # поиск контакта
            contact = view.contact_to_s()
            base = logger.get_base()
            result = view.findcontact(base, contact)
            view.showcontact(result)
        # elif mod =='3': # редактирование контакта
        #     contact = view.contact_to_s()
        #     base = logger.logger.get_base()
        #     needcorrect = view.findcontact(base, contact)


        # elif mod =='4': # удаление контакта
        #     base = view.deletecontact()
        # elif mod =='5': # показать все контакты
        #     result = view.book
        elif mod =='0': # остановка процесса
            break 


