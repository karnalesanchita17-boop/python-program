import re
def extract_digits():
    text = input("Enter a string: ")
    print("Digits:", re.findall(r"\d", text))

def words_starting_a():
    sentence = input("Enter a sentence: ")
    print("Words beginning with A/a:", re.findall(r"\b[aA]\w*\b", sentence))

def count_vowels():
    text = input("Enter a string: ")
    vowels = re.findall(r"[aeiou]", text, re.IGNORECASE)
    print("Vowel occurrences:", len(vowels))
    print("Vowels:", vowels)

def extract_uppercase():
    text = input("Enter a string: ")
    print("Uppercase letters:", re.findall(r"[A-Z]", text))

def find_whitespace_characters():
    text = input("Enter text (you can type \\t or \\n literally): ")
    # This identifies actual whitespace characters present in the entered text.
    print("Whitespace characters:", re.findall(r"[ \t\n]", text))

def collapse_spaces():
    text = input("Enter text: ")
    print("Result:", re.sub(r" {2,}", " ", text))

def five_character_words():
    sentence = input("Enter a sentence: ")
    print("Five-character words:", re.findall(r"\b[A-Za-z]{5}\b", sentence))

def words_ending_s():
    sentence = input("Enter a sentence: ")
    print("Words ending in s:", re.findall(r"\b\w+s\b", sentence, re.IGNORECASE))

def remove_special_characters():
    text = input("Enter a string: ")
    print("Result:", re.sub(r"[^A-Za-z0-9 ]", "", text))

def count_words():
    sentence = input("Enter a sentence: ")
    print("Word count:", len(re.findall(r"\b\w+\b", sentence)))

def validate_mobile():
    number = input("Enter a 10-digit Indian mobile number: ")
    pattern = r"[6-9]\d{9}"
    print("Valid mobile number" if re.fullmatch(pattern, number) else "Invalid mobile number")

def validate_email():
    email = input("Enter an email address: ")
    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
    print("Email format looks valid" if re.fullmatch(pattern, email) else "Invalid email format")

def extract_dates():
    text = input("Enter a paragraph: ")
    print("Dates (DD-MM-YYYY):", re.findall(r"\b(?:0[1-9]|[12]\d|3[01])-(?:0[1-9]|1[0-2])-\d{4}\b", text))

def extract_urls():
    text = input("Enter text: ")
    print("Web addresses:", re.findall(r"https?://[^\s]+", text))

def extract_hashtags():
    text = input("Enter a social media post: ")
    print("Hashtags:", re.findall(r"(?<!\w)#[A-Za-z0-9_]+", text))

def validate_password():
    password = input("Enter a password: ")
    pattern = r"(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]).{8,}"
    print("Strong password format" if re.fullmatch(pattern, password) else "Password does not meet requirements")

def repeated_words():
    sentence = input("Enter a sentence: ")
    pattern = r"\b([A-Za-z]+)\s+\1\b"
    matches = re.findall(pattern, sentence, re.IGNORECASE)
    print("Consecutive repeated words:", matches)

def extract_pin_codes():
    text = input("Enter a paragraph: ")
    print("Six-digit PIN codes:", re.findall(r"\b[1-9]\d{5}\b", text))

def validate_vehicle_number():
    number = input("Enter a vehicle registration number (e.g. MH12AB1234): ").upper()
    pattern = r"[A-Z]{2}\d{2}[A-Z]{1,2}\d{4}"
    print("Registration format looks valid" if re.fullmatch(pattern, number) else "Invalid registration format")

def extract_extensions():
    text = input("Enter text containing filenames: ")
    print("File extensions:", re.findall(r"\b[\w-]+\.(\w+)\b", text))

def clean_html_text():
    text = input("Enter text containing HTML tags: ")
    text = re.sub(r"<[^>]+>", " ", text)          # Remove HTML tags
    text = re.sub(r"\s+", " ", text)              # Collapse whitespace
    text = re.sub(r"[^\w\s.,!?'-]", "", text)     # Remove unwanted punctuation
    print("Clean text:", text.strip())

