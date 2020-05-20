from tkinter import *
import tkinter.font

root=Tk()
root.geometry("800x600")

class PaintApp:
    text_font=StringVar()
    text_size=IntVar()
    bold_text=IntVar()
    italic_text=IntVar()

    drawing_tool=StringVar()

    left_but='up'
    x_pos,y_pos=None,None

    x1_line_pt,y1_line_pt,x2_line_pt,y2_line_pt=None,None,None,None

    @staticmethod
    def quit():
        root.destroy()

    def make_menu_bar(self):
        the_menu=Menu(root)
       
        #File#
        file_menu=Menu(the_menu,tearoff=0)
        file_menu.add_command(label='Open')
        file_menu.add_command(label='Save')
        file_menu.add_separator()
        file_menu.add_command(label='Quit',command=self.quit)

        the_menu.add_cascade(label='File',menu=file_menu)
        #File#

        #Font#
        font_menu=Menu(the_menu,tearoff=0)

        font_type_submenu=Menu(font_menu,tearoff=0)
        font_type_submenu.add_radiobutton(label='Times',variable=self.text_font,value='Times')
        font_type_submenu.add_radiobutton(label='Courier',variable=self.text_font,value='Courier')
        font_type_submenu.add_radiobutton(label='Arial',variable=self.text_font,value='Arial')
        font_menu.add_cascade(label='Font Type',menu=font_type_submenu)

        font_size_submenu=Menu(font_menu,tearoff=0)
        font_size_submenu.add_radiobutton(label='10',variable=self.text_size,value=10)
        font_size_submenu.add_radiobutton(label='15',variable=self.text_size,value=15)
        font_size_submenu.add_radiobutton(label='20',variable=self.text_size,value=20)
        font_size_submenu.add_radiobutton(label='25',variable=self.text_size,value=25)
        font_menu.add_cascade(label='Font Size',menu=font_size_submenu)
        
        font_menu.add_checkbutton(label='Bold',variable=self.bold_text, onvalue=1,offvalue=0)
        font_menu.add_checkbutton(label='Italic',variable=self.italic_text, onvalue=1,offvalue=0)
        
        the_menu.add_cascade(label='Font',menu=font_menu)
        
        #Tool#
        tool_menu=Menu(the_menu,tearoff=0)
        tool_menu.add_radiobutton(label='Pencil',variable=self.drawing_tool,value='pencil')
        tool_menu.add_radiobutton(label='Line',variable=self.drawing_tool,value='line')
        tool_menu.add_radiobutton(label='Oval',variable=self.drawing_tool,value='oval')
        tool_menu.add_radiobutton(label='Rectangle',variable=self.drawing_tool,value='rectangle')
        tool_menu.add_radiobutton(label='Text',variable=self.drawing_tool,value='text')

        the_menu.add_cascade(label='Tool',menu=tool_menu)
        #Tool#

        root.config(menu=the_menu)

    def __init__(self):
        drawing_area=Canvas(root)
        drawing_area.pack()
        self.text_font.set('Times')
        self.text_size.set(20)
        self.bold_text.set(0)
        self.italic_text.set(0)
        self.drawing_tool.set('line')
        self.make_menu_bar()

paint_app=PaintApp()
root.mainloop()

