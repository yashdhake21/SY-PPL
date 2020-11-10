import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class PyApp(Gtk.Window):
    def __init__(self):
        super(PyApp, self).__init__()
        self.set_title("Hello World in PyGTK")
        self.set_default_size(400, 300)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.label = Gtk.Label("Enter name")
        self.entry = Gtk.Entry()
        self.btn = Gtk.Button("Say Hello")
        self.btn.connect("button_press_event", self.hello)

        fixed = Gtk.Fixed()
        fixed.put(self.label, 100, 100)
        fixed.put(self.entry, 100, 125)
        fixed.put(self.btn, 100, 150)

        self.add(fixed)
        self.show_all()

    def hello(self, widget, event):
        print("hello", self.entry.get_text())


PyApp()
Gtk.main()