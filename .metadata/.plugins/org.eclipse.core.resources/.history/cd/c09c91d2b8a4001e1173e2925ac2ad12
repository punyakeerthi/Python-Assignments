'''
Created on Dec 22, 2023

@author: PBL
'''
import os
import PyPDF2
import sys
import json
import re
import configparser
import mysql.connector

# ... (existing code)

def load_questions_from_chapter(connection, chapter_name):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            SELECT question_text
            FROM questions
            WHERE chapter_name = %s
        """, (chapter_name,))

        questions = cursor.fetchall()

        if not questions:
            print(f"No questions found for chapter '{chapter_name}'.")
        else:
            print(f"Questions for chapter '{chapter_name}':")
            for question in questions:
                print(question[0])

    except mysql.connector.Error as err:
        print(f"Error loading questions from the database: {err}")

    finally:
        if 'cursor' in locals():
            cursor.close()

# ... (existing code)
def connect_to_database():
    try:
        # Update with your MySQL database credentials
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Punya@1991",
            database="demo"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        sys.exit(1)

if __name__ == "__main__":
    pdf_path = 'D:/Data/SBM_01.pdf'
    config_path = 'D:/Data/application.properties'

    try: 
        chapter_name = input("Enter the chapter name to load questions: ").strip()

        if not chapter_name:
            print("Chapter name cannot be empty.")
            sys.exit(1)

    except ValueError:
        print("Invalid input. Please enter a valid page number.")
        sys.exit(1)

    connection = connect_to_database() 
    load_questions_from_chapter(connection, chapter_name)

    if connection.is_connected():
        connection.close()
