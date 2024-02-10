from gui_fcatory import  WindowsFactory, MacOSFactory, LinuxFactory, Application
import sys

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