def extract_invoice_fields():
    text = input("Enter invoice text: ")
    invoice_no = re.findall(r"(?i)\b(?:invoice\s*(?:no|number|#)?\s*[:#-]?\s*)([A-Z0-9/-]+)", text)
    dates = re.findall(r"\b(?:0[1-9]|[12]\d|3[01])[-/](?:0[1-9]|1[0-2])[-/]\d{4}\b", text)
    amounts = re.findall(r"(?:₹|Rs\.?\s*)\s?\d[\d,]*(?:\.\d{2})?", text, re.IGNORECASE)
    print("Invoice numbers:", invoice_no)
    print("Dates:", dates)
    print("Monetary amounts:", amounts)

def find_python_comments():
    print("Enter Python source code; type END on a line by itself to finish:")
    lines = []
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)
    source = "\n".join(lines)
    comments = re.findall(r"#.*", source)
    print("Possible single-line comments:")
    for comment in comments:
        print(comment)
    print("Note: Regex may mistake # inside strings (for example, '# not a comment') for a comment.")
    print("It also cannot reliably parse every multiline/string continuation case; Python's tokenizer is safer.")

def validate_product_code():
    code = input("Enter product code (ABC-1234-XY): ")
    pattern = r"[A-Z]{3}-\d{4}-[A-Z]{2}"
    print("Valid product code" if re.fullmatch(pattern, code) else "Invalid product code")

def extract_student_fields():
    text = input("Enter student details (e.g. Name: Amit, Roll: 12, Marks: 85): ")
    names = re.findall(r"(?i)\bName\s*:\s*([A-Za-z ]+?)(?=,\s*(?:Roll|Roll No|Marks)\s*:|$)", text)
    rolls = re.findall(r"(?i)\bRoll(?:\s*No)?\s*:\s*(\d+)", text)
    marks = re.findall(r"(?i)\bMarks\s*:\s*(\d+(?:\.\d+)?)", text)
    print("Names:", [x.strip() for x in names])
    print("Roll numbers:", rolls)
    print("Marks:", marks)

def extract_research_references():
    text = input("Enter a research reference or references: ")
    dois = re.findall(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", text, re.IGNORECASE)
    years = re.findall(r"\b(?:19|20)\d{2}\b", text)
    emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", text)
    urls = re.findall(r"https?://[^\s)]+", text)
    print("DOI identifiers:", dois)
    print("Publication years:", years)
    print("Email addresses:", emails)
    print("URLs:", urls)

PROGRAMS = {
    "1": ("Extract all digits", extract_digits),
    "2": ("Words beginning with A/a", words_starting_a),
    "3": ("Count vowel occurrences", count_vowels),
    "4": ("Extract uppercase letters", extract_uppercase),
    "5": ("Identify spaces, tabs, and newlines", find_whitespace_characters),
    "6": ("Replace multiple spaces with one", collapse_spaces),
    "7": ("Find five-character words", five_character_words),
    "8": ("Words ending with s", words_ending_s),
    "9": ("Remove special characters", remove_special_characters),
    "10": ("Count words", count_words),
    "11": ("Validate Indian mobile number", validate_mobile),
    "12": ("Validate email format", validate_email),
    "13": ("Extract DD-MM-YYYY dates", extract_dates),
    "14": ("Extract HTTP/HTTPS URLs", extract_urls),
    "15": ("Extract hashtags", extract_hashtags),
    "16": ("Validate password rules", validate_password),
    "17": ("Find consecutive repeated words", repeated_words),
    "18": ("Extract six-digit Indian PIN codes", extract_pin_codes),
    "19": ("Validate vehicle registration format", validate_vehicle_number),
    "20": ("Extract file extensions", extract_extensions),
    "21": ("Remove HTML tags and clean text", clean_html_text),
    "22": ("Extract invoice fields", extract_invoice_fields),
    "23": ("Identify possible Python comments", find_python_comments),
    "24": ("Validate product code", validate_product_code),
    "25": ("Extract student fields", extract_student_fields),
    "26": ("Extract research reference fields", extract_research_references),
}

def main():
    while True:
        print("\\n===== REGULAR EXPRESSION PROGRAMS =====")
        for number, (description, _) in PROGRAMS.items():
            print(f"{number}. {description}")
        print("0. Exit")
        choice = input("Choose a program (0-26): ").strip()
        if choice == "0":
            print("Exiting program.")
            break
        selected = PROGRAMS.get(choice)
        if selected:
            print(f"\\n--- {selected[0]} ---")
            selected[1]()
        else:
            print("Invalid choice. Please enter a number from 0 to 26.")

if __name__ == "__main__":
    main()
