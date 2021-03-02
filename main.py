from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from  kivy.properties import ObjectProperty
import sqlite3


def get_item_info(id : str) :

    if not id :
        return 0
    con = sqlite3.connect('./TRIOL.db')
    cursor = con.cursor()
    cursor.execute('select name, description FROM Product where item_number = '+ id)
    out = cursor.fetchall()
    return out[0] if out else 0



class Container(GridLayout) :
    label = ObjectProperty()
    textinput = ObjectProperty()

    def find_item(self, id : str):

        result = get_item_info(id)
        return result[0] if result else 'No find'


class MyApp(App) :
    title = 'Triol'
    kv_file = './main.kv'

    def build(self):
        return Container()

if __name__ == '__main__' :
    MyApp().run()