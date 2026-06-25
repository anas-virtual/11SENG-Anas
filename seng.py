import tkinter as tk
import random
import ctypes # For DPI awarness on Windows
try: 
    ctypes.windll.shcore.SetProcessDpiAwarness(1) # This basically just makes the app look better and removes the blurriness and low resolution
except:
    pass
#This is a Nested Data Structure that contains all the lessons
LESSONS = {
    "Basic Phrases!": [
        ("Hello", "Namaste (नमस्ते)"),
        ("Thank you", "Dhanyavaad (धन्यवाद)"),
        ("Please", "Kripya (कृपया)"),
        ("Yes", "Haan (हाँ)"),
        ("No", "Nahi (नहीं)"),
        ("Sorry", "Maaf Karna (माफ़ करना)"),
        ("Good morning", "Suprabhat (सुप्रभात)"),
        ("Good night", "Shubh raatri (शुभ रात्रि)"),
        ("How are you?", "Aap kaise hain? (आप कैसे हैं?)"),
        ("My name is Anas", "Mera naam Anas hai (मेरा नाम Anas है)"),
    ],
    "Colours": [
        ("Red", "Laal (लाल)"),
        ("Blue", "Neela (नीला)"),
        ("Green", "Hara (हरा)"),
        ("Yellow", "Peela (पीला)"),
        ("White", "Shukla (शुक्ल)")
        ("Black", "Kaala (काला)"),
        ("Orange", "Narangi (नारंगी)"),
        ("Pink", "gulabi (गुलाबी)"),
        ("Purple", "Baingani (बैंगनी)"),
        ("Brown", "Bhoora (भूरा)"),
    ],
    "Family":[
        ("Mother", "Maa (माँ)"),
        ("Father", "Pita (पिता)"),
        ("Brother", "Bhai (भाई)"),
        ("Sister", "Behen (बहन)"),
        ("Grandmother", "Dadi (दादी)"),
        ("Grandfather", "Dada (दादा)"),
        ("Son", "Beta (बेटा)"),
        ("Daughter", "Beti (बेटी)"),
        ("Husband", "Pati (पति)"),
        ("Wife", "Patni (पत्नी)")
    ],
    "Numbers": [
        ("One", "Ek (एक)"),
        ("Two", "Do (दो)"),
        ("Three", "Teen (तीन)"),
        ("Four", "Chaar (चार)"),
        ("Five", "Paanch (पाँच)"),
        ("Six", "Chhah (छह)"),
        ("Seven", "Saat (सात)"),
        ("Eight", "Aath (आठ)"),
        ("Nine", "Nau (नौ)"),
        ("Ten", "Das (दस)")
    ],
    "Food & Drinks": [
        ("Water", "Paani (पानी)"),
        ("Food", "Khaana (खाना)"),
        ("Milk", "Doodh (दूध)"),
        ("Tea", "Chai (चाय)"),
        ("Sugar", "Cheeni (चीनी)"),
        ("Salt", "Namak (नमक)"),
        ("Rice", "Chawal (चावल)"),
        ("Bread", "Roti (रोटी)"),
        ("Vegetables", "Sabzi (सब्ज)")
        ("Fruits", "Phal (फल)"),
    ],
}
ALL_PAIRS = [(eng, hin) for pairs in LESSONS.values() for eng, hin in pairs] # This is a list of all the pairs in the LESSONS dictionary

class HindiApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Learn Hindi")
        self.geometry("480x600")
        self.resizable(False, False)

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for Page in (WelcomePage, MenuPage, LearnMenuPage, QuizPage, Resultspage):
            frame = Page(container, self)
            self.frames[Page] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(WelcomePage)

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        if hasattr(frame, "on_show"):
            frame.on_show()
        frame.tkraise()
    
    def open_lesson(self, topic):
        if "lesson" in self.frames:
            self.frames["lesson"].destroy()

        frame = LessonPage(self.frames[WelcomePage])
