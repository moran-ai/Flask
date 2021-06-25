import random
from PIL import Image, ImageFont, ImageDraw, ImageFilter

# 随机产生验证码颜色
def generate_random_color():
    """
    返回RGB三通道的随机颜色
    :return:
    """
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# 生成图片
def generate_image(length):
    """
    :param length: 图片验证码的长度
    :return:
    """
    s = 'QWd234ERfsTjavac23456gfjiGFj789sc245rFDS22F42iptYPgdYf56T58HO4N'
    # 画布的大小
    size = (128, 50)
    # 创建画布  new()函数 参数解析：new(图片模式，图片大小,图片颜色，如果省略则默认为黑色)
    img = Image.new('RGB', size, color=generate_random_color())
    # img.show()
    # 创建字体  参数解析：字体路径和字体大小
    font = ImageFont.truetype('C:\Windows\Fonts\simhei.ttf', size=40)
    # 创建ImageDraw()对象，用来画验证码
    # ImageDraw.Draw(im, mode) 参数解析：img:绘制图片的位置 mode:模式(RGB, BGR)可选
    draw = ImageDraw.Draw(img)
    # 绘制验证码
    code = ''
    for i in range(length):
        c = random.choice(s)  # 随机选择文字
        code += c
        # (横坐标，纵坐标) text:文字， fill：颜色 font:字体
        draw.text((5 + random.randint(4, 7) + 20*i, random.randint(5, 9)),
                  text=c, fill=generate_random_color(), font=font)

    # img.show()
    # 绘制干扰线
    for i in range(20):
        x1 = random.randint(0, 130)
        y1 = random.randint(0, 50 / 2)

        x2 = random.randint(0, 130)
        y2 = random.randint(50 / 2, 130)
        draw.line(((x1, y1), (x2, y2)), fill=generate_random_color())

    # 添加滤镜
    img = img.filter(ImageFilter.EDGE_ENHANCE)
    # img.show()
    return img, code

if __name__ == '__main__':
    generate_image(6)
