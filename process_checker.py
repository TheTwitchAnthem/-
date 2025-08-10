import psutil
import json
import os


class ProcessChecker:
    def __init__(self):
        self.safe_db = self.load_db("save.json")
        self.danger_db = self.load_db("danger.json")

    def load_db(self, filename):
        """Загружает базу данных процессов из JSON файла"""
        try:
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return []
        except (json.JSONDecodeError, UnicodeDecodeError) as e:
            print(f"Error loading {filename}: {str(e)}")
            return []

    def get_active_processes(self):
        """Возвращает список активных процессов"""
        return [proc.info for proc in psutil.process_iter(['pid', 'name', 'status'])
                if proc.info['status'] == psutil.STATUS_RUNNING]

    def get_suspended_processes(self):
        """Возвращает список приостановленных процессов"""
        return [proc.info for proc in psutil.process_iter(['pid', 'name', 'status'])
                if proc.info['status'] == psutil.STATUS_STOPPED]

    def analyze_processes(self, processes):
        """Анализирует процессы и возвращает (dangerous, unknown)"""
        dangerous = []
        unknown = []

        for proc in processes:
            name = proc['name'].lower()

            if name in self.danger_db:
                dangerous.append(f"{name} (PID: {proc['pid']})")
            elif name not in self.safe_db:
                unknown.append(f"{name} (PID: {proc['pid']})")

        return dangerous, unknown