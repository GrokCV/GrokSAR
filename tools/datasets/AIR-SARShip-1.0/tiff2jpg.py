import os
import cv2


def convert_tiff_to_jpg(input_folder, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 获取输入文件夹中的所有TIFF文件
    tiff_files = [f for f in os.listdir(input_folder) if f.endswith(".tiff") or f.endswith(".tif")]

    for tiff_file in tiff_files:
        input_file = os.path.join(input_folder, tiff_file)
        output_file = os.path.join(output_folder, tiff_file.replace(".tiff", ".jpg").replace(".tif", ".jpg"))

        try:
            # 使用OpenCV打开TIFF图像文件
            tiff_image = cv2.imread(input_file, cv2.IMREAD_UNCHANGED)

            if tiff_image is not None:
                # 如果TIFF图像只有一个通道，将其转换为三通道
                if tiff_image.shape[-1] == 1:
                    tiff_image = cv2.cvtColor(tiff_image, cv2.COLOR_GRAY2BGR)

                # 保存为JPEG图像
                cv2.imwrite(output_file, tiff_image)
                print(f'成功将{input_file}转换为{output_file}')
            else:
                print(f'无法打开文件: {input_file}')
        except Exception as e:
            print(f'转换失败: {e}')


if __name__ == "__main__":
    input_folder = "./images"  # 包含TIFF文件的文件夹路径
    output_folder = "./JPEGImages"  # 保存JPEG文件的文件夹路径

    convert_tiff_to_jpg(input_folder, output_folder)