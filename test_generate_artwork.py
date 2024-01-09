import unittest
from generate_artwork import sha_to_binary, generate_8bit_art


class TestArtGeneration(unittest.TestCase):

    def test_sha_to_binary(self):
        # Test cases for sha_to_binary function
        test_sha = "d0740f807cea36ac165694e3e03942d0e01b7d10"
        expected_binary = "11010000011101000011111110000011111001101101001100110101001110110000110101011010011100011110001111001101000001110111010000"

        result_binary = sha_to_binary(test_sha)
        self.assertEqual(result_binary, expected_binary, "Binary conversion is incorrect")

    def test_generate_8bit_art(self):
        # Test cases for generate_8bit_art function
        test_sha = "d0740f807cea36ac165694e3e03942d0e01b7d10"
        # Additional assertions can be made for the generated image characteristics

        generated_image = generate_8bit_art(test_sha)
        # Example: Assert the image mode and size
        self.assertEqual(generated_image.mode, 'RGB', "Image mode is not RGB")
        self.assertEqual(generated_image.size, (8, 8), "Image size is incorrect")


if __name__ == '__main__':
    unittest.main()
