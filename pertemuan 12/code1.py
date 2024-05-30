import tkinter as tk

root = tk.Tk()

# Latihan 1 : Membuat widget dasar
# widgetDasarku = tk.Tk()
# widgetDasarku.mainloop()

# Latihan 2 : Membuat Canvas
# Kanvasku = tk.Canvas(root, height = 1080, width=1920)
# Kanvasku.pack()

# Latihan 3 : Membuat Canvas
Frameku = tk.Frame(root, bg = 'pink')
Frameku.place(relwidth = 0.8, relheight = 0.8)

# Latihan 4a : Membuat button di root
# Tombolku = tk.Button(root, text = "Tes Tombol", bg = 'gray', fg = 'red')
# Tombolku.pack()

# Latihan 4b : Membuat Button di frame
Tombolku = tk.Button(Frameku, text = "Tes Tombol", bg = 'gray', fg ='red')
Tombolku.pack()

#latihan 5 L Mmebuat entry
Entryku = tk.Entry(Frameku, bg='white')
Entryku.pack()
root.mainloop()