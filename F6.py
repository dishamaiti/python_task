import logging

logging.basicConfig(
    filename="duplicate.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def remove_duplicates(lst: list[int]) -> list[int]:
    """
    Remove duplicate elements from a list while preserving order.
    """
    logging.info("Removing duplicates from list")

    result = []

    for num in lst:
        if num not in result:
            result.append(num)

    logging.info(f"List after removing duplicates: {result}")
    return result


numbers = [1, 2, 2, 3, 4, 3, 5]
print("After removing duplicates:", remove_duplicates(numbers))