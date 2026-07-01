from ast import Lambda
from tabnanny import check
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
        ("White", "Safed (सफेद)"),
        ("Black", "Kaala (काला)"),
        ("Orange", "Narangi (नारंगी)"),
        ("Pink", "Gulabi (गुलाबी)"),
    ],
    "Family":[
        ("Mother", "Maa (माँ)"),
        ("Father", "Pita (पिता)"),
        ("Brother", "Bhai (भाई)"),
        ("Sister", "Behen (बहन)"),
        ("Son", "Beta (बेटा)"),
        ("Daughter", "Beti (बेटी)"),
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
        ("Rice", "Chawal (चावल)"),
        ("Bread", "Roti (रोटी)"),
        ("Fruits", "Phal (फल)"),
    ],
}
ALL_PAIRS = [(e, h) for pairs in LESSONS.values() for e, h in pairs] # This is a list of all the pairs in the LESSONS dictionary

root =tk.Tk()
root.title("Learn Hindi!")
root.geometry("440x580")
root.resizable(False, False)

container =tk.Frame(root)
container.pack(fill="both", expand=True)

pages = {}

def show(name):
    pages[name].tkraise()

def make_page(name):
    f =tk.Frame(container)
    f.place(relwidth=1, relheight=1)
    pages[name] = f
    return f

pg = make_page("Welcome")
tk.Label(pg, text="Namaste!", font=("Arial", 60)).pack(pady=(80, 10))
tk.Label(pg, text="Learn Hindi", font=("Arial", 28, "bold")).pack()
tk.Label(pg, text="A fun way to learn everyday Hindi", font=("Arial", 12)).pack(pady=(6, 40))
tk.Button(pg, text="Get Started ->", font=("Arial", 14, "bold"), width=18, height=2, command=lambda: show("menu")).pack()

#Menu Page
pg = make_page("menu")
tk.Label(pg, text="What would you like to do?", font=("Arial", 16, "bold")).pack(pady=(80,30))
tk.Button(pg, text="Learn", font=("Arial", 14), width=20, height=3, command=lambda: show("learn_menu")).pack(pady=10)
tk.Button(pg, text="Quiz", font=("Arial", 14), width=20, height=3, command=lambda: start_quiz()).pack(pady=10)

#Learn Menu Page
pg=make_page("learn_menu")
tk.Label(pg, text="Choose a Topic", font=("Arial", 18, "bold")).pack(pady=(50,20))
for topic in LESSONS:
    tk.Button(pg, text=topic, font=("Arial", 13), width=22, height=2, command=lambda t=topic: open_lesson(t)).pack(pady=5)
    tk.Button(pg, text="<- Menu", font=("Arial", 11), width=12, command=lambda: show("menu")).pack(pady=(15,0))

#Lesson Page
lesson_data = {"pairs": [], "index": 0}
pg = make_page("lesson")
tk.Label(pg, text="", name="topic_lbl", font=("Arial", 20, "bold")).pack(pady=(30, 2))
tk.Label(pg, text="", name="counter_lbl", font=("Arial", 11)).pack()

card = tk.Frame(pg, relief="ridge", bd=2, padx=20, pady=20)
card.pack(pady=(15, 0), padx=40, fill="x")
tk.Label(card, text="", name="eng_lbl", font=("Arial", 22, "bold"), wraplength=340).pack(pady=(0,8))

nav = tk.Frame(pg); nav.pack()

def refresh_card():
    i, pairs = lesson_data["index"], lesson_data["pairs"]
    pages["lesson"].nametowidget("topic_lbl").config(text=lesson_data["topic"])
    pages["lesson"].nametowidget("counter_lbl").config(text=f"Card {i+1} of {len(pairs)}")
    card.nametowidget("eng_lbl").config(text=pairs[i][0])
    card.nametowidget("hin_lbl").config(text=pairs[i][1])

def open_lesson(topic):
    lesson_data.update({"topic": topic, "pairs": LESSONS[topic], "index":0})
    refresh_card()
    show("lesson")

tk.Button(nav, text="< Prev", width=10, command=lambda: [lesson_data.update({"index":(lesson_data["index"]-1)%len(lesson_data["pairs"])}), refresh_card()]).grid(row=0, column=0, padx=10)
tk.Button(pg, text="<- Menu", font=("Arial", 11), width=12, command=lambda: show("menu")).pack(pady=(15,0))

