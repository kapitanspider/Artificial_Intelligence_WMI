#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from pygame.locals import *


class Bomb:
    def __init__(self, priority, type):
        self.priority = priority
        self.type = type

    def priority(self):
        return self.priority
