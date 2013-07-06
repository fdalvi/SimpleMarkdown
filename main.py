#! /usr/bin/python

import gtk
import sys
import external.markdown2
import webkit

class MainWindow(gtk.Window):
    def __init__(self):

        # Initialize main window
        super(MainWindow, self).__init__()
        
        self.set_title("SimpleMarkdown")

        try:
            self.set_icon_from_file("logo.png")
        except Exception, e:
            print e.message
            sys.exit(1)

        self.connect("destroy", gtk.main_quit)
        self.set_size_request(800, 600)
        self.set_position(gtk.WIN_POS_CENTER)

        vbox = gtk.VBox(False, 2)

        # Create Menubar
        self.createMenuBar(vbox)

        
        table = gtk.Table(1, 2, True)

        self.text = gtk.TextView()
        self.text.set_editable(gtk.TRUE)
        table.attach(self.text, 0, 1, 0, 1)

        self.preview = webkit.WebView()
        
        table.attach(self.preview, 1, 2, 0, 1)

        vbox.pack_end(table, True, True, 0)
        self.add(vbox)

        self.show_all()

    def createMenuBar(self, vbox):
        menubar = gtk.MenuBar()

        # File menu
        fileMenu = gtk.MenuItem("File")
        fileSubMenu = gtk.Menu()
        fileMenu.set_submenu(fileSubMenu)

        fileMenuNew = gtk.MenuItem("_New")
        
        fileSubMenu.append(fileMenuNew)
        fileMenuExit = gtk.MenuItem("_Quit")
        fileMenuExit.connect("activate", gtk.main_quit)
        fileSubMenu.append(fileMenuExit)

        menubar.append(fileMenu);

        # Tools menu
        toolsMenu = gtk.MenuItem("Tools")
        toolsSubMenu = gtk.Menu()
        toolsMenu.set_submenu(toolsSubMenu)
        fileMenuExit = gtk.MenuItem("_Preview")
        fileMenuExit.connect("activate", self.preview)
        toolsSubMenu.append(fileMenuExit)

        menubar.append(toolsMenu);

        # Help menu
        helpMenu = gtk.MenuItem("Help")
        helpSubMenu = gtk.Menu()
        helpMenu.set_submenu(helpSubMenu)

        helpMenuAbout = gtk.MenuItem("About")
        helpMenuAbout.connect("activate", self.aboutDialog)
        helpSubMenu.append(helpMenuAbout)

        menubar.append(helpMenu)

        vbox.pack_start(menubar, False, False, 0)

    def aboutDialog(self, widget):
        about = gtk.AboutDialog()
        about.set_program_name("SimpleMarkdown")
        about.set_version("0.1")
        about.set_copyright("(c) Fahim Imaduddin Dalvi")
        about.set_comments("SimpleMarkdown is a fast and simple markdown editor")
        about.set_logo(gtk.gdk.pixbuf_new_from_file("logo.png"))
        about.run()
        about.destroy()

    def preview(self, widget):
        markdowner = external.markdown2.Markdown()
        textBuffer = self.text.get_buffer();
        self.preview.load_html_string(markdowner.convert(textBuffer.get_text(textBuffer.get_start_iter(), textBuffer.get_end_iter())), "file:///")


MainWindow()
gtk.main()