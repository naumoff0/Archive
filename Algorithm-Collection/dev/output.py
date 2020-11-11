import tkinter as tk
import sys
import threading
import queue


class Window(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

    def redirect(self):
        self.queue = queue.Queue()
        TextRedirector(self.queue).start()
        self.master.after(100, self.process_queue)
        sys.stdout = TextRedirector(self.text, "stdout")
        sys.stderr = TextRedirector(self.text, "stderr")


class TextRedirector(threading.Thread):
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)
        self.root.mainloop()

    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,))
        self.widget.configure(state="disabled")
