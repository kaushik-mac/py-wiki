
'''This programme only runs in python virtual enviroment so make sure to set your intrepreter to virtual python enviromnent'''

# '''import all modules needed'''
from tkinter import Button, Label, Listbox, PhotoImage, Tk ,Text  
from tkinter.constants import ACTIVE, END, SINGLE
import wikipedia
from py_module import search

# '''set up basic configuration for main app'''
root=Tk()
root.geometry('500x500')
root.resizable(False,False)
root.title('Pywiki Search')
# '''icon photo on title bar which is saved in same directory named `wikipedia.png`'''
photo_icon=PhotoImage(file='wikipedia.png')
root.iconphoto(False,photo_icon)
root.configure(bg='#34393b')


# '''main function in whhich all things are there'''
def main_function():
    # '''command function to search on wikipedia api if entered text by user in match in wikipedia api if true then show a list of all possible title in wikipedia''' 
    def result():

        global result_list 

        # label to show how to do summary search
        search_topic_label=Label(root,text='Select topic from above list and press submit button below',bg='#34393b',fg='#fffffc',font=('bold italic',12))
        search_topic_label.place(x=20,y=300,height=20,width=460)
        # btn for summary search label
        search_topic_btn=Button(root,text='Submit',bg='#6be387',fg='#c72222',font=('bold italic',11),command=lambda:result_selected())
        search_topic_btn.place(x=200,y=330,height=20,width=100)

        # get text entered by user
        search_object=str(search_input.get('1.0','end'))
        search_object_number=int(number_input.get('1.0','end'))
        # search the result from custom library named `pywiki`
        y=list(search(search_object,search_object_number))
        # create list box and insert elements here the result of user inputed text
        result_list=Listbox(root,selectmode=SINGLE,font=('bold',12),bg='#e8e26f')
        result_list.place(x=25,y=50,height=230,width=445)
        result_list.insert(END)
        for items in y:
            result_list.insert(END,items)

        
    # function to show what topic user what to read from wikipedia based on what he/she search    
    def result_selected():
        # get selected item
        selected_item=(result_list.get(ACTIVE))
        summary=(wikipedia.summary(selected_item,sentences=3))
   
        # resize the geometry
        root.geometry('500x700')
        # output the summary
        summary_label=Label(root,text=summary,wraplength=440,font=('small',9))
        summary_label.place(x=20,y=370,height=300,width=460)
    
    # label to show search text
    search_label=Label(root,text='Search',bg='#6be387',fg='#000000',font=("bold italic", 11))
    search_label.place(x=20,y=20,height=20,width=60)
    # to get user input
    search_input=Text(root,bg='#b3afaf')
    search_input.place(x=90,y=20,height=20,width=130)
    # search result by pressing this button
    search_btn=Button(root,text='Submit',command=result,bg='#6be387',fg='#c72222',font=('bold italic',11))
    search_btn.place(x=400,y=20,height=20,width=70)
    # how many result user want
    number_label=Label(root,text='No. of result',bg='#a6cede',fg='#000000',font=("bold italic", 11))
    number_label.place(x=250,y=20,height=20,width=85)
    # get entry of number of result
    number_input=Text(root,bg='#b3afaf')
    number_input.place(x=350,y=20,height=20,width=40)

# call function
main_function()
# show the app
root.mainloop()
