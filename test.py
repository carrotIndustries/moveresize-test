from gi.repository import Gtk, Gdk
import time

builder=Gtk.Builder()
builder.add_from_file("ui.glade")
win=builder.get_object("window1")
win.show_all()


class Handler :
	def __init__(self) :
		pass
	
	def quit(self, widget) :
		Gtk.main_quit()
	
	def resize(self, edge, ev) :
		win.begin_resize_drag(edge, 1, ev.x_root, ev.y_root, ev.time)
		
	def bp_nw(self, widget, ev) :
		self.resize(Gdk.WindowEdge.NORTH_WEST ,ev)
		
	def bp_n(self, widget, ev) :
		self.resize(Gdk.WindowEdge.NORTH ,ev)
	
	def bp_ne(self, widget, ev) :
		self.resize(Gdk.WindowEdge.NORTH_EAST ,ev)
	
	def bp_w(self, widget, ev) :
		self.resize(Gdk.WindowEdge.WEST ,ev)
	
	def bp_e(self, widget, ev) :
		self.resize(Gdk.WindowEdge.EAST ,ev)
	
	def bp_sw(self, widget, ev) :
		self.resize(Gdk.WindowEdge.SOUTH_WEST ,ev)
	
	def bp_s(self, widget, ev) :
		self.resize(Gdk.WindowEdge.SOUTH ,ev)
	
	def bp_se(self, widget, ev) :
		self.resize(Gdk.WindowEdge.SOUTH_EAST ,ev)
	
	def bp_move(self, widget, ev) :
		win.begin_move_drag(1, ev.x_root, ev.y_root, ev.time)
		
		
builder.connect_signals(Handler())

Gtk.main()
