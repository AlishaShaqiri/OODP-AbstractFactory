import sys

class GUIFactory:
    def create_button(self):
        pass

    def create_window(self):
        pass
class WindowsFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_window(self):
        return WindowsWindow()

class MacOSFactory(GUIFactory):
    def create_button(self):
        return MacOSButton()

    def create_window(self):
        return MacOSWindow()

class LinuxFactory(GUIFactory):
    def create_button(self):
        return LinuxButton()

    def create_window(self):
        return LinuxWindow()

class Button:
    def render(self):
        pass

class WindowsButton(Button):
    def render(self):
        print("Rendering a Windows-style button")

class MacOSButton(Button):
    def render(self):
        print("Rendering a macOS-style button")

class LinuxButton(Button):
    def render(self):
        print("Rendering a Linux-style button")

class Window:
    def render(self):
        pass

class WindowsWindow(Window):
    def render(self):
        print("Rendering a Windows-style window")

class MacOSWindow(Window):
    def render(self):
        print("Rendering a macOS-style window")

class LinuxWindow(Window):
    def render(self):
        print("Rendering a Linux-style window")

class Application:
    def __init__(self, factory):
        self.factory = factory

    def create_ui(self):
        button = self.factory.create_button()
        window = self.factory.create_window()

        button.render()
        window.render()

def main():
    if sys.platform == "win32":
        factory = WindowsFactory()
    elif sys.platform == "darwin":
        factory = MacOSFactory()
    else:
        factory = LinuxFactory()

    app = Application(factory)
    app.create_ui()

if __name__ == "__main__":
    main()
