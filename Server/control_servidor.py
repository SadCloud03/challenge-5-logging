from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime, timezone

app = Flask(__name__)

DB_Name = "data_base_logs.db"

