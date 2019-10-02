
from tkinter import *
from tkinter import filedialog
from mass_file_downloader import gui_main


path = ""
url = ""

class main_gui:

	def __init__(self, master):
		self.master = master
		master.title("Mass Image Downloader")

		#file choosing button
		self.file_button = Button(master, text="...", command=self.pick_file)

		#text
		self.label_url = Label(master, text="Site url: ")
		self.label_path = Label(master, text="File path: ")

		#inputs
		self.url_input = Entry(master, validate="none") #add some kind of validation later
		self.file_input = Entry(master, validate="none")



		#need printing file statuses window
		

		#download and exit buttons
		self.down_button = Button(master, text="Download", command=self.down)
		self.close_button = Button(master, text="Exit", command=master.quit)




		#LAYOUT
		self.url_input.grid(row=1, column=2, columnspan=4, )
		self.file_input.grid(row=2, column=2, columnspan=4, )


		self.label_url.grid(row=1, column=1, columnspan=1, sticky=W)
		self.label_path.grid(row=2, column=1, columnspan=1, sticky=W)


		self.file_button.grid(row=2, column=6, columnspan=1)

		self.down_button.grid(row=10, column=2)
		self.close_button.grid(row=10, column=3)




#updates file_input and path
	def pick_file(self):

		global path
		p =  filedialog.askdirectory(initialdir = "/",title = "Select folder",)

		self.file_input.delete(0, END)
		self.file_input.insert(0, str(p))

		path = self.file_input.get()



	def down(self):

		global path
		global url

		#add check for url existing
		url = self.url_input.get()

		#makes sure a path exists
		if self.file_input.get() == "":
			self.pick_file()
		else:
			path = self.file_input.get()

		#downloads files with given info
		gui_main(path, url)


root = Tk()
my_gui = main_gui(root)
root.mainloop()



#__TODO__LIST__
'''

need to add scrollbar for messages

'''