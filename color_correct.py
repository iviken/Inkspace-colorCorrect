#!/usr/bin/env python
# coding=utf-8
#
# Copyright (C) [YEAR] [YOUR NAME], [YOUR EMAIL]
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#

from email.policy import default
import inkex

class ColorCorrect(inkex.ColorExtension):
    def add_arguments(self, pars):
        pars.add_argument("--R_channel", type=int, default=0, help="Red")
        pars.add_argument("--G_channel", type=int, default=0, help="Red")
        pars.add_argument("--B_channel", type=int, default=0, help="Red")
        pars.add_argument("--flag_toAll", type=inkex.Boolean, dest="flag_toAll")

    def modify_color(self, name, color):
        if self.options.flag_toAll:
            color.red += int(self.options.R_channel)
            color.green += int(self.options.G_channel)
            color.blue += int(self.options.B_channel)

        return color

if __name__ == '__main__':
    ColorCorrect().run()