#Quiz Page
NUM_Q, NUM_OPT = 8,4
quiz = {"questions": [], "index": 0, "score": 0, "answered": False}

pg = make_page("quiz")
tk.Label(pg, text="Hindi Quiz", font=("Arial", 20, "bold")).pack(pady=(25,2))
q_progress = tk.Label(pg, font=("Arial", 11)); q_progress.pack()
q_score = tk.Label(pg, font=("Arial", 11)); q_score.pack()
q_text = tk.Label(pg, font=("Arial", 15, "bold"), wraplength=380, justify="center")
q_text.pack(pady=(15, 8))

opt_frame =tk.Frame(pg); opt_frame.pack()
opt_btns = [tk.Button(opt_frame, text="", font=("Arial", 11), width=32, height=2, command=lambda i=i: check(i)) for i in range(NUM_OPT)]
for b in opt_btns: b.pack(pady=3)

q_feedback = tk.Label(pg, font=("Arial", 12, "bold")); q_feedback.pack(pady=4)
next_btn = tk.Button(pg, text="Next ->", font=("Arial", 12), width=14, state="disabled")
next_btn.pack()
tk.Button(pg, text="<- Menu", font=("Arial", 11), width=12, command=lambda: show("menu")).pack(pady=(8, 0))

def build_questions():
    pool, qs = random.sample(ALL_PAIRS, NUM_Q), []
    for eng, correct in pool:
        wrong = random.sample([h for e, h in ALL_PAIRS if h != correct], NUM_OPT - 1)
        options = wrong + [correct]
        random.shuffle(options)
        qs.append({"prompt": f'What is the Hindi for:\n"{eng}"?', "options": options, "answer": options.index(correct)})
    return qs

def load_q():
    q = quiz["questions"][quiz["index"]]
    q_progress.config(text=f"Question {quiz['index']+1} of {NUM_Q}")
    q_score.config(text=f"Score: {quiz['score']} / {quiz['index']}")
    q_text.config(text=q["prompt"])
    q_feedback.config(text="")
    quiz["answered"] = False
    for i, b in enumerate(opt_btns):
        b.config(text=q["options"][1], state="normal")
    next_btn.config(state="disabled"), text=("Next ->") if quiz["index"] < NUM_Q - 1 else "See Results", command=advance)

def check(i):
    if quiz["answered"]: return
    quiz["answered"] = True
    correct = i == quiz["questions"][quiz["index"]]["answer"]
    if correct:
        quiz["score"] +=1
        q_feedback.config(text="Correct!", fg="green")
    else:
        ans = quiz["questions"][quiz["index"]]["options"][quiz["questions"][quiz["index"]]["answer"]]
        q_feedback.config(text=f"Wrong! ->", fg="red")
    for b in opt_btns: b.config(state="disabled")
    next_btn.config(state="normal")

def advance():
    quiz["index"] += 1
    if quiz["index"] < NUM_Q:
        load_q()
    else:
        show_results()

def start_quiz():
    quiz.update({"questions": build_questions(), "index": 0, "score": 0})
    load_q()
    show("quiz")

pg = make_page("results")
tk.Label(pg, text="Quiz Complete!", font=("Arial", 22, "bold")).pack(pady=(60,10))
res_trophy = tk.Label(pg, font=("Arial", 50)); res_trophy.pack(pady=8)
res_score = tk.Label(pg, font=("Arial", 16)); res_score.pack(pady=4)
res_msg = tk.Label(pg, font=("Arial", 13), wraplength=360); res_msg.pack(pady=8)
tk.Button(pg, text="Try Again", font=("Arial", 13), width=18, height=2, command=lambda: show("menu")).pack()

def show_results():
    pct = int(quiz["score"] / NUM_Q * 100)
    trophy, msg = ("Excellent! You're A Hindi Speaker!") if pct >= 80 else
    ("Good effort! Keep it up!") if pct >=50 else 
    ("Keep practising!")
    res_trophy.config(text=trophy)
    res_score.config(text=f"You scored {quiz['score']} / {NUM_Q} ({pct}%)")
    res_msg.config(text=msg)
    show("results")

#Start
show("welcome")
root.mainloop()
