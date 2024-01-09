from PIL import Image


def sha_to_binary(sha):
    # Convert hexadecimal string to binary string
    binary = bin(int(sha, 16))[2:].zfill(len(sha) * 4)
    return binary


def generate_8bit_art(sha):
    # Get binary representation from the SHA
    binary = sha_to_binary(sha)

    # Create an 8x8 pixel grid
    size = 8
    image = Image.new("RGB", (size, size))
    pixels = image.load()

    # Define a color map based on binary patterns
    color_map = {
        '000': (0, 0, 0),  # Black
        '001': (255, 255, 255),  # White
        '010': (255, 0, 0),  # Red
        '011': (0, 255, 0),  # Green
        '100': (0, 0, 255),  # Blue
        '101': (255, 255, 0),  # Yellow
        '110': (255, 0, 255),  # Magenta
        '111': (0, 255, 255),  # Cyan
        # Add more color mappings based on your preference and patterns
    }

    # Fill pixels based on the binary sequence
    for i in range(size):
        for j in range(size):
            index = i * size + j
            pixel_color = color_map[binary[index * 3: index * 3 + 3]]  # Using every 3 bits for color
            pixels[j, i] = pixel_color

    return image
