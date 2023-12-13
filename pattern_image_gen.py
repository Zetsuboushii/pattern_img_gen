from PIL import Image


def generate_pattern_image(image1: str, image2: str, image3: str, source_width: int, source_height: int):
    target_width, target_height = 1920, 1080
    final_image = Image.new('RGBA', (target_width, target_height), (0, 0, 0, 0))

    source_paths = [image1, image2, image3]

    source_img_size = (source_width, source_height)
    reps_x, reps_y = target_width // source_img_size[0], target_height // source_img_size[1]

    for i in range(reps_y):
        for j in range(reps_x):
            img = Image.open(source_paths[(i + j) % len(source_paths)]).convert('RGBA')

            rotated_img = img.rotate(45, expand=True)

            x = j * source_img_size[0] - (rotated_img.width - source_img_size[0]) / 2
            y = i * source_img_size[1] - (rotated_img.height - source_img_size[1]) / 2

            final_image.paste(rotated_img, (int(x), int(y)), rotated_img)

    final_image = final_image.crop((0, 0, target_width, target_height))

    final_image.save('output.png', 'png')
    print('Generated Image')


if __name__ == '__main__':
    generate_pattern_image("C:\\Users\\lukeg\\Desktop\\sprites\\hofmann.png", "C:\\Users\\lukeg\\Desktop\\sprites\\kruse.png", "C:\\Users\\lukeg\\Desktop\\sprites\\stroetmann.png", 128, 128)
