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
        elif mod =='3': # редактирование контакта
            contact = view.contact_to_s()
            base = logger.get_base()
            result = view.findcontact(base, contact)
            if 'не найден' not in result[0] and len(base.split('\n'))>1:
                result = view.findcontact(base, [0])
                new_contact = view.addcontact()
                upd = view.update_base(upd)
                logger.update_base(upd)
            elif 'не найден' not in result[0]:
                result = base.split('\n')[0]
                new_contact = view.addcontact()
                upd = view.addcontact(base, result, new_contact)
                logger.update_base(upd)


        elif mod =='4': # удаление контакта
            contact = view.contact_to_s
            base = logger.get_base()
            result = view.findcontact(base, contact)
            view.showcontact(result)
        if 'не найден' not in result[0] and len(base.split('\n'))>1:
            upd = view.deletecontact(base, result)
            logger.update_base(upd)
        elif 'не найден' not in result[0]:
            result = base.split('\n')[0]
            upd = view.deletecontact(base, result)
            logger.update_base()

        elif mod =='0': # остановка процесса
            break 


