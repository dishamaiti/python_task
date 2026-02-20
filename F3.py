import logging

logging.basicConfig(
    filename="largest.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
def second_largest(lst: list[int]) -> int:
    """
    This finds the second largest element in a list.
    """
    logging.info("Finding second largest element")

    largest = float('-inf')
    second = float('-inf')

    for num in lst:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num

    logging.info(f"Second largest element found: {second}")
    return second


numbers = [10, 25, 8, 40, 30]
print("Second largest:", second_largest(numbers))