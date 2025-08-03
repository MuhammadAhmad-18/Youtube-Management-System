# 📺 YouTube Manager App

A simple terminal-based CRUD (Create, Read, Update, Delete) application to manage YouTube videos using **Python** and **SQLite**.

---

## 🚀 Features

- 📄 List all saved videos
- ➕ Add a new video entry
- ✏️ Update existing video details (title, duration, link, or author)
- ❌ Delete a video by title
- 💾 Data is saved locally using SQLite database (`youtube.db`)

---

## 🛠️ Tech Stack

- **Python 3**
- **SQLite3 (Built-in Python module)**

---

## 📂 Table Schema

**Table Name:** `vedios_list`

| Column Name     | Type         | Constraints          |
|------------------|--------------|----------------------|
| `id`             | INTEGER      | PRIMARY KEY AUTOINCREMENT |
| `vedio_title`    | VARCHAR(50)  | NOT NULL             |
| `vedio_duration` | VARCHAR(20)  | NOT NULL             |
| `vedio_link`     | VARCHAR(100) | NOT NULL             |
| `vedio_author`   | VARCHAR(20)  | NOT NULL             |

---

## 🧑‍💻 How to Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run the script:

```bash
python your_script_name.py
