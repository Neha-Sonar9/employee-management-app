# from flask import Flask, jsonify

# app = Flask(__name__)

# @app.route("/api/employees", methods=["GET"])
# def get_employees():
#     employees = [
#         {"id": 1, "name": "Alice", "role": "DevOps Engineer"},
#         {"id": 2, "name": "Bob", "role": "Backend Developer"}
#     ]
#     return jsonify(employees)

# if __name__ == "__main__":
#     app.run(host="127.0.0.1", port=5000)



import os

import psycopg
from psycopg.rows import dict_row
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/api/employees", methods=["GET"])
def get_employees():
    with psycopg.connect(
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        row_factory=dict_row,
        connect_timeout=5,
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT id, name, role FROM employees ORDER BY id"
            )
            employees = cur.fetchall()

    return jsonify(employees)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
