#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Video

"""


class Video:
    """
    Video class

    """

    def __init__(self):
        self.width = 520
        self.height = 1080
        self.show_progress = False
        self.name = "clip"
        self.format = "mov"
        self.path_o = "media/original/"
        self.path_c = "media/cropped/"

    def get_aspect_ratio(self):
        """
        get_aspect_ratio
        """

        return (self.width, self.height)

    def set_aspect_ratio(self, width, height):
        """
        set_aspect_ratio
        """

        self.width = width
        self.height = height


video = Video()
