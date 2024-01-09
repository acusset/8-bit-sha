import sys

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
        '000': (0, 0, 0),        # Black
        '001': (255, 255, 255),  # White
        '010': (255, 0, 0),      # Red
        '011': (0, 255, 0),      # Green
        '100': (0, 0, 255),      # Blue
        '101': (255, 255, 0),    # Yellow
        '110': (255, 0, 255),    # Magenta
        '111': (0, 255, 255),    # Cyan
        # Add more color mappings based on your preference and patterns
    }

    # Fill pixels based on the binary sequence
    groups = len(binary) // 3
    for i in range(groups):
        pixel_color = color_map[binary[i * 3: i * 3 + 3]]
        pixels[i % size, i // size] = pixel_color

    # Fill remaining pixels with white color
    for i in range(groups, size * size):
        pixels[i % size, i // size] = (255, 255, 255)  # White color

    image.save(sha + '.png')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python generate_artwork.py <commit_sha>")
        sys.exit(1)

    commit_sha = sys.argv[1]

    generate_8bit_art(commit_sha)
