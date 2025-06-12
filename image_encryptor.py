from PIL import Image

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    image = image.convert("RGB")
    pixels = image.load()

    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256
            )

    image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")


def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    image = image.convert("RGB")
    pixels = image.load()

    width, height = image.size

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            pixels[x, y] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256
            )

    image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")


def main():
    print("Simple Image Encryption Tool")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = input("Choose an option (1/2): ")

    input_path = input("Enter input image path: ")
    output_path = input("Enter output image path: ")
    key = int(input("Enter numeric key (1–255): "))

    if choice == "1":
        encrypt_image(input_path, output_path, key)
    elif choice == "2":
        decrypt_image(input_path, output_path, key)
    else:
        print("Invalid option selected.")


if __name__ == "__main__":
    main()