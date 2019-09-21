
#need to install on debian tkinter

from tkinter import *
from tkinter import filedialog
from mass_file_downloader import create_folder, parse, splice, mass_down

path = ""
url = ""

class main_gui:

	def __init__(self, master):
		self.master = master
		master.title("Mass Image Downloader")

		#file choosing button
		self.file_button = Button(master, text="...", command=self.pick_file)
		#self.file_button = Button(master, text="...", command=lambda *args: pick_file())

		#text
		self.label_url = Label(master, text="Thread url: ")
		self.label_path = Label(master, text="File path: ")

		#inputs
		self.url_input = Entry(master, validate="none") #add some kind of validation later
		self.file_input = Entry(master, validate="none")



		#need printing file statuses window
		

		#download and exit buttons
		self.down_button = Button(master, text="Download", command=self.down)
		self.close_button = Button(master, text="Exit", command=master.quit)
		#self.down_button = Button(master, text="Download", command=lambda *args: down())


		#LAYOUT
		self.url_input.grid(row=1, column=2, columnspan=4, )#sticky=W)
		self.file_input.grid(row=2, column=2, columnspan=4, )#sticky=W)


		self.label_url.grid(row=1, column=1, columnspan=1, sticky=W)
		self.label_path.grid(row=2, column=1, columnspan=1, sticky=W)


		self.file_button.grid(row=2, column=6, columnspan=1)

		self.down_button.grid(row=10, column=2)
		self.close_button.grid(row=10, column=3)




#doesnt update path variable
	def pick_file(self):

		global path
		p =  filedialog.askdirectory(initialdir = "/",title = "Select folder",)

		self.file_input.delete(0, END)
		self.file_input.insert(0, str(p))

		path = self.file_input.get()



	def down(self):

		global path
		global url

		url = self.url_input.get()

		if self.file_input.get() == "":
			self.pick_file()
		else:
			path = self.file_input.get()


		#for testing purposes
		pattern = "(?<!\"fileThumb\" )(href=\"//is2.4chan.org/.{1,22}\")"


		#create_folder(path)
		#urls = parse(pattern, "http://" + url)
		#urls = splice(urls)
		#mass_down(path, urls)

		#need downloader to give file types in windows


	



#C:\Users\XPS\Documents/test/


root = Tk()
my_gui = main_gui(root)
root.mainloop()



#__TODO__LIST__

#need to add scrollbar for messages

#listbox for file choosing or site choosing
#add radio buttons to choose site or just regex the url
