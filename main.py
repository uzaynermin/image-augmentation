from builtins import type, range
import cv2
import gradio as gr


def flip_image(img, flip_code):
    flipped_image = cv2.flip(img, flip_code)
    return flipped_image


def scale_image(img, scale_percent):
    print(f"image w: {img.shape[0]}, image h: {img.shape[1]}")
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    print(f"new image w: {width}, image h: {height}")
    dim = (height, width)
    resized_image = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    return resized_image


def rotate_image(img, angle):
    rotated_image = cv2.rotate(img, angle)
    return rotated_image


def color_manipulation(img, x):
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray_image


def blur(img, x):
    blured = cv2.blur(img, (x,x),cv2.BORDER_DEFAULT)
    return blured


if __name__ == '__main__':
    operations = {
        "Rotating": rotate_image,
        "Scaling": scale_image,
        "Flipping": flip_image,
        "Color Manipulation": color_manipulation,
        "Blur": blur
    }

    inputs = gr.components.Image(label="Original Image")
    outputs = gr.components.Image(label="Result")

    operation_choice_ind = gr.components.Dropdown(choices=list(operations.keys()), label="Select")
    parameter = gr.Textbox(label="function parameter")
    print(f"parameter: {parameter}")

    def apply(img, ind, param):
        print(f"ind: {ind} param: {param}")

        operation = operations[ind]
        return operation(img, int(param))


    demo = gr.Interface(fn=apply, inputs=[inputs, operation_choice_ind, parameter], outputs=outputs)
    demo.launch(share=True)
