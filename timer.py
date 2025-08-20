import tkinter as tk
from tkinter import ttk
import time
import platform

# --- Optional: sound handling based on OS ---
if platform.system() == "Windows":
    import winsound

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")
        self.master.geometry("400x300")
        self.master.configure(bg="#2c3e50")

        self.is_running = False
        self.is_paused = False
        self.current_cycle = "work"
        self.work_time = 25 * 60  # 25 minutes
        self.break_time = 5 * 60  # 5 minutes
        self.time_left = self.work_time

        # --- Frames ---
        self.header_frame = tk.Frame(master, bg="#2c3e50")
        self.header_frame.pack(pady=10)

        self.timer_frame = tk.Frame(master, bg="#2c3e50")
        self.timer_frame.pack(pady=20)

        self.button_frame = tk.Frame(master, bg="#2c3e50")
        self.button_frame.pack(pady=10)

        # --- Widgets ---
        self.header_label = tk.Label(self.header_frame, text="Pomodoro Timer", font=("Helvetica", 20, "bold"), fg="#ecf0f1", bg="#2c3e50")
        self.header_label.pack()

        self.status_label = tk.Label(self.timer_frame, text=" เวลาทำงาน ", font=("Helvetica", 16), fg="#f39c12", bg="#2c3e50")
        self.status_label.pack()

        self.time_label = tk.Label(self.timer_frame, text=self.format_time(self.time_left), font=("Helvetica", 48, "bold"), fg="#ecf0f1", bg="#2c3e50")
        self.time_label.pack(pady=10)

        self.current_time_label = tk.Label(self.header_frame, font=("Helvetica", 12), fg="#7f8c8d", bg="#2c3e50")
        self.current_time_label.pack(side="right", anchor="ne", padx=10)
        self.update_current_time()

        self.start_button = ttk.Button(self.button_frame, text="เริ่มนับถอยหลัง", command=self.start_timer)
        self.start_button.grid(row=0, column=0, padx=5)

        self.pause_button = ttk.Button(self.button_frame, text="หยุดชั่วคราว", command=self.pause_timer)
        self.pause_button.grid(row=0, column=1, padx=5)

        self.reset_button = ttk.Button(self.button_frame, text="รีเซ็ต", command=self.reset_timer)
        self.reset_button.grid(row=0, column=2, padx=5)

    def format_time(self, seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

    def update_current_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.current_time_label.config(text=f"เวลาปัจจุบัน: {current_time}")
        self.master.after(1000, self.update_current_time)

    def start_timer(self):
        if not self.is_running:
            self.is_running = True
            self.is_paused = False
            self.start_button.config(text="กำลังนับถอยหลัง")
            self.countdown()

    def pause_timer(self):
        if self.is_running:
            self.is_paused = True
            self.is_running = False
            self.start_button.config(text="เริ่มนับต่อ")

    def reset_timer(self):
        self.is_running = False
        self.is_paused = False
        self.current_cycle = "work"
        self.time_left = self.work_time
        self.time_label.config(text=self.format_time(self.time_left))
        self.status_label.config(text="Work Time", fg="#f39c12")
        self.start_button.config(text="Start")

    def countdown(self):
        if self.is_running and not self.is_paused:
            if self.time_left > 0:
                self.time_left -= 1
                self.time_label.config(text=self.format_time(self.time_left))
                self.master.after(1000, self.countdown)
            else:
                self.switch_cycle()

    def play_alert_sound(self):
        if platform.system() == "Windows":
            winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
        else:
            print('\a')  # Terminal/system beep for Linux/macOS

    def switch_cycle(self):
        self.play_alert_sound()

        if self.current_cycle == "work":
            self.current_cycle = "break"
            self.time_left = self.break_time
            self.status_label.config(text="Break Time", fg="#2ecc71")
        else:
            self.current_cycle = "work"
            self.time_left = self.work_time
            self.status_label.config(text="Work Time", fg="#f39c12")

        self.time_label.config(text=self.format_time(self.time_left))
        self.is_running = False
        self.start_timer()

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
