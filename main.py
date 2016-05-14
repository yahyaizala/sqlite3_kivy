#
from kivy.app import App
from kivy.uix.scrollview import  ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import  TextInput
from kivy.uix.button import  Button
from kivy.core.window import Window
from kivy.uix.label import Label
import sqlite3
class SliteApp(App):
    dbname="mydb.db"
    def build(self):

        root=BoxLayout(orientation="vertical",size_hint=(1,1))
        form=BoxLayout(size_hint=(1,None),height=50)
        self.inp=input=TextInput(size_hint_x=3)
        btn=Button(size_hint_x=1,text="Save")
        form.add_widget(input)
        form.add_widget(btn)
        btn.bind(on_release=self.save)
        scrol=ScrollView(size_hint=(1,0.9))
        self.grid= GridLayout(cols=1, spacing=1, size_hint_y=None,padding=10)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        root.add_widget(form)
        scrol.add_widget(self.grid)
        root.add_widget(scrol)
        self.addGrid()
        return root
    def addGrid(self):
        db = sqlite3.connect(self.dbname)
        cursor = db.cursor()
        sql = "select id,name from users"
        users = cursor.execute(sql).fetchall()
        for entry in users:
            self.grid.add_widget(Button(text=entry[1], size_hint=(1, None), height=50))
        db.close()

    def on_start(self):
        db = sqlite3.connect(self.dbname)
        db.execute("create table if not exists users(id integer primary key autoincrement,name varchar(35))")
        db.close()

    def save(self,inst):
        val=self.inp.text
        db=sqlite3.connect(self.dbname)
        sql="INSERT INTO users(name) VALUES('{}')".format(str(val))
        print sql
        #db.row_factory=sqlite3.Row
        #cursor=db.cursor()
        #cursor.execute(sql)
        db.execute(sql)
        db.commit()
        db.close()
        self.inp.text=""
        self.grid.add_widget(Button(text=val,size_hint=(1,None),height=50))



if __name__ == '__main__':
    SliteApp().run()
