import re   # Import regular expressions for pattern matching   
from simpleeval import simple_eval  # Import simple_eval for evaluating mathematical expressions
from typing import Final  # For type hints
templates = [
    r".*\b{synonym}\b.*",  # Match synonym anywhere in the sentence
]

synonym_lists = {
    "math": ["mathematics", "arithmetic", "algebra", "math", "solve math", "maths", "maths problems", "maths help", "maths assistance"],
    "perfect_number": ["find perfect number", "perfect number", "perfect numbers", "perfect number help"],
    "prime_number": ["find prime number", "prime number", "prime numbers", "prime number help"],
    "fibonacci": ["fibonacci", "fibonacci sequence", "fibonacci numbers", "fibonacci help", "fibonacci assistance"],
    "factorial": ["factorial", "factorial of", "factorial help", "factorial assistance"],
    "palindrome": ["palindrome", "palindrome number", "palindrome help", "palindrome assistance"],
    "armstrong": ["armstrong", "armstrong number", "armstrong help", "armstrong assistance"],
    "perfect_square": ["perfect square", "perfect squares", "perfect square help", "perfect square assistance"],
    "perfect_cube": ["perfect cube", "perfect cubes", "perfect cube help", "perfect cube assistance"],
    "even_odd": ["even odd", "even or odd", "even or odd number", "even odd number", "even odd help", "even odd assistance"],
    "square_root": ["square root", "square root of", "square root help", "square root assistance"],
    "cube_root": ["cube root", "cube root of", "cube root help", "cube root assistance"]
}

pattern_response_pairs = {}
for category, synonyms in synonym_lists.items():
    # Create a regex pattern for each synonym in the category  
    for synonym in synonyms:
        for template in templates:
            pattern = re.compile(template.format(synonym=re.escape(synonym)), re.IGNORECASE)
            pattern_response_pairs[pattern] = category

def generate_response(category, user_input=None, context=None):
    if category == "math":
        if context:
            context.user_data["awaiting_math"] = True
        return "Sure! Send me a math expression like '4 + 3 * 2' and I’ll solve it."

    elif category == "fibonacci":
        # Example logic
        return "Fibonacci logic not implemented yet."

    elif category == "prime_number":
        return "Prime number logic not implemented yet."

    # Add more elif blocks for other categories...

    else:
        return "Invalid category. Please try again."

def evaluate_math_expression(expression: str) -> str:
    try:
        math_pattern = r'^[\d\s\+\-\*/\(\)\.]+$'
        if not re.match(math_pattern, expression.strip()):
            return "That doesn't look like a valid math expression."
        result = simple_eval(expression)
        return f"The result is: {result}"
    except:
        return "Hmm... I couldn't solve that expression. Try something simpler like '4 + 3 * 2'."

def handle_response(text: str, context=None) -> str:
    cleaned_text = text.lower().strip()
    # Check if the cleaned text matches any math expression pattern
    for pattern, category in pattern_response_pairs.items():
        if pattern.search(cleaned_text):
            return generate_response(category, cleaned_text, context)
    
    print("User input:", cleaned_text)
    for pattern in pattern_response_pairs:
        print("Trying pattern:", pattern.pattern)
    return "I'm still learning.!"