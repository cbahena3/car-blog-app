import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS cars;
        """
    )
    conn.execute(
        """
        CREATE TABLE cars (
          id INTEGER PRIMARY KEY NOT NULL,
          title TINYTEXT,
          description TEXT,
          image BLOB,
          make TINYTEXT,
          model TINYTEXT,
          color TINYTEXT,
          year INTEGER
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    cars_seed_data = [
        ("my first car", "This was my first car when i was 18",
         "https://carwow-uk-wp-3.imgix.net/18015-MC20BluInfinito-scaled-e1666008987698.jpg", "maserati", "MC20", "blue", 2024),
        ("my second car", "This was my first car when i was 19",
         "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbhxXrzJueBW6uavud_uDO6gkZuRcg-QiKwABoP036NEHD1uyss9LfqKtpw2R_XgCBl8g&usqp=CAU", "bmw", "M3", "green", 2024),
        ("my third car", "This was my first car when i was 20",
         "https://hips.hearstapps.com/hmg-prod/images/audirs7sportback-performance-nardogrey012-6496455664abb.jpg?crop=0.506xw:0.380xh;0.402xw,0.387xh&resize=1200:*", "audi", "rs7", "gray", 2024),
    ]
    conn.executemany(
        """
        INSERT INTO cars (title, description, image, make, model, color, year)
        VALUES (?,?,?)
        """,
        cars_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()


def cars_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM cars
        """
    ).fetchall()
    return [dict(row) for row in rows]


def cars_find_by_id(id):
    conn = connect_to_db()
    row = conn.execute(
        """
        SELECT * FROM cars
        WHERE id = ?
        """,
        id,
    ).fetchone()
    return dict(row)


if __name__ == "__main__":
    initial_setup()


def cars_create(title, description, image, make, model, color, year):
    conn = connect_to_db()
    row = conn.execute(
        """
        INSERT INTO cars (title, description, image, make, model, color, year)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        RETURNING *
        """,
        (title, description, image, make, model, color, year),
    ).fetchone()
    conn.commit()
    return dict(row)
