from Notepad import *


def main() -> None:
    # Create Notepad instance
    notepad = Notepad()

    # Keep the window running until the user closes
    notepad.window.mainloop()


if __name__ == '__main__':
    main()
