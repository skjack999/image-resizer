from PIL import Image

def resize_image(input_image, output_image, new_width, new_height):

    try:
        img = Image.open(input_image)
        resized_img = img.resize((new_width, new_height))
        resized_img.save(output_image)
        print("Your work is finishd")
    except Exception as e:
        print(f"have a error: {e}")
input_file = input("Input your photo Name: ")
output_file = input("Input your output image name: ")
new_width = int(input("Input your weight: "))
new_height = int(input("Input your  height:: "))
resize_image(input_file, output_file, new_width, new_height)
