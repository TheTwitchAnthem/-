import webbrowser
from urllib.parse import quote


class ProcessResearcher:
    def __init__(self):
        self.search_engines = [
            "https://www.google.com/search?q=",
            "https://www.bing.com/search?q=",
            "https://duckduckgo.com/?q="
        ]

    def research_processes(self, processes):
        """Ищет информацию о процессах в браузере"""
        for process in processes:
            query = f"Что за процесс {process} Windows"
            self.search_in_browser(query)

    def search_in_browser(self, query):
        """Открывает поиск в браузере"""
        encoded_query = quote(query)
        for engine in self.search_engines:
            webbrowser.open_new_tab(engine + encoded_query)