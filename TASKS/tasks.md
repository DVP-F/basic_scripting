# TASKS  

## **Project Briefs for Solo Projects**  

### **1. File Organizer Script**  

- **Difficulty**: Easy  
- **Language Options**: Python, PowerShell, Batch  
- **Goal**: Organize all files in a given folder into subfolders by extension.  
- **Bonus Challenge**: Add CLI flags: `--dry-run`, `--move`, `--copy`, and log actions taken.  
- **Recommended Python modules**: `os`, `shutil`, `argparse`  

**Python Starter Template:**

```python
import os, shutil, argparse

parser = argparse.ArgumentParser()
parser.add_argument("folder")
parser.add_argument("--dry-run", action="store_true")
args = parser.parse_args()

for file in os.listdir(args.folder):
   filepath = os.path.join(args.folder, file)
   if os.path.isfile(filepath):
      ext = file.split(".")[-1]
      dest_folder = os.path.join(args.folder, ext.upper())
      os.makedirs(dest_folder, exist_ok=True)
      if not args.dry_run:
        shutil.move(filepath, os.path.join(dest_folder, file))
      print(f"{'Would move' if args.dry_run else 'Moved'}: {file} -> {dest_folder}")
```

---

### **2. Disk Usage Reporter**  

- **Difficulty**: Medium  
- **Language**: PowerShell or Python  
- **Goal**: Display used, free, total space for each drive.  
- **PowerShell hint**: `Get-PSDrive -PSProvider 'FileSystem'`  

---

### **3. Simple Weather CLI**  

- **Difficulty**: Medium  
- **Language**: Python  
- **Goal**: Fetch weather from OpenWeatherMap API and show temperature, humidity, description.  
- **Modules**: `requests`, `json`  

---

## **Group Project Briefs**  

### **1. PC Health Check Toolkit (3 people)**  

- **Difficulty**: Advanced  
- **Part 1 (PowerShell)**: Script that:  
  - Lists running processes  
  - Checks if Windows is up-to-date  
  - Tests internet connectivity  
- **Part 2 (Python)**: Script that:  
  - Reports CPU, RAM usage, and disk space  
  - Outputs to an HTML report (use `jinja2`)  
- **Part 3 (Batch/CMD)**:  
  - Launch center: a simple CMD menu to run the Python or PowerShell scripts  
- **Optional bonus**: Add a backup function or system cleanup  

---

### **2. Port Scanner + Mini Admin Toolkit (2-3 people)**  

- **Difficulty**: Advanced  
- **Modules**: `socket`, `threading`, `argparse`  
- **Toolkit Functions**:  
  - Scan common ports of a given IP  
  - Display local IP, external IP (use `requests` to `https://api.ipify.org`)  
  - Save scan results to `results.csv`  
- **Challenge**: Add progress bars using `tqdm`  

---

### **3. Log File Analyzer (2 people)**  

- **Difficulty**: Medium  
- **Language**: Python  
- **Goal**: Parse an Apache log or custom server log and output:  
  - Most common IP  
  - Number of 404 errors  
  - Requests per hour graph (optional using `matplotlib`)  
- **Modules**: `re`, `collections`, `matplotlib`  

---

## **Exam Question Style Suggestions**

- **Write a Bash script that takes a folder path and counts how many `.txt` files are in it.**  
- **In PowerShell, display the top 5 processes by memory usage.**  
- **In Python, given a CSV file, read it and show how many rows contain the word "error".**  
- **Write a CMD batch script that asks for two numbers and adds them.**  
- **Write a script (any language) to ping a given IP 5 times and report if it's up or down.**  
- **Write a script to create scripts for you with pre-made modules - any lang.**
- **Interact with a DB (any lang) (any DB) with either a TUI or GUI**
- **Automatically scan downloaded files with the VirusTotal API**
