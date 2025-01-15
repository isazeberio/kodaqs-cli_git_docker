#!/usr/bin/env python3

import sys
import string
from collections import Counter
import matplotlib.pyplot as plt


def count_characters(file_path):
    """
    Count the occurrences of characters A-Z in a file.
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Convert to uppercase and filter A-Z characters
    text = text.upper()
    char_counts = Counter(char for char in text if char in string.ascii_uppercase)
    return char_counts


def plot_histogram(char_counts):
    """
    Plot a histogram of character counts.
    """
    characters = list(string.ascii_uppercase)
    counts = [char_counts[char] for char in characters]

    plt.figure(figsize=(10, 6))
    plt.bar(characters, counts, color='skyblue', edgecolor='black')
    plt.title('Character Count Histogram (A-Z)', fontsize=16)
    plt.xlabel('Character', fontsize=14)
    plt.ylabel('Count', fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()

    # Save the histogram as an image file
    plt.savefig('character_count_histogram.png')
    print("Histogram saved as 'character_count_histogram.png'")


def main():
    """
    Main function to process input and generate character count histogram.
    """
    if len(sys.argv) != 2:
        print("Usage: python character-count.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    char_counts = count_characters(file_path)

    if char_counts:
        print("Character counts:")
        for char, count in sorted(char_counts.items()):
            print(f"{char}: {count}")

        plot_histogram(char_counts)
    else:
        print("No valid A-Z characters found in the file.")


if __name__ == "__main__":
    main()
