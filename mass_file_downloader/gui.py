
#need to install on debian tkinter

from tkinter import *
from tkinter import filedialog
from mass_file_downloader import create_folder, parse, splice, mass_down

class main_gui:
	def __init__(self, master):
		self.master = master
		master.title("Mass Image Downloader")

		#self.url = ""
		#self.path = ""
		url = StringVar()
		path = StringVar()


		self.file_button = Button(master, text="...", command=self.pick_file)

		self.label_url = Label(master, text="Thread url: ")
		self.label_path = Label(master, text="File path: ")


		self.url_input = Entry(master, validate="none") #add some kind of validation later
		self.file_input = Entry(master, validate="none")



		#need printing file statuses window
		

		self.down_button = Button(master, text="Download", command=self.down)
		self.close_button = Button(master, text="Exit", command=master.quit)
		

		#LAYOUT
		self.url_input.grid(row=1, column=2, columnspan=4, )#sticky=W)
		self.file_input.grid(row=2, column=2, columnspan=4, )#sticky=W)


		self.label_url.grid(row=1, column=1, columnspan=1, sticky=W)
		self.label_path.grid(row=2, column=1, columnspan=1, sticky=W)


		self.file_button.grid(row=2, column=6, columnspan=1)

		self.down_button.grid(row=10, column=2)
		self.close_button.grid(row=10, column=3)



	def down(self):
		url = self.url_input.get()
		path = self.file_input.get()

		pattern = "(?<!\"fileThumb\" )(href=\"//is2.4chan.org/.{1,22}\")"

		print(url)
		print(path)

		#create_folder(self.path)
		#urls = parse(pattern, "http://" + self.url)
		#urls = splice(urls)
		#mass_down(self.path, urls)

		#need downloader to give file types in windows


	#doesnt update path variable
	def pick_file(self):
		p =  filedialog.askdirectory(initialdir = "/",title = "Select folder",)

		path = str(p)
		print(path)



#C:\Users\XPS\Documents/test/


root = Tk()
my_gui = main_gui(root)
root.mainloop()



#__TODO__LIST__

#need to add scrollbar for messages

#listbox for file choosing or site choosing
#add radio buttons to choose site or just regex the url
