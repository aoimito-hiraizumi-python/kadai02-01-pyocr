from PIL import Image
import datetime
import sys
import glob
# import os
import pyocr
import pyocr.builders


tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No OCR tool found")
    sys.exit(1)

tool = tools[0]

# file_path = Image.open("images/01.png")
# file_path.show()

def image_to_text(file_path):
    txt = tool.image_to_string(
        Image.open(file_path),
        lang="jpn",
        builder=pyocr.builders.DigitBuilder(tesseract_layout=6)
    )
    return txt

def main():
    file_paths = glob.glob("images/*")
    # to_dir = "outputs"
    txts = []
    dt_now = datetime.datetime.now()
    
    for file_path in file_paths:
        txt = int(image_to_text(file_path))

        # filename = os.path.splitext(os.path.basename(file_path))[0]
        # # os.path.splitext() パスから拡張子以外と拡張子に分割されたタプルで値を取得
        # # os.path.splitext("images/01.png") -> ('images/01', '.png')
        # # os.path.basename() パスからファイル名のみを取得
        # # print(os.path.basename(images/01.png)) 出力 -> 01.png

        # to_path = os.path.join(to_dir, filename + ".txt")
        # # 出力先のパスを生成
        # os.path.join() 引数に渡した2つの文字列を結合し、1つのパスにする
        # print(os.path.join(outputs, 01.txt)) -> outputs/01.txt
        # print(to_path)

        # with open("to_path", mode="a") as f:
        #     f.writelines(txt)
        
        txts.append(txt)
    with open("cal.txt", "w") as f:
        f.writelines(str(sum(txts)))
    # print(sum(txts))

    with open("cal.txt", "r") as r:
        # print(r.read())
        cal_sum = r.read()
    
    print(str(dt_now.year) + "/" + str(dt_now.month) + "/" + str(dt_now.day) + "の摂取カロリーは" + cal_sum + "kcalです。")



if __name__ == "__main__":
    main()
