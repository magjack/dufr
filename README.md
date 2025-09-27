# 🎨 GitHub Graph Word Writer

Welcome to the **Designated Ugly Fat Repo** - Write any text on your GitHub contribution graph! Spell out "WASSSUP!" in beautiful green squares! 🚀

## 🎯 What does this do?

This script creates ASCII art on your GitHub contribution graph by making commits on precisely calculated dates:

- ✅ Spells out any text like "WASSSUP!" in beautiful green squares
- ✅ Precisely calculates dates to form perfect letters
- ✅ Supports any custom text and year
- ✅ Preview mode to see your art before creating commits
- ✅ Uses only Python standard library (no external dependencies!)

## 🚀 Quick Start

### 1. Clone and Setup
```bash
git clone <your-repo-url>
cd dufr
```

### 2. Create your word art

**Preview how "WASSSUP!" will look:**
```bash
python graph_art.py --preview
```

**Create the actual commits for "WASSSUP!":**
```bash
python graph_art.py
```

**Custom text:**
```bash
python graph_art.py --text "HELLO"
python graph_art.py --text "2025"
python graph_art.py --text "CODE"
```

**Different year or position:**
```bash
python graph_art.py --text "WASSSUP!" --year 2025
python graph_art.py --text "HELLO" --start-week 15
```

### 3. Push to GitHub
```bash
git push origin main
```

## 📋 Command Line Options

| Option | Description | Default |
|--------|-------------|---------|
| `--text` | Text to display on graph | "WASSSUP!" |
| `--year` | Target year for the graph | 2025 |
| `--start-week` | Week to start the text (0-52) | 8 |
| `--preview` | Preview the layout without creating commits | - |
| `--preview-dates` | Show all commit dates | - |

## 🎨 Supported Characters

The script supports these characters for your graph art:
- **W A S U P !** - Perfect for "WASSSUP!"
- All uppercase letters: **A B C D E F G H I J K L M N O P Q R S T U V W X Y Z**
- Numbers: **0 1 2 3 4 5 6 7 8 9**
- Special: **!**
- Spaces between words are automatically handled

Want to add more characters? Edit the `letters` dictionary in `graph_art.py`!

## 🎨 ASCII Art Preview

Here's how "WASSSUP!" looks on your GitHub contribution graph:

```
Sun │········█···█··███···████··████··████·█···█·████··█··
Mon │········█···█·█···█·█·····█·····█·····█···█·█···█·█··
Tue │········█···█·█···█·█·····█·····█·····█···█·█···█·█··
Wed │········█···█·█████··███···███···███··█···█·████··█··
Thu │········█·█·█·█···█·····█·····█·····█·█···█·█·····█··
Fri │········██·██·█···█·····█·····█·····█·█···█·█········
Sat │········█···█·█···█·████··████··████···███··█·····█··
    └─────────────────────────────────────────────────────
     Jan                                            Dec 2025
```

Each `█` represents a day with commits, forming perfect letters!

## 📊 What gets created?

- Precisely calculated commits on specific dates
- Creates unique JSON data files for each commit date
- Realistic commit messages with timestamps
- Perfect letter formation on your GitHub graph

## ⚠️ Ethical Usage

This tool is for:
- ✅ Fun ASCII art on your personal GitHub profile
- ✅ Learning Git/Python automation
- ✅ Impressing friends with creative contributions
- ✅ Personal motivation and habit building

Please don't use this to:
- ❌ Deceive employers about your actual coding activity
- ❌ Inflate your GitHub profile dishonestly for job applications

## 🛠️ Requirements

- Python 3.6+
- Git installed and configured
- GitHub repository (public or private)

## 🎨 Customization

Want to add more letters or symbols? Edit the `letters` dictionary in `graph_art.py`! Each letter is defined as a 7×5 grid where `1` means "make a commit" and `0` means "no commit".

## 📝 License

This project is in the public domain. Use it however you want! 

---

**Happy Contributing!** 🎉

*Remember: The best way to have a green contribution graph is to actually code regularly. This is just for fun! 🎉*
