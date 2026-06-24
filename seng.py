import tkinter as tk
import random
import ctypes # For DPI awarness on Windows
try: 
    ctypes.windll.shcore.SetProcessDpiAwarness(1) # This basically just makes the app look better and removes the blurriness and low resolution
except:
    pass

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
    
}