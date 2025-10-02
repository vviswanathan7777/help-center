# simple_utils.py - A tiny utility library

def reverse_string(text):
    """
    Return a new string with the characters of `text` in reverse order.
    
    Parameters:
        text (str): Input string to reverse.
    
    Returns:
        reversed_text (str): The reversed string.
    """
    return text[::-1]

def count_words(sentence):
    """
    Count the number of words in a sentence.
    
    Parameters:
        sentence (str): Input text; words are separated by any whitespace characters.
    
    Returns:
        int: Number of words in the sentence.
    """
    return len(sentence.split())

def celsius_to_fahrenheit(celsius):
    """
    Convert a temperature from degrees Celsius to degrees Fahrenheit.
    
    Parameters:
        celsius (float): Temperature in degrees Celsius.
    
    Returns:
        fahrenheit (float): Temperature converted to degrees Fahrenheit.
    """
    return (celsius * 9/5) + 32
