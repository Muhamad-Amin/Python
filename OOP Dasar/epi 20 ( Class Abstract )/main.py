""" class abstract """

# abc = abstract base class

from abc import ABC, abstractmethod


class Button(ABC):
    @abstractmethod
    def click(self):
        # print("ini adalah button click")
        pass


class PushButton(Button):
    pass


tombol1 = PushButton()

tombol1.click()
