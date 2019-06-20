import tkinter as tk
import json
from difflib import get_close_matches

window = tk.Tk()  # Creates Main Window
window.title("Dictionary Search Application")

dictionary = json.load(open("data_dictionary.json"))

similar_word = None


def find_word():
    w = word_to_search.get()
    w = w.lower()
    if w in dictionary:
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, dictionary[w])
    elif w.title() in dictionary:
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, dictionary[w.title()])
    elif w.upper() in dictionary:
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, dictionary[w.upper()])
    elif len(get_close_matches(w, dictionary.keys())) > 0:
        global similar_word
        similar_word = get_close_matches(w, dictionary.keys())[0]
        i_string = "Did you mean %s instead? Press Yes or No: " % similar_word
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, i_string)

    else:
        text_area.delete("1.0", tk.END)
        text_area.insert(
            tk.END, "The word doesn't exist. Please double check it!")


def press_y():
    if similar_word is None:
        no_similar_word()
    else:
        text_area.delete("1.0", tk.END)
        text_area.insert(tk.END, dictionary[similar_word])


def press_n():
    if similar_word is None:
        no_similar_word()
    else:
        text_area.delete("1.0", tk.END)
        text_area.insert(
            tk.END, "The word doesn't exist. Please double check it!")


def no_similar_word():
    text_area.delete("1.0", tk.END)
    text_area.insert(
        tk.END, "What are you doing! There has been no word suggested!")


label_heading = tk.Label(
    window, text="Dictionary Application", font="Times 16 bold")
label_heading.grid(row=0, column=0, columnspan=9)

label_search = tk.Label(window, text="Word to Search:")
label_search.grid(row=1, column=0, columnspan=2)

word_to_search = tk.StringVar()
entry_search = tk.Entry(window, textvariable=word_to_search)
entry_search.grid(row=1, column=2, columnspan=2)

button_search = tk.Button(window, text="GO!", width=10, command=find_word)
button_search.grid(row=1, column=4, columnspan=2)

button_Y = tk.Button(window, text="Yes!", width=10, command=press_y)
button_Y.grid(row=1, column=6, columnspan=2)

button_N = tk.Button(window, text="No!", width=10, command=press_n)
button_N.grid(row=1, column=8, columnspan=2)

text_area = tk.Text(window, height=5, width=58)
text_area.grid(row=2, column=0, columnspan=9)

window.geometry("480x150+750+300")
window.mainloop()  # Keeps the window open
