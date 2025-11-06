import sqlite3
from fastapi import HTTPException

# ----------------------------
# Database Connection Function
# ----------------------------
def db_conn():
    conn = sqlite3.connect("ADVICER.db", check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn


# ----------------------------
# Table Creation
# ----------------------------
conn = db_conn()
conn.execute("""
CREATE TABLE IF NOT EXISTS ADVICES (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    category TEXT NOT NULL
)
""")
conn.commit()
conn.close()


# ----------------------------
# CRUD FUNCTIONS
# ----------------------------

# Create advice
def create_advice(title: str, description: str, category: str):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO ADVICES (title, description, category) VALUES (?, ?, ?)",
        (title, description, category)
    )
    conn.commit()
    conn.close()
    return {"message": "Advice added successfully", "id": cur.lastrowid}


# Get all advices
def get_all_advices():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM ADVICES")
    rows = cur.fetchall()
    conn.close()
    return [dict(row) for row in rows]


# Get advice by ID
def get_advice_by_id(advice_id: int):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM ADVICES WHERE id = ?", (advice_id,))
    row = cur.fetchone()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Advice not found")
    return dict(row)


# Get advice by category
def get_advice_by_category(category: str):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute("SELECT * FROM ADVICES WHERE category = ?", (category,))
    rows = cur.fetchall()
    conn.close()

    if not rows:
        raise HTTPException(status_code=404, detail="No advices found for this category")
    return [dict(row) for row in rows]


# Update advice
def update_advice(advice_id: int, title: str, description: str, category: str):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute(
        "UPDATE ADVICES SET title = ?, description = ?, category = ? WHERE id = ?",
        (title, description, category, advice_id)
    )
    conn.commit()
    conn.close()

    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Advice not found")
    return {"message": "Advice updated successfully"}


# Delete advice
def delete_advice(advice_id: int):
    conn = db_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM ADVICES WHERE id = ?", (advice_id,))
    conn.commit()
    conn.close()

    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Advice not found")
    return {"message": "Advice deleted successfully"}

    
