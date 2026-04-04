import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

f_name = 'student_data.csv'
cols = ['Roll', 'Name', 'CN', 'OOPS', 'DSA', 'DBMS', 'Total', 'Per', 'Grade', 'Status']

def start_file():
    if not os.path.exists(f_name):
        with open(f_name, "w", newline="") as f:
            w = csv.writer(f)
            w.writerow(cols)

class StudentSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("My School Project")
        self.root.geometry("1000x600")
        start_file()
        
        self.side = tk.Frame(self.root, bg="gray", width=150)
        self.side.pack(side="left", fill="y")
        
        self.body = tk.Frame(self.root, bg="white")
        self.body.pack(side="right", fill="both", expand=True)

        tk.Button(self.side, text="Dashboard", command=self.go_home, width=15).pack(pady=5)
        tk.Button(self.side, text="Add New", command=self.go_add, width=15).pack(pady=5)
        tk.Button(self.side, text="View List", command=self.go_view, width=15).pack(pady=5)
        tk.Button(self.side, text="Delete", command=self.go_del, width=15).pack(pady=5)
        tk.Button(self.side, text="Report Card", command=self.go_report, width=15).pack(pady=5)
        tk.Button(self.side, text="Summary", command=self.go_sum, width=15).pack(pady=5)
        
        self.go_home()

    def reset_body(self):
        for widget in self.body.winfo_children():
            widget.destroy()

    def go_home(self):
        self.reset_body()
        tk.Label(self.body, text="Student Management System", font=("Arial", 20)).pack(pady=20)
        tk.Label(self.body, text="Welcome to the main dashboard", font=("Arial", 12)).pack()

    def go_add(self):
        self.reset_body()
        tk.Label(self.body, text="Enter Student Details", font=("Arial", 15)).pack(pady=10)
        self.boxes = {}
        items = ["Roll", "Name", "CN", "OOPS", "DSA", "DBMS"]
        for i in items:
            row = tk.Frame(self.body)
            row.pack(pady=5)
            tk.Label(row, text=i, width=10).pack(side="left")
            ent = tk.Entry(row)
            ent.pack(side="left")
            self.boxes[i] = ent
        tk.Button(self.body, text="Save Now", command=self.save_it).pack(pady=20)

    def save_it(self):
        r_val = self.boxes["Roll"].get()
        n_val = self.boxes["Name"].get()
        try:
            m1, m2, m3, m4 = int(self.boxes["CN"].get()), int(self.boxes["OOPS"].get()), int(self.boxes["DSA"].get()), int(self.boxes["DBMS"].get())
            tot = m1 + m2 + m3 + m4
            per = tot / 4
            if per >= 80: g = "A"
            elif per >= 60: g = "B"
            elif per >= 40: g = "C"
            else: g = "F"
            res = "PASS" if all(x >= 35 for x in [m1, m2, m3, m4]) else "FAIL"
            with open(f_name, "a", newline="") as f:
                csv.writer(f).writerow([r_val, n_val, m1, m2, m3, m4, tot, per, g, res])
            messagebox.showinfo("Done", "Saved successfully")
            self.go_home()
        except:
            messagebox.showerror("Error", "Input error in marks")

    def go_view(self):
        self.reset_body()
        t = ttk.Treeview(self.body, columns=cols, show="headings")
        for c in cols:
            t.heading(c, text=c)
            t.column(c, width=80)
        try:
            with open(f_name, "r") as f:
                r = csv.reader(f)
                next(r)
                for row in r:
                    t.insert("", "end", values=row)
        except: pass
        t.pack(fill="both", expand=True)

    def go_del(self):
        self.reset_body()
        tk.Label(self.body, text="Delete a Student", font=("Arial", 15)).pack(pady=20)
        tk.Label(self.body, text="Enter Roll Number:").pack()
        self.d_ent = tk.Entry(self.body)
        self.d_ent.pack(pady=5)
        tk.Button(self.body, text="Delete Now", bg="red", fg="white", command=self.do_del).pack(pady=10)

    def do_del(self):
        rl = self.d_ent.get()
        rows = []
        found = False
        with open(f_name, "r") as f:
            reader = list(csv.reader(f))
            rows.append(reader[0])
            for r in reader[1:]:
                if r[0] == rl: found = True
                else: rows.append(r)
        if found:
            with open(f_name, "w", newline="") as f:
                csv.writer(f).writerows(rows)
            messagebox.showinfo("Success", "Deleted")
        else: messagebox.showerror("Error", "Not found")

    def go_report(self):
        self.reset_body()
        tk.Label(self.body, text="Generate Report Card", font=("Arial", 15)).pack(pady=20)
        self.r_ent = tk.Entry(self.body)
        self.r_ent.pack()
        tk.Button(self.body, text="Show Report", command=self.show_rep).pack(pady=10)
        self.rep_area = tk.Label(self.body, text="", font=("Courier", 10), justify="left")
        self.rep_area.pack(pady=20)

    def show_rep(self):
        rl = self.r_ent.get()
        with open(f_name, "r") as f:
            r = csv.reader(f)
            next(r)
            for row in r:
                if row[0] == rl:
                    txt = f"Name: {row[1]}\nRoll: {row[0]}\n----------\nTotal: {row[6]}\nPer: {row[7]}%\nGrade: {row[8]}\nStatus: {row[9]}"
                    self.rep_area.config(text=txt)
                    return
        messagebox.showerror("Error", "Student not in list")

    def go_sum(self):
        self.reset_body()
        tk.Label(self.body, text="Class Summary", font=("Arial", 15)).pack(pady=20)
        count = 0
        p_count = 0
        total_per = 0
        with open(f_name, "r") as f:
            r = csv.reader(f)
            next(r)
            for row in r:
                count += 1
                if row[9] == "PASS": p_count += 1
                total_per += float(row[7])
        
        if count > 0:
            avg = total_per / count
            tk.Label(self.body, text=f"Total Students: {count}").pack()
            tk.Label(self.body, text=f"Pass Percentage: {(p_count/count)*100}%").pack()
            tk.Label(self.body, text=f"Class Average: {avg}%").pack()
        else: tk.Label(self.body, text="No data").pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentSystem(root)
    root.mainloop()