from kivy.app import App
from kivy.uix.gridlayout import GridLayout
import sqlite3


def get_item_info(id : str) :
# ищем наименование товара по его ID
# Возвращает картеж для найденого товара из двух записей (наименование, описание)
# или [0]

    if not id  or not id.isdigit():
        # проверка переданного id на пустоту
        # проверка на отсутсвие букв в id товара
        return [0]
    con = sqlite3.connect('./TRIOL.db')
    cursor = con.cursor()
    cursor.execute('select name, description FROM Product where item_number = '+ id)
    out = cursor.fetchall()
    return out[0] if out else 0



class Container(GridLayout) :

    def find_item(self, id : str):

        result = get_item_info(id)
        return result[0] if result[0] else 'No find'

    def set_label_text(self, text : list, label : object):
    # функция устанавливаает свойство text объекта label
        label.text = text


class MyApp(App) :
    title = 'Triol'
    kv_file = './main.kv'

    def build(self):
        return Container()

if __name__ == '__main__' :
    MyApp().run()