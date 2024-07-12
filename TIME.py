#1.0
import tkinter as tk
import time
import threading

class TimeViewer(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.time_label = tk.Label(self, font=("Helvetica", 48), fg="black", bg="white")
        self.time_label.pack()

        self.update_clock()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.time_label.config(text=current_time)
        self.after(1000, self.update_clock)

class Timer(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.start_button = tk.Button(self, text="开始计时", command=self.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(self, text="停止计时", command=self.stop_timer)
        self.stop_button.pack()

        self.elapsed_time_label = tk.Label(self, font=("Helvetica", 24), fg="black", bg="white")
        self.elapsed_time_label.pack()

        self.timer_running = False
        self.start_time = 0
        self.elapsed_time = 0

    def start_timer(self):
        if not self.timer_running:
            self.start_time = time.time()
            self.timer_running = True
            threading.Thread(target=self.run_timer).start()

    def run_timer(self):
        while self.timer_running:
            self.elapsed_time = time.time() - self.start_time
            time_str = f"经过时间: {self.format_time(self.elapsed_time)}"
            self.elapsed_time_label.config(text=time_str)
            time.sleep(1)

    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False

    def format_time(self, seconds):
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        seconds = int(seconds % 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

class ClockApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("时钟")

        self.time_viewer = TimeViewer(self)
        self.time_viewer.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.timer = Timer(self)
        self.timer.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

if __name__ == "__main__":
    app = ClockApp()
    app.mainloop()