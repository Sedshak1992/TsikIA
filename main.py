# TsikIA - Fichiers à copier sur GitHub Mobile

## 1. Créer le fichier 
import os
import json
import uuid
from datetime import datetime
from flask import Flask, render_template, request, jsonify, session
from openai import OpenAI

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "your-secret-key-here")

# Configuration OpenRouter
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is required")

client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url="https://openrouter.ai/api/v1"
)

# Constants
USER_STORE_FILE = "user_store.json"
DEFAULT_PLANS = {
    "free": {"name": "Gratuit", "daily_quota": 5, "price": 0},
    "basic": {"name": "Basique", "daily_quota": 50, "price": 10},
    "premium": {"name": "Premium", "daily_quota": 200, "price": 25}
}

def load_user_store():
    """Load user store from JSON file or create default structure"""
    try:
        with open(USER_STORE_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        default_store = {
            "users": {},
            "plans": DEFAULT_PLANS
        }
        save_user_store(default_store)
        return default_store

def save_user_store(store):
    """Save user store to JSON file"""
  
