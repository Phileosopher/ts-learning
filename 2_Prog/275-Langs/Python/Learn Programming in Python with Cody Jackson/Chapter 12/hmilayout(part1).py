import sys
sys.path.extend(["/home/cody/PycharmProjects/VirtualPLC"])

import Models.FuelFarm.components as components
import Models.FuelFarm.functionality as functionality

from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.config import Config

import kivy
kivy.require("1.10.0")
