import logging

logging.basicConfig(
    filename="missing.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def find_missing_number(lst: list[int]) -> int:
    """
    Find the missing number in a list containing numbers from 1 to N.
    """
    logging.info("Finding missing number in the list")

    n = len(lst) + 1
    total_sum = n * (n + 1) // 2

    list_sum = 0
    for num in lst:
        list_sum += num

    missing = total_sum - list_sum

    logging.info(f"Missing number found: {missing}")
    return missing


numbers = [1, 2, 4, 5]
print("Missing number:", find_missing_number(numbers))