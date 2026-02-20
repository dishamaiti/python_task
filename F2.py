import logging

logging.basicConfig(
    filename="frequency.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def char_frequency(s: str) -> dict:
    """
    Calculate frequency of each character in a string.
    """
    logging.info("Calculating character frequency")

    freq = {}

    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    logging.info(f"Character frequency calculated: {freq}")
    return freq


s = "programming"
print("Character frequency:", char_frequency(s))