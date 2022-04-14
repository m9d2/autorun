import cv2
import paddlehub as hub


class OcrHelper:
    ocr = ''

    def __init__(self):
        self.ocr = hub.Module(name="chinese_ocr_db_crnn_mobile")

    def position(self, path, key):
        np_images = [cv2.imread(path)]
        results = self.ocr.recognize_text(
            images=np_images,  # 图片数据，ndarray.shape 为 [H, W, C]，BGR格式
            use_gpu=False,  # 是否使用 GPU；若使用GPU，请先设置CUDA_VISIBLE_DEVICES环境变量
            # output_dir='ocr_result',  # 图片的保存路径，默认设为 ocr_result
            # visualization=True,       # 是否将识别结果保存为图片文件
            box_thresh=0.5,  # 检测文本框置信度的阈值
            text_thresh=0.5)  # 识别中文文本置信度的阈值
        for result in results:
            for info in result['data']:
                text = info['text']
                if text.find(key) == 0:
                    return info['text_box_position'][0]
        return [0, 0]


if __name__ == '__main__':
    orc = OcrHelper()
    position = orc.position('D:\\img\\zdl2.png', '我知道了')
    print(position)
