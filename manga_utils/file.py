import configparser

from manga_utils.latest_manga import latest

manga_file = "manga.ini"
latest_chapter_key = "latest_chapter"
chapters_key = "chapters"

class Chapters:
    def __init__(self, manga ,chap_name, chapters):
        self.chap_name = chap_name
        self.chapters = chapters
        self.manga = manga

    def get_parser(self):
        config = configparser.ConfigParser()
        config.read(manga_file)
        return config

    def write_to_file(self):
        parser = self.get_parser()
        try:
            parser.add_section(self.manga)
        except configparser.DuplicateSectionError:
            pass

        parser.set(self.manga, latest_chapter_key, self.chap_name)
        parser.set(self.manga, chapters_key, str(self.chapters))

        with open(manga_file, "w") as manga_ini:
            parser.write(manga_ini)

    def compare(self):
        parser = self.get_parser()
        latest = parser.get(self.manga, latest_chapter_key)
        chapters = parser.get(self.manga, chapters_key)
        if self.chapters > int(chapters):
            print(latest)
            return True
        return False
        
    def check_entry(self):
        parser = self.get_parser()
        try:
            parser.add_section(self.manga)
            
        except configparser.DuplicateSectionError:
            return False
        return True



 