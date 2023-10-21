''' ADIF Treeview
    show ADIF data on Treeview GUI
'''
import os

import tkinter as tk
from tkinter import ttk

import pandas as pd


class Application(tk.Frame):
    '''Application - class to define GUI widgets

        tkinter widgets will be defined in Application.__init__

        Args:
            None
        Returns:
            None
    '''

    def __init__(self, master):
        super().__init__(master)
        self.grid()

        self.num_data = 0

        frame1 = tk.Frame(master)
        label1 = tk.Label(frame1,
                          text='File:',
                          )
        label1.grid(row=0, column=0)
        self.label2 = tk.Label(frame1,
                               width=25,
                               text='',
                               justify=tk.CENTER,
                               border=1,
                               font=('Courier New', 12)
                               )
        self.label2.grid(row=0, column=1)
        frame1.grid()

        frame2 = tk.Frame(master)
        self.treeview_from_csv(frame2)
        frame2.grid()

        frame3 = tk.Frame(master)
        extbtn = tk.Button(frame3,
                           text='Exit',
                           command=quit,
                           )
        extbtn.grid(row=0, column=0)
        frame3.grid()

    def treeview_from_csv(self, master):
        ''' treeview_from_csv '''
        # sample_csv = 'treeview_data.csv'
        sample_csv = 'adif_data.csv'
        self.label2['text'] = sample_csv
        path, _ = os.path.split(__file__)
        sample_file_path = os.path.join(path, sample_csv)

        # read_csv
        _df = pd.read_csv(sample_file_path, comment='#')
        column_list = _df.columns.to_list()
        self.num_data = len(_df)
        # ind_time_on = column_list.index('TIME_ON')
        # ind_time_off = column_list.index('TIME_OFF')

        # treeview
        self.tree = ttk.Treeview(master,
                                 columns=column_list,
                                 selectmode=tk.EXTENDED,
                                 height=10)
        
        # style
        style = ttk.Style()
        style.configure('Treeview.Heading', font=('Calibri', 11))
        style.configure('Treeview', font=('Courier New', 12))

        # column setting, heading
        self.tree.column('#0', width=0, stretch=tk.NO)
        self.tree.heading('#0', text='')
        for _c in column_list:
            if _c == 'ID':
                self.tree.column(_c, width=25, anchor=tk.CENTER)
            else:
                self.tree.column(_c, width=80, anchor=tk.CENTER)
            self.tree.heading(_c, text=_c, anchor=tk.CENTER)

        # record
        for i in range(len(_df)):
            values = _df.iloc[i].to_list()

            # print(values[7], type(values[9]))
            target_columns_index = [7, 9]
            for j in target_columns_index:
                # tmp = '{:06d}'.format(values[j])
                # print(values[j], tmp)
                # values[j] = '{:06d}'.format(values[j])
                values[j] = f'{values[j]:06}'

            self.tree.insert(parent='', tags=i, index=tk.END, iid=i, values=values)
            # print(values)
            # background color each 2 lines
            if i % 2 == 0:
                self.tree.tag_configure(i, background='#e6e6fa')

        # scrollbar
        scrollbar = ttk.Scrollbar(master, orient=tk.VERTICAL,
                                  command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.grid(row=0, column=0)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))


def main():
    '''example to call Application class'''

    root = tk.Tk()

    root.geometry('1400x300')
    root.title('ADIF Treeview')
    root.grid_anchor(tk.CENTER)

    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
