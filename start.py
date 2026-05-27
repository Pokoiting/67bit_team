import string
from collections import Counter

def analyze_text(text: str) -> None:
    translator = str.maketrans('', '', string.punctuation)
    cleaned = text.translate(translator)

    words = cleaned.lower().split()

    total_words = len(words)
    most_common = Counter(words).most_common(5)

    print(f"Общее количество слов: {total_words}")
    print("\n5 самых частых слов:")
    for word, count in most_common:
        print(f"  {word}: {count}")


sample_text = """
SEO is the practice of improving a website to increase its visibility.
SEO helps people find your site through search engines.
Good SEO content is relevant, useful, and well-structured.
A semantic core is the foundation of SEO strategy.
"""

analyze_text(sample_text)