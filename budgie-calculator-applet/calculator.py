#!/usr/bin/python3
# -*- encoding=utf-8 -*-

import gi
gi.require_version('Gtk','3.0')
from gi.repository import Gtk


class CalculatorGui(Gtk.Box):
    def __init__(self, css=False, buttons_fill=False, button_expand=False, box_padding=3, grid_padding=3):
        Gtk.Box.__init__(self)

        self.set_orientation(Gtk.Orientation.VERTICAL)

        self.grid      = Gtk.Grid     ()
        self.sep       = Gtk.Separator()
        self.entry     = Gtk.Entry    ()
        self.entry_box = Gtk.Box      ()

        if css:
            self.provider  = Gtk.CssProvider.new()
            self.provider.load_from_resource(css)


        self.pack_start(self.entry_box, True , True , box_padding)
        self.pack_start(self.sep      , True , True , 0        )
        self.pack_end  (self.grid     , True, True, box_padding)
        
        self.entry_box.pack_start(self.entry, True, True, box_padding)

        self.grid.set_row_spacing(grid_padding)
        self.grid.set_column_spacing(grid_padding)

        # This is where all the buttons are defined.
        self.buttonC      = Gtk.Button.new_with_label('C')
        self.button1      = Gtk.Button.new_with_label('1')
        self.button2      = Gtk.Button.new_with_label('2')
        self.button3      = Gtk.Button.new_with_label('3')
        self.button4      = Gtk.Button.new_with_label('4')
        self.button5      = Gtk.Button.new_with_label('5')
        self.button6      = Gtk.Button.new_with_label('6')
        self.button7      = Gtk.Button.new_with_label('7')
        self.button8      = Gtk.Button.new_with_label('8')
        self.button9      = Gtk.Button.new_with_label('9')
        self.button0      = Gtk.Button.new_with_label('0')
        self.buttonbpar   = Gtk.Button.new_with_label('(')
        self.buttonfpar   = Gtk.Button.new_with_label(')')
        self.buttonplus   = Gtk.Button.new_with_label('+')
        self.buttonequal  = Gtk.Button.new_with_label('=')
        self.buttonminus  = Gtk.Button.new_with_label('-')
        self.buttondivide = Gtk.Button.new_with_label('÷')
        self.buttonmulti  = Gtk.Button.new_with_label('×')
        self.buttondot    = Gtk.Button.new_with_label('.')
        self.buttonback   = Gtk.Button.new_with_label('🠄')
        self.buttonroot   = Gtk.Button.new_with_label('')
        self.buttonpower  = Gtk.Button.new_with_label('^')
                

        # Special colour for equal button.

        self.buttonequal.set_css_name('equal')
        
        
        self.button1.connect("clicked",self.fnc_button1)
        self.button2.connect("clicked",self.fnc_button2)
        self.button3.connect("clicked",self.fnc_button3)
        self.button4.connect("clicked",self.fnc_button4)
        self.button5.connect("clicked",self.fnc_button5)
        self.button6.connect("clicked",self.fnc_button6)
        self.button7.connect("clicked",self.fnc_button7)
        self.button8.connect("clicked",self.fnc_button8)
        self.button9.connect("clicked",self.fnc_button9)
        self.button0.connect("clicked",self.fnc_button0)
        self.buttonplus.connect("clicked",self.fnc_buttonplus)
        self.buttonfpar.connect("clicked",self.fnc_buttonfpar)
        self.buttonbpar.connect("clicked",self.fnc_buttonbpar)
        self.buttonminus.connect("clicked",self.fnc_buttonminus)
        self.buttondivide.connect("clicked",self.fnc_buttondivide)
        self.buttonmulti.connect("clicked",self.fnc_buttonmulti)
        self.buttondot.connect("clicked",self.fnc_buttondot)
        self.buttonpower.connect('clicked',self.fnc_buttonpower)
        

        self.buttonequal.connect('clicked', self.go            )
        self.buttonback.connect ('clicked', self.backspace_func)
        self.buttonC.connect    ('clicked', self.clear         )

        self.buttonequal.set_css_name('go_button')
        self.grid.set_border_width(3)
        

        # Here all the buttons are positioned.
        self.grid.attach(self.buttonC     , 1, 1, 1, 1)
        self.grid.attach(self.buttonbpar  , 2, 1, 1, 1)
        self.grid.attach(self.buttonfpar  , 3, 1, 1, 1)
        self.grid.attach(self.buttonback  , 4, 1, 1, 1)
        self.grid.attach(self.button1     , 1, 2, 1, 1)
        self.grid.attach(self.button2     , 2, 2, 1, 1)
        self.grid.attach(self.button3     , 3, 2, 1, 1)
        self.grid.attach(self.buttonplus  , 4, 2, 1, 1)
        self.grid.attach(self.button4     , 1, 3, 1, 1)
        self.grid.attach(self.button5     , 2, 3, 1, 1)
        self.grid.attach(self.button6     , 3, 3, 1, 1)
        self.grid.attach(self.buttonmulti , 4, 3, 1, 1)
        self.grid.attach(self.buttonback  , 5, 3, 1, 1)
        self.grid.attach(self.button7     , 1, 4, 1, 1)
        self.grid.attach(self.button8     , 2, 4, 1, 1)
        self.grid.attach(self.button9     , 3, 4, 1, 1)
        self.grid.attach(self.buttonminus , 4, 4, 1, 1)
        self.grid.attach(self.buttondot   , 1, 5, 1, 1)
        self.grid.attach(self.button0     , 2, 5, 1, 1)
        self.grid.attach(self.buttonpower , 3, 5, 1, 1)
        self.grid.attach(self.buttondivide, 4, 5, 1, 1)
        
        self.entry_box.pack_end(self.buttonequal, False, False, box_padding)
        

    def go(self, widget):
        _ = self.formatted_text()
        exec(f'self.entry.set_text(str({_}))')
    
    def backspace_func(self, widget):
        self.entry.set_text(self.entry.get_text()[:-1])
        
    def clear(self, button):
        self.entry.set_text('')
        
    def formatted_text(self):
              return self.entry.get_text().replace(' ','').replace('[','(').replace(']',')')\
                   .replace('×','*').replace('^','**').replace('÷','/')
                   
   # Now here are the functions for normal buttons
   
    def fnc_button1(self, button): self.entry.set_text(self.entry.get_text() + '1') 

    def fnc_button2(self, button): self.entry.set_text(self.entry.get_text() + '2') 
       
    def fnc_button3(self, button): self.entry.set_text(self.entry.get_text() + '3') 
     
    def fnc_button4(self, button): self.entry.set_text(self.entry.get_text() + '4') 
        
    def fnc_button5(self, button): self.entry.set_text(self.entry.get_text() + '5') 
         
    def fnc_button6(self, button): self.entry.set_text(self.entry.get_text() + '6') 
         
    def fnc_button7(self, button): self.entry.set_text(self.entry.get_text() + '7')      
    
    def fnc_button8(self, button): self.entry.set_text(self.entry.get_text() + '8') 
     
    def fnc_button9(self, button): self.entry.set_text(self.entry.get_text() + '9') 
     
    def fnc_button0(self, button): self.entry.set_text(self.entry.get_text() + '0') 
         
    def fnc_buttonplus(self, button): self.entry.set_text(self.entry.get_text() + '+') 
    
    def fnc_buttonfpar(self, button): self.entry.set_text(self.entry.get_text() + ')') 
         
    def fnc_buttonbpar(self, button): self.entry.set_text(self.entry.get_text() + '(')      
    
    def fnc_buttonminus(self, button): self.entry.set_text(self.entry.get_text() + '-')      
    
    def fnc_buttondivide(self, button): self.entry.set_text(self.entry.get_text() + '÷')      
    
    def fnc_buttonmulti(self, button): self.entry.set_text(self.entry.get_text() + '×')      
    
    def fnc_buttondot(self, button): self.entry.set_text(self.entry.get_text() + '.')      
    
    def fnc_buttonrem(self, button): self.entry.set_text(self.entry.get_text() + '%')
    
    def fnc_buttonpower(self, button): self.entry.set_text(self.entry.get_text() + '^') 