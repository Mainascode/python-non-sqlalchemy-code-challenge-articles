#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


    # don't remove this line, it's for debugging!
    ipdb.set_trace()
# Import the Author class from its module
from author import Author

# Define variables and create sample instances for debugging
try:
    # Valid Author instance
    author1 = Author("Jane Austen")
    print(f"Author 1: {author1.name}")  # Outputs: Author 1: Jane Austen

    # Invalid Author instance: Empty name
    try:
        author2 = Author("")
    except ValueError as e:
        print(f"Error creating author: {e}")  # Outputs: Name must be longer than 0 characters

    # Invalid Author instance: Name not a string
    try:
        author3 = Author(123)
    except TypeError as e:
        print(f"Error creating author: {e}")  # Outputs: Name must be of type str

    # Attempting to change an author's name
    try:
        author1.name = "Charlotte Brontë"
    except AttributeError as e:
        print(f"Error modifying author's name: {e}")  # Outputs: Cannot change the author's name after instantiation

except Exception as e:
    print(f"Unexpected error: {e}")
