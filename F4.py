import logging

logging.basicConfig(
    filename="sorting.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def is_sorted(lst: list[int]) -> bool:
    """
    Check whether a list is sorted in ascending order.
    """
    logging.info("Checking if list is sorted in ascending order")

    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            logging.info("List is not sorted")
            return False

    logging.info("List is sorted")
    return True


numbers = [1, 2, 3, 4, 5]
print("Is sorted:", is_sorted(numbers))