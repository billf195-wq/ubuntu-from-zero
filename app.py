#!/usr/bin/env python3
"""Ubuntu From Zero — local Tkinter lesson browser (stdlib + Tk only)."""
from __future__ import annotations

import tkinter as tk
from tkinter import ttk, messagebox
import webbrowser
from pathlib import Path

from lessons import CATEGORIES, LESSONS, filter_lessons, get_lesson

ROOT = Path(__file__).resolve().parent
ORANGE = "#E95420"
ORANGE_DARK = "#c7471b"


class Theme:
    def __init__(self, mode: str = "dark"):
        self.mode = mode
        self.apply()

    def apply(self):
        if self.mode == "dark":
            self.bg = "#1a1a1a"
            self.card = "#242424"
            self.fg = "#f0f0f0"
            self.muted = "#aaaaaa"
            self.entry_bg = "#2a2a2a"
            self.list_bg = "#1e1e1e"
            self.select_bg = "#3d2018"
        else:
            self.bg = "#f6f5f4"
            self.card = "#ffffff"
            self.fg = "#2c2c2c"
            self.muted = "#666666"
            self.entry_bg = "#ffffff"
            self.list_bg = "#ffffff"
            self.select_bg = "#ffe8df"
        self.accent = ORANGE


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Ubuntu From Zero — Developed by Bill Foster")
        self.geometry("960x640")
        self.minsize(720, 480)
        self.theme = Theme("dark")
        self.selected_id = None
        self._build()
        self._apply_theme()
        self.refresh_list()

    def _build(self):
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        top = ttk.Frame(self, padding=8)
        top.grid(row=0, column=0, sticky="ew")
        top.columnconfigure(2, weight=1)

        title_col = ttk.Frame(top)
        title_col.grid(row=0, column=0, padx=(0, 12), sticky="w")
        ttk.Label(title_col, text="Ubuntu From Zero", font=("Ubuntu", 14, "bold")).pack(anchor="w")
        ttk.Label(title_col, text="Developed by Bill Foster", font=("Ubuntu", 9)).pack(anchor="w")
        self.cat_var = tk.StringVar(value="all")
        self.cat = ttk.Combobox(
            top,
            textvariable=self.cat_var,
            values=[c[0] for c in CATEGORIES],
            state="readonly",
            width=16,
        )
        self.cat.grid(row=0, column=1, padx=4)
        self.cat.bind("<<ComboboxSelected>>", lambda e: self.refresh_list())
        # Show friendly labels via map
        self._cat_labels = dict(CATEGORIES)
        self.cat_display = ttk.Combobox(
            top,
            values=[c[1] for c in CATEGORIES],
            state="readonly",
            width=22,
        )
        self.cat_display.set("All lessons")
        self.cat_display.grid(row=0, column=1, padx=4)
        self.cat_display.bind("<<ComboboxSelected>>", self._on_cat)
        self.cat.grid_remove()

        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *_: self.refresh_list())
        self.search = ttk.Entry(top, textvariable=self.search_var)
        self.search.grid(row=0, column=2, sticky="ew", padx=8)
        self.search.insert(0, "")
        ttk.Label(top, text="Search").grid(row=0, column=3)
        self.theme_btn = ttk.Button(top, text="Light / Dark", command=self.toggle_theme)
        self.theme_btn.grid(row=0, column=4, padx=4)

        paned = ttk.Panedwindow(self, orient=tk.HORIZONTAL)
        paned.grid(row=1, column=0, sticky="nsew", padx=8, pady=8)

        left = ttk.Frame(paned)
        right = ttk.Frame(paned)
        paned.add(left, weight=1)
        paned.add(right, weight=2)

        left.rowconfigure(0, weight=1)
        left.columnconfigure(0, weight=1)
        self.listbox = tk.Listbox(left, activestyle="dotbox", exportselection=False)
        self.listbox.grid(row=0, column=0, sticky="nsew")
        scroll = ttk.Scrollbar(left, orient=tk.VERTICAL, command=self.listbox.yview)
        scroll.grid(row=0, column=1, sticky="ns")
        self.listbox.configure(yscrollcommand=scroll.set)
        self.listbox.bind("<<ListboxSelect>>", self._on_select)

        right.rowconfigure(2, weight=1)
        right.columnconfigure(0, weight=1)
        self.title_lbl = ttk.Label(right, text="Select a lesson", font=("Ubuntu", 16, "bold"))
        self.title_lbl.grid(row=0, column=0, sticky="w", pady=(0, 4))
        self.meta_lbl = ttk.Label(right, text="")
        self.meta_lbl.grid(row=1, column=0, sticky="w", pady=(0, 8))

        self.detail = tk.Text(right, wrap=tk.WORD, height=20, relief=tk.FLAT, padx=8, pady=8)
        self.detail.grid(row=2, column=0, sticky="nsew")
        self.detail.configure(state=tk.DISABLED)

        btns = ttk.Frame(right)
        btns.grid(row=3, column=0, sticky="ew", pady=(8, 0))
        self.open_btn = ttk.Button(btns, text="Open full lesson", command=self.open_lesson, state=tk.DISABLED)
        self.open_btn.pack(side=tk.LEFT)
        ttk.Label(btns, text="  Opens html/lessons/… in your browser (file://)").pack(side=tk.LEFT)

        status = ttk.Frame(self, padding=4)
        status.grid(row=2, column=0, sticky="ew")
        self.status = ttk.Label(status, text=f"{len(LESSONS)} lessons · {ROOT}")
        self.status.pack(side=tk.LEFT)

        self._visible = []

    def _on_cat(self, _event=None):
        label = self.cat_display.get()
        for key, lab in CATEGORIES:
            if lab == label:
                self.cat_var.set(key)
                break
        self.refresh_list()

    def refresh_list(self):
        cat = self.cat_var.get() or "all"
        q = self.search_var.get()
        self._visible = filter_lessons(cat, q)
        self.listbox.delete(0, tk.END)
        for lesson in self._visible:
            self.listbox.insert(tk.END, f'{lesson["num"]:02d}. {lesson["title"]}')
        self.status.configure(text=f"{len(self._visible)} shown · {len(LESSONS)} total")

    def _on_select(self, _event=None):
        sel = self.listbox.curselection()
        if not sel:
            return
        lesson = self._visible[sel[0]]
        self.selected_id = lesson["id"]
        self.title_lbl.configure(text=lesson["title"])
        self.meta_lbl.configure(text=f'Lesson {lesson["num"]} · {lesson["level_label"]}')
        text = lesson["summary"] + "\n\nSteps:\n"
        for i, step in enumerate(lesson["steps"], 1):
            text += f"  {i}. {step}\n"
        self.detail.configure(state=tk.NORMAL)
        self.detail.delete("1.0", tk.END)
        self.detail.insert("1.0", text)
        self.detail.configure(state=tk.DISABLED)
        self.open_btn.configure(state=tk.NORMAL)

    def open_lesson(self):
        if not self.selected_id:
            return
        lesson = get_lesson(self.selected_id)
        if not lesson:
            return
        path = ROOT / lesson["html_file"]
        if not path.is_file():
            messagebox.showerror("Missing file", f"Lesson HTML not found:\n{path}")
            return
        webbrowser.open(path.as_uri())

    def toggle_theme(self):
        self.theme.mode = "light" if self.theme.mode == "dark" else "dark"
        self.theme.apply()
        self._apply_theme()

    def _apply_theme(self):
        t = self.theme
        self.configure(bg=t.bg)
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except tk.TclError:
            pass
        style.configure(".", background=t.bg, foreground=t.fg, fieldbackground=t.entry_bg)
        style.configure("TFrame", background=t.bg)
        style.configure("TLabel", background=t.bg, foreground=t.fg)
        style.configure("TButton", background=t.accent, foreground="#ffffff", padding=6)
        style.map("TButton", background=[("active", ORANGE_DARK)])
        style.configure("TCombobox", fieldbackground=t.entry_bg, background=t.card, foreground=t.fg)
        style.configure("TEntry", fieldbackground=t.entry_bg, foreground=t.fg)
        style.configure("TPanedwindow", background=t.bg)
        self.listbox.configure(
            bg=t.list_bg,
            fg=t.fg,
            selectbackground=t.accent,
            selectforeground="#ffffff",
            highlightthickness=0,
            borderwidth=0,
            font=("Ubuntu", 11),
        )
        self.detail.configure(
            bg=t.card,
            fg=t.fg,
            insertbackground=t.fg,
            font=("Ubuntu", 11),
        )


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
