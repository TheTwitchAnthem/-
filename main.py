import json
import psutil
import webbrowser
from tkinter import Tk, Label, Listbox, Scrollbar, Frame, StringVar, messagebox
import tkinter as tk
from process_checker import ProcessChecker
from process_researcher import ProcessResearcher


class ProcessScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Process Scanner")
        self.root.geometry("800x600")

        # Инициализация модулей
        self.checker = ProcessChecker("process_db.json")
        self.researcher = ProcessResearcher()

        # GUI
        self.setup_ui()

    def setup_ui(self):
        main_frame = Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        Label(main_frame, text="Process Scanner", font=("Arial", 16)).pack(pady=10)

        # Вкладки
        notebook = tk.ttk.Notebook(main_frame)
        notebook.pack(fill=tk.BOTH, expand=True)

        # Вкладка активных процессов
        active_tab = Frame(notebook)
        self.setup_process_tab(active_tab, "Active Processes")
        notebook.add(active_tab, text="Active")

        # Вкладка приостановленных процессов
        suspended_tab = Frame(notebook)
        self.setup_process_tab(suspended_tab, "Suspended Processes")
        notebook.add(suspended_tab, text="Suspended")

        # Кнопки
        btn_frame = Frame(main_frame)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Scan All", command=self.scan_all).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Research Unknown", command=self.research_unknown).pack(side=tk.LEFT, padx=5)

        # Статус
        self.status_var = StringVar()
        Label(main_frame, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W).pack(fill=tk.X)

    def setup_process_tab(self, parent, title):
        Label(parent, text=title, font=("Arial", 12)).pack(pady=5)

        list_frame = Frame(parent)
        list_frame.pack(fill=tk.BOTH, expand=True)

        # Списки
        Label(list_frame, text="Malicious:").grid(row=0, column=0, sticky="w")
        self.malicious_list = Listbox(list_frame, width=40, height=10)
        self.malicious_list.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

        Label(list_frame, text="Unknown:").grid(row=0, column=1, sticky="w")
        self.unknown_list = Listbox(list_frame, width=40, height=10)
        self.unknown_list.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

        # Скроллбары
        for lst in [self.malicious_list, self.unknown_list]:
            scroll = Scrollbar(list_frame, command=lst.yview)
            scroll.grid(row=1, column=2, sticky="ns")
            lst.config(yscrollcommand=scroll.set)

    def scan_all(self):
        """Сканирует все типы процессов"""
        self.status_var.set("Scanning active processes...")
        active_procs = self.checker.get_active_processes()
        self.check_processes(active_procs, "Active")

        self.status_var.set("Scanning suspended processes...")
        suspended_procs = self.checker.get_suspended_processes()
        self.check_processes(suspended_procs, "Suspended")

        self.status_var.set("Scan completed")

    def check_processes(self, processes, process_type):
        """Анализирует процессы и выводит результаты"""
        malicious, unknown = self.checker.analyze_processes(processes)

        if process_type == "Active":
            self.update_list(self.malicious_list, malicious)
            self.update_list(self.unknown_list, unknown)
        else:
            # Для suspended можно добавить отдельные списки
            pass

    def update_list(self, list_widget, items):
        list_widget.delete(0, tk.END)
        for item in items:
            list_widget.insert(tk.END, item)

    def research_unknown(self):
        """Исследует неизвестные процессы"""
        unknown_procs = self.unknown_list.get(0, tk.END)
        if not unknown_procs:
            messagebox.showinfo("Info", "No unknown processes to research")
            return

        self.status_var.set("Researching unknown processes...")
        self.researcher.research_processes(unknown_procs)
        self.status_var.set("Research completed")


if __name__ == "__main__":
    root = Tk()
    app = ProcessScannerApp(root)
    root.mainloop()