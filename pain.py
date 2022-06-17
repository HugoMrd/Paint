from tkinter import *
from tkinter.colorchooser import askcolor


class Paint(object):

    taille_de_base = 5.0
    couleur_de_base = 'black'

    def __init__(self):
        self.root = Tk()
        self.root.title('Paint')
        ##self.root.iconbitmap('@/paint.xbm')
        img = PhotoImage(file='icons/paint.ico')
        self.root.tk.call('wm', 'iconphoto', root._w, img)

        self.bouton_stylo = Button(self.root, text='pen', command=self.stylo)
        self.bouton_stylo.grid(row=0, column=0)

        self.couleur_boutton = Button(self.root, text='color', command=self.choix_couleur)
        self.couleur_boutton.grid(row=0, column=1)

        self.gomme_button = Button(self.root, text='eraser', command=self.gomme)
        self.gomme_button.grid(row=0, column=2)

        self.choix_taille_button = Scale(self.root, from_=1, to=20, orient=HORIZONTAL)
        self.choix_taille_button.grid(row=0, column=3)

        self.supprimer_tout_button = Button(self.root, text='Tout supprimer', command=self.supprimer_tout)
        self.supprimer_tout_button.grid(row=0, column=4)

        self.canvas = Canvas(self.root, bg='white', width=1280, height=1024)
        self.canvas.grid(row=1, columnspan=5)
        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choix_taille_button.get()
        self.color = self.couleur_de_base
        self.gomme_on = False
        self.active_button = self.bouton_stylo
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

    def stylo(self):
        self.activate_button(self.bouton_stylo)

    def supprimer_tout(self):
        self.canvas.delete('all')



    def choix_couleur(self):
        self.gomme_on = False
        self.color = askcolor(color=self.color)[1]

    def gomme(self):
        self.activate_button(self.gomme_button, gomme_mode=True)

    def activate_button(self, some_button, gomme_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.gomme_on = gomme_mode

    def paint(self, event):
        self.line_width = self.choix_taille_button.get()
        paint_color = 'white' if self.gomme_on else self.color
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Paint()

