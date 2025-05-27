# =====================================
# STRING AND ARRAY PROGRAMS IN PYTHON
# =====================================

# This script contains various Python programs demonstrating string manipulation,   

# Program 1: String Manipulation
def string_operations():
    print("=== STRING OPERATIONS ===")
    text = "Hello World Python Programming"
    
    print(f"Original: {text}")
    print(f"Length: {len(text)}")
    print(f"Uppercase: {text.upper()}")
    print(f"Lowercase: {text.lower()}")
    print(f"Title Case: {text.title()}")
    print(f"Replace 'Python' with 'Java': {text.replace('Python', 'Java')}")
    print(f"Split into words: {text.split()}")
    print(f"Count 'o': {text.count('o')}")
    print(f"Find 'Python': {text.find('Python')}")
    print(f"Starts with 'Hello': {text.startswith('Hello')}")
    print(f"Ends with 'ing': {text.endswith('ing')}")
    print()

# Program 2: Array/List Operations
def array_operations():
    print("=== ARRAY/LIST OPERATIONS ===")
    numbers = [10, 25, 3, 78, 45, 12, 90, 5]
    
    print(f"Original array: {numbers}")
    print(f"Length: {len(numbers)}")
    print(f"Sum: {sum(numbers)}")
    print(f"Maximum: {max(numbers)}")
    print(f"Minimum: {min(numbers)}")
    print(f"Average: {sum(numbers)/len(numbers):.2f}")
    print(f"Sorted: {sorted(numbers)}")
    print(f"Reversed: {numbers[::-1]}")
    
    # Add and remove elements
    numbers.append(100)
    print(f"After append(100): {numbers}")
    numbers.insert(2, 999)
    print(f"After insert(2, 999): {numbers}")
    numbers.remove(25)
    print(f"After remove(25): {numbers}")
    print()

# Program 3: String Array Processing
def string_array_processing():
    print("=== STRING ARRAY PROCESSING ===")
    names = ["Alice", "Bob", "Charlie", "Diana", "Edward"]
    
    print(f"Names: {names}")
    
    # Filter names with length > 4
    long_names = [name for name in names if len(name) > 4]
    print(f"Names with length > 4: {long_names}")
    
    # Convert to uppercase
    upper_names = [name.upper() for name in names]
    print(f"Uppercase names: {upper_names}")
    
    # Names starting with specific letter
    names_with_e = [name for name in names if name.startswith('E')]
    print(f"Names starting with 'E': {names_with_e}")
    
    # Join names
    joined = ", ".join(names)
    print(f"Joined names: {joined}")
    print()

# Program 4: Character Frequency Counter
def char_frequency():
    print("=== CHARACTER FREQUENCY COUNTER ===")
    text = input("Enter a string: ")
    
    # Method 1: Using dictionary
    freq = {}
    for char in text.lower():
        if char.isalpha():  # Only count letters
            freq[char] = freq.get(char, 0) + 1
    
    print("Character frequencies:")
    for char in sorted(freq.keys()):
        print(f"'{char}': {freq[char]}")
    print()

# Program 5: Word Operations
def word_operations():
    print("=== WORD OPERATIONS ===")
    sentence = "Python is a powerful programming language for data science"
    words = sentence.split()
    
    print(f"Sentence: {sentence}")
    print(f"Word count: {len(words)}")
    print(f"Words: {words}")
    
    # Longest word
    longest = max(words, key=len)
    print(f"Longest word: '{longest}' (length: {len(longest)})")
    
    # Words longer than 5 characters
    long_words = [word for word in words if len(word) > 5]
    print(f"Words longer than 5 chars: {long_words}")
    
    # Reverse each word
    reversed_words = [word[::-1] for word in words]
    print(f"Reversed words: {reversed_words}")
    print()

# Program 6: Array Searching and Sorting
def search_sort_array():
    print("=== ARRAY SEARCHING AND SORTING ===")
    numbers = [64, 34, 25, 12, 22, 11, 90, 88, 76, 50]
    
    print(f"Original: {numbers}")
    
    # Linear Search
    target = 22
    index = -1
    for i in range(len(numbers)):
        if numbers[i] == target:
            index = i
            break
    
    if index != -1:
        print(f"Linear search: {target} found at index {index}")
    else:
        print(f"Linear search: {target} not found")
    
    # Bubble Sort implementation
    arr = numbers.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    print(f"Bubble sorted: {arr}")
    
    # Binary search (on sorted array)
    def binary_search(arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    result = binary_search(arr, target)
    print(f"Binary search: {target} found at index {result} in sorted array")
    print()

# Program 7: String Pattern Matching
def pattern_matching():
    print("=== STRING PATTERN MATCHING ===")
    text = "The quick brown fox jumps over the lazy dog"
    
    # Find all words starting with specific letter
    words = text.split()
    t_words = [word for word in words if word.lower().startswith('t')]
    print(f"Words starting with 't': {t_words}")
    
    # Check if string contains only alphabets
    test_strings = ["Hello", "Hello123", "Hello World", "ABC"]
    for s in test_strings:
        is_alpha = s.replace(" ", "").isalpha()
        print(f"'{s}' contains only alphabets: {is_alpha}")
    
    # Palindrome check
    def is_palindrome(s):
        s = s.lower().replace(" ", "")
        return s == s[::-1]
    
    test_palindromes = ["radar", "hello", "A man a plan a canal Panama", "race car"]
    for s in test_palindromes:
        print(f"'{s}' is palindrome: {is_palindrome(s)}")
    print()

# Program 8: 2D Array Operations
def two_d_array():
    print("=== 2D ARRAY OPERATIONS ===")
    
    # Create 3x3 matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    
    print("Original matrix:")
    for row in matrix:
        print(row)
    
    # Matrix operations
    print(f"\nMatrix dimensions: {len(matrix)}x{len(matrix[0])}")
    
    # Sum of all elements
    total = sum(sum(row) for row in matrix)
    print(f"Sum of all elements: {total}")
    
    # Transpose
    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    print("\nTranspose:")
    for row in transpose:
        print(row)
    
    # Diagonal sum
    diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))
    print(f"\nDiagonal sum: {diagonal_sum}")

# Main execution
if __name__ == "__main__":
    string_operations()
    array_operations()
    string_array_processing()
    char_frequency()
    word_operations()
    search_sort_array()
    pattern_matching()
    two_d_array()