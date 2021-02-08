#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  JARVIS_2.0.py
#  
#  Copyright 2021 DARK2 <dark2@DARK2-PC>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from vosk import Model, KaldiRecognizer
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QMovie
from plyer import notification
import speech_recognition as sr
import os
import pyaudio
import pyttsx3
import sys
import datetime
import psutil
import webbrowser
import vlc
import json
import requests
import time
import wikipedia


