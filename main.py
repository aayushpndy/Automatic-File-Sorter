import tkinter as tk
from tkinter import filedialog
import index
import webbrowser
from PIL import Image, ImageTk

# ---------------------------------------------------------------------------
# COLORS
# ---------------------------------------------------------------------------
BG_PAGE      = "#eef2f8"
NAVY         = "#10275c"
GRAY_TEXT    = "#5b6472"
CARD_BORDER  = "#e2e6ee"
WHITE        = "#ffffff"
BLUE_BTN     = "#2f6fed"
BLUE_BTN_HV  = "#2560d6"
DARK_BTN     = "#13224a"
GREEN_PILL_BG= "#e5f7ea"
GREEN_PILL_FG= "#1e9e4c"
TOTAL_BG     = "#e9f1fd"
INFO_BG      = "#eaf3ff"

# icon colors per category (matches the reference image)
CARD_META = {
    "image":        ("🖼",  "Image Files",        "#22a35d"),
    "video":        ("🎬",  "Video Files",        "#e0483c"),
    "text":         ("📄",  "Text Files",         "#2f7ed8"),
    "audio":        ("🎵",  "Audio Files",        "#8a5cf6"),
    "presentation": ("🖥",  "Presentation Files", "#e08a2b"),
    "compressed":   ("🗜",  "Compressed Files",   "#e0b32b"),
    "programme":    ("</>", "Programme Files",    "#8a5cf6"),
    "web":          ("🌐",  "Web Files",          "#2f7ed8"),
    "document":     ("📑",  "Document Files",     "#159e8f"),
    "spreadsheet":  ("📊",  "Spreadsheet Files",  "#22a35d"),
}

# order of the 10 small cards, 5 per row (matches the photo layout)
CARD_ORDER = ["image", "video", "text", "audio", "presentation",
              "compressed", "programme", "web", "document", "spreadsheet"]


# ---------------------------------------------------------------------------
# ROOT WINDOW
# ---------------------------------------------------------------------------
root = tk.Tk()
root.title("Automatic File Sorter")
root.geometry("1000x700")
root.configure(bg=BG_PAGE)
root.minsize(900, 650)

# ---------------------------------------------------------------------------
# HEADER
# ---------------------------------------------------------------------------
header = tk.Frame(root, bg=BG_PAGE)
header.pack(pady=(40, 10))

title_label = tk.Label(
    header, text="Automatic File Sorter",
    font=("Segoe UI", 28, "bold"), fg=NAVY, bg=BG_PAGE
)
title_label.pack()

subtitle_label = tk.Label(
    header, text="Select a folder to automatically sort your files into organized categories.",
    font=("Segoe UI", 11), fg=GRAY_TEXT, bg=BG_PAGE
)
subtitle_label.pack(pady=(5, 0))

# ---------------------------------------------------------------------------
# FOLDER SELECT ROW
# ---------------------------------------------------------------------------
path_row = tk.Frame(root, bg=BG_PAGE)
path_row.pack(pady=20)

entry_frame = tk.Frame(path_row, bg=WHITE, highlightbackground=CARD_BORDER,
                        highlightthickness=1)
entry_frame.pack(side="left", ipady=10)

tk.Label(entry_frame, text="📁", bg=WHITE, font=("Segoe UI", 11)).pack(side="left", padx=(15, 5))

entry = tk.Entry(entry_frame, width=55, font=("Segoe UI", 11),
                  bd=0, bg=WHITE, fg="#333333")
entry.pack(side="left", ipady=4, padx=(0, 15))
entry.insert(0, "")


def browse_folder():
    folder = filedialog.askdirectory()
    if folder:
        entry.delete(0, tk.END)
        entry.insert(0, folder)


browse_btn = tk.Button(
    path_row, text="📁  Browse", command=browse_folder,
    bg=DARK_BTN, fg=WHITE, activebackground=DARK_BTN, activeforeground=WHITE,
    font=("Segoe UI", 11, "bold"), bd=0, padx=20, pady=12, cursor="hand2"
)
browse_btn.pack(side="left", padx=(10, 0))

# ---------------------------------------------------------------------------
# CLICK TO SORT BUTTON
# ---------------------------------------------------------------------------
sort_btn_frame = tk.Frame(root, bg=BG_PAGE)
sort_btn_frame.pack(pady=10)


