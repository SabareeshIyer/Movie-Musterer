import requests
import json
import gi
from pprint import pprint

gi.require_version('Gtk','3.0')
from gi.repository import Gtk, GdkPixbuf

class MyWindow(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self,title="IMDb for Desktop")

		self.set_size_request(800,300)
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		vbox.set_homogeneous(False)
		
		hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
		hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
		hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20)		
		vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)	
		hbox3.set_size_request(100,0)

		vbox.pack_start(hbox1,False,False,0)
		vbox.pack_start(hbox2,False,False,0)
		vbox.pack_end(vbox2,False,False,0)
		vbox2.set_size_request(20,50)
		vbox.pack_start(hbox3,False,False,0)

		#Labels and Entry fields to get movie title and year

		movieTitleLabel = Gtk.Label("Enter movie title")
		hbox1.pack_start(movieTitleLabel,False,False,0)

		movieYearLabel = Gtk.Label("Enter movie year")
		hbox2.pack_start(movieYearLabel,False,False,0)

		self.movieTitleEntry = Gtk.Entry()
		self.movieTitleEntry.connect("activate",self.on_enter)
		hbox1.pack_start(self.movieTitleEntry,False,False,0)

		self.movieYearEntry = Gtk.Entry()
		hbox2.pack_start(self.movieYearEntry,False,False,0)

		searchButton = Gtk.Button.new_with_label("Search")
		searchButton.set_size_request(40,40)
		searchButton.connect("clicked",self.on_search_clicked)
		hbox3.pack_start(searchButton,False,False,0)

		self.display = Gtk.Label("")
		hbox3.pack_start(self.display,False,False,0)

		#img = Gtk.Image.new_from_file('imdb_image.jpeg')
		#hbox3.pack_start(img,False,False,0)

		self.add(vbox)


	def on_search_clicked(self,searchButton):
			
			url = 'http://omdbapi.com/?t='+self.movieTitleEntry.get_text()+'&y='+self.movieYearEntry.get_text()+'plot=short&r=json'
			response = requests.get(url)
			data = response.json()

			self.display.set_text("Director: "+data["Director"]+"\tYear: "+data["Year"]+"\nGenre: "+data["Genre"]+"\nCast: "+data["Actors"]+"\nPlot: "+data["Plot"])


	def on_enter(self,movieTitleEntry):
		url = 'http://omdbapi.com/?t='+self.movieTitleEntry.get_text()+'&y='+self.movieYearEntry.get_text()+'plot=short&r=json'
		response = requests.get(url)
		data = response.json()

		self.display.set_text("Director: "+data["Director"]+"\tYear: "+data["Year"]+"\nGenre: "+data["Genre"]+"\nCast: "+data["Actors"]+"\nPlot: "+data["Plot"])

			

window = MyWindow()
window.connect("delete-event",Gtk.main_quit)
window.show_all()
Gtk.main()