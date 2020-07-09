import gi.repository
gi.require_version('Budgie', '1.0')
from gi.repository import Budgie, GObject, Gtk, Gio
from calculator import CalculatorGui as calc
import os


"""
Budgie EmptyPopover

Author: Heavily Modified fro CountDown applet by Jacob Vlijm
Copyright © 2017-2020 Ubuntu Budgie Developers
Website=https://ubuntubudgie.org
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or any later version. This
program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
A PARTICULAR PURPOSE. See the GNU General Public License for more details. You
should have received a copy of the GNU General Public License along with this
program.  If not, see <http://www.gnu.org/licenses/>.
"""

class budgie_calculator(GObject.GObject, Budgie.Plugin):
    """ This is simply an entry point into your Budgie Applet implementation.
        Note you must always override Object, and implement Plugin.
    """

    # Good manners, make sure we have unique name in GObject type system
    __gtype_name__ = "BudgieCalculatorApplet"

    def __init__(self):
        """ Initialisation is important.
        """
        GObject.Object.__init__(self)

    def do_get_panel_widget(self, uuid):
        """ This is where the real fun happens. Return a new Budgie.Applet
            instance with the given UUID. The UUID is determined by the
            BudgiePanelManager, and is used for lifetime tracking.
        """
        return BudgieCalculatorApplet(uuid)


class BudgieCalculatorApplet(Budgie.Applet):
    """ Budgie.Applet is in fact a Gtk.Bin """

    def __init__(self, uuid):

        self.tab_message = ""
        Budgie.Applet.__init__(self)
        self.uuid = uuid

        # applet appearance
        self.icon = Gtk.Image()
        self.icon.set_from_icon_name(
            "gnome-calculator", Gtk.IconSize.MENU
        )
        self.box = Gtk.EventBox()
        self.box.add(self.icon)
        self.add(self.box)
        self.popover = Budgie.Popover.new(self.box)
        
        self.calc = calc(False, True, True)
        self.popover.add(self.calc)

        self.box.show_all()
        self.show_all()
        self.box.connect("button-press-event", self.on_press)


    def on_press(self, box, arg):
        self.manager.show_popover(self.box)

    def do_update_popovers(self, manager):
        self.manager = manager
        self.manager.register_popover(self.box, self.popover)

    def do_supports_settings(self):
        """Return True if support setting through Budgie Setting,
        False otherwise.
        """
        return False