def on_enter(e):
    sort_button.config(bg=BLUE_BTN_HV)


def on_leave(e):
    sort_button.config(bg=BLUE_BTN)


sort_button = tk.Button(
    sort_btn_frame, text="≡  Click to Sort", command=lambda: sortFiles(),
    bg=BLUE_BTN, fg=WHITE, activebackground=BLUE_BTN_HV, activeforeground=WHITE,
    font=("Segoe UI", 12, "bold"), bd=0, padx=40, pady=14, cursor="hand2"
)
sort_button.pack()
sort_button.bind("<Enter>", on_enter)
sort_button.bind("<Leave>", on_leave)

# ---------------------------------------------------------------------------
# SORTING SUMMARY PANEL
# ---------------------------------------------------------------------------
summary_panel = tk.Frame(root, bg=WHITE, highlightbackground=CARD_BORDER,
                          highlightthickness=1)
summary_panel.pack(pady=(20, 0), padx=80, fill="both", expand=True)

summary_header = tk.Frame(summary_panel, bg=WHITE)
summary_header.pack(fill="x", padx=25, pady=(20, 10))

tk.Label(summary_header, text="📶  Sorting Summary", font=("Segoe UI", 13, "bold"),
          fg=NAVY, bg=WHITE).pack(side="left")

status_pill = tk.Label(
    summary_header, text="", font=("Segoe UI", 10, "bold"),
    fg=GREEN_PILL_FG, bg=GREEN_PILL_BG, padx=12, pady=4
)
status_pill.pack(side="right")

tk.Frame(summary_panel, bg=CARD_BORDER, height=1).pack(fill="x")

cards_area = tk.Frame(summary_panel, bg=WHITE)
cards_area.pack(fill="both", expand=True, padx=25, pady=20)
for c in range(6):
    cards_area.grid_columnconfigure(c, weight=1)

# ---------------------------------------------------------------------------
# INFO / STATUS BAR
# ---------------------------------------------------------------------------
info_bar = tk.Frame(root, bg=INFO_BG, highlightbackground="#cfe2fb", highlightthickness=1)
info_bar.pack(pady=20, padx=80, fill="x")

info_label = tk.Label(
    info_bar, text="", font=("Segoe UI", 10), fg="#2f5fae", bg=INFO_BG
)
info_label.pack(pady=12)


# ---------------------------------------------------------------------------
# CARD BUILDERS
# ---------------------------------------------------------------------------
def make_total_card(parent, total):
    card = tk.Frame(parent, bg=TOTAL_BG, highlightbackground="#c9ddf8",
                     highlightthickness=1)
    tk.Label(card, text="Total Files", font=("Segoe UI", 11), fg=BLUE_BTN,
             bg=TOTAL_BG).pack(pady=(20, 5))
    tk.Label(card, text=str(total), font=("Segoe UI", 30, "bold"), fg=BLUE_BTN,
             bg=TOTAL_BG).pack()
    tk.Label(card, text="Files sorted successfully", font=("Segoe UI", 9),
             fg=GRAY_TEXT, bg=TOTAL_BG).pack(pady=(5, 10))
    tk.Label(card, text="📁", font=("Segoe UI", 20), fg=BLUE_BTN,
             bg=TOTAL_BG).pack(pady=(0, 20))
    return card


def make_category_card(parent, icon, name, count, color):
    card = tk.Frame(parent, bg=WHITE, highlightbackground=CARD_BORDER,
                     highlightthickness=1)
    tk.Label(card, text=name, font=("Segoe UI", 10, "bold"), fg="#333333",
             bg=WHITE).pack(pady=(18, 8), padx=15, anchor="w")
    row = tk.Frame(card, bg=WHITE)
    row.pack(pady=(0, 18), padx=15, anchor="w")
    tk.Label(row, text=icon, font=("Segoe UI", 14), fg=color, bg=WHITE).pack(side="left")
    tk.Label(row, text=str(count), font=("Segoe UI", 16, "bold"), fg="#333333",
             bg=WHITE).pack(side="left", padx=(10, 0))
    return card


