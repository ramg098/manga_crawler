from manga_utils import latest_manga
from manga_utils import file
from manga_utils import notify


martial_peak = "Martial Peak"
def main():
    latest_chap, chapters = latest_manga.latest("https://ww5.manganelo.tv/manga/manga-bn978870")
    chapter = file.Chapters(martial_peak, latest_chap, chapters)
    check_entry = chapter.check_entry()
    if check_entry:
        chapter.write_to_file()
        print("added new entry ",martial_peak)
    new_chapter = chapter.compare()
    if new_chapter:
        print("new chapter available for ", martial_peak)
        chapter.write_to_file()
        notify.notify()

if __name__ == '__main__':
    main()