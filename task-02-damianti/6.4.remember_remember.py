# download Pillow in order to use PIL
from PIL import Image


def decrypt_message(image_path):
    """
    takes a file path image_path as input and returns a decrypted message as a string

    :param image_path: (string) The file path to the image to be processed.
    :return: message: (string) The decrypted message extracted from the image.
    """
    # Open the image using the Image module
    image = Image.open(image_path)

    # Get the dimensions of the image
    width, height = image.size

    # Use list comprehension to find the row number of the black pixel in each column
    row_numbers = [
        next(y for y in range(height) if image.getpixel((x, y)) == 1)
        for x in range(width)
    ]

    # Convert the row numbers to characters using the ord() function
    message = ''.join(chr(row_number) for row_number in row_numbers)

    return message


# Example usage
if __name__ == "__main__":
    msg = decrypt_message("resources/code.png")
    print(msg)