# ---------------------------------------------------------------------------
# MAIN LOGIC (unchanged from the original — only presentation is new)
# ---------------------------------------------------------------------------
def sortFiles():
    location = entry.get()          # t,i,v,a,,ps,c,pg,w,d,s
    result = index.Sort(location)

    # clear previous summary
    for widget in cards_area.winfo_children():
        widget.destroy()

    if result["success"]:
        total = (result['text'] + result['image'] + result['video'] + result['audio']
                  + result['presentation'] + result['compressed'] + result['programme']
                  + result['web'] + result['document'] + result['spreadsheet'])

        status_pill.config(text="✓ Completed")

        # total card spans column 0, both rows
        total_card = make_total_card(cards_area, total)
        total_card.grid(row=0, column=0, rowspan=2, sticky="nsew", padx=8, pady=8)

        # remaining 10 category cards, 5 per row, columns 1-5
        for i, key in enumerate(CARD_ORDER):
            row = i // 5
            col = 1 + (i % 5)
            icon, name, color = CARD_META[key]
            count = result.get(key, 0)
            card = make_category_card(cards_area, icon, name, count, color)
            card.grid(row=row, column=col, sticky="nsew", padx=8, pady=8)

        info_label.config(text="ℹ️  Your files have been sorted into their respective folders.")
    else:
        status_pill.config(text="")
        info_label.config(text=result['message'])
def sortFiles():
    location = entry.get().strip()

    # Clear previous cards
    for widget in cards_area.winfo_children():
        widget.destroy()

    # Empty path
    if not location:
        status_pill.config(
            text="✕ Error",
            bg="#ffe8e8",
            fg="red"
        )
        info_label.config(text="Please select or enter a folder path.")
        return

    result = index.Sort(location)

    if result["success"]:

        status_pill.config(
            text="✓ Completed",
            bg=GREEN_PILL_BG,
            fg=GREEN_PILL_FG
        )

        total = sum(result.get(key, 0) for key in CARD_ORDER)

        total_card = make_total_card(cards_area, total)
        total_card.grid(
            row=0,
            column=0,
            rowspan=2,
            sticky="nsew",
            padx=8,
            pady=8
        )

        visible_cards = []

        for key in CARD_ORDER:
            count = result.get(key, 0)
            if count > 0:
                visible_cards.append((key, count))

        for i, (key, count) in enumerate(visible_cards):
            row = i // 5
            col = 1 + (i % 5)

            icon, name, color = CARD_META[key]

            card = make_category_card(
                cards_area,
                icon,
                name,
                count,
                color
            )

            card.grid(
                row=row,
                column=col,
                sticky="nsew",
                padx=8,
                pady=8
            )

        info_label.config(
            text=f"✔ Successfully sorted {total} files."
        )

    else:

        status_pill.config(
            text="✕ Error, Please Insert Correct Path",
            bg="#ffe8e8",
            fg="red"
        )

        info_label.config(
            text=result["message"]
        )

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

def open_github(event=None):
    webbrowser.open("https://github.com/aayushpndy")

def open_linkedin(event=None):
    webbrowser.open("https://www.linkedin.com/in/aayush-pandey-867350407/")

def open_email(event=None):
    webbrowser.open("mailto:aayushpandey606@gmail.com")


footer = tk.Frame(root, bg=BG_PAGE)
footer.pack(side="bottom", pady=(5,15))

tk.Label(
    footer,
    text="Made by Aayush Pandey",
    font=("Segoe UI",15),
    fg="#666666",
    bg=BG_PAGE
).pack()

icons = tk.Frame(footer, bg=BG_PAGE)
icons.pack(pady=6)

github_icon = ImageTk.PhotoImage(Image.open("assets/icons/github.png").resize((20,20)))
linkedin_icon = ImageTk.PhotoImage(Image.open("assets/icons/linkedin.png").resize((23,23)))
gmail_icon = ImageTk.PhotoImage(Image.open("assets/icons/gmail.png").resize((20,20)))

github = tk.Label(
    icons,
    image=github_icon,
    bg=BG_PAGE,
    cursor="hand2"
)
github.pack(side="left", padx=12)
github.bind("<Button-1>", open_github)

linkedin = tk.Label(
    icons,
    image=linkedin_icon,
    bg=BG_PAGE,
    cursor="hand2"
)
linkedin.pack(side="left", padx=12)
linkedin.bind("<Button-1>", open_linkedin)

gmail = tk.Label(
    icons,
    image=gmail_icon,
    bg=BG_PAGE,
    cursor="hand2"
)
gmail.pack(side="left", padx=12)
gmail.bind("<Button-1>", open_email)

root.mainloop()