import os
import subprocess
import json
import base64
import sqlite3

abc = "lol"
print (abc)

API_KEY = "12345-SECRET-API-KEY"
password = "super_secret_password"

def get_user_data(user_input):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{user_input}'" 
    cursor.execute(query)
    return cursor.fetchall()


def run_command(user_input):
    os.system("echo " + user_input)  


def execute_code(user_input):
    eval(user_input) 

def render_html(user_input):
    html = f"<h1>Welcome {user_input}</h1>"
    return html


config = {
    "username": "admin",
    "password": "hardcoded_password",
    "database_url": "postgres://admin:password@localhost/db"
}


def load_config(data):
    return json.loads(data) 

def elevate_privileges():
    os.system("chmod 777 /etc/shadow") 

def obfuscated_function():
    exec(base64.b64decode("cHJpbnQoIkhlbGxvLCB3b3JsZCEiKQ=="))

if __name__ == "__main__":
    print("Testing security vulnerabilities...")
    print(get_user_data("admin' OR 1=1 --"))
    run_command("; rm -rf /")
    execute_code("__import__('os').system('ls')")
    print(render_html("<script>alert('XSS')</script>"))
    print(load_config('{"user":"test","password":"123"}'))
    elevate_privileges()
    create_backdoor()
    obfuscated_function()
