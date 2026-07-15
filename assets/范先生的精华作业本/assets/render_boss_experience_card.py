from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import textwrap

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "boss_zhipin_experience_card.png"

W, H = 1240, 1754
BG = (232, 249, 251)
WHITE = (255, 255, 255)
TEXT = (38, 44, 54)
MUTED = (120, 130, 145)
TEAL = (0, 196, 190)
NAVY = (24, 34, 75)
LINE = (229, 235, 242)

font_regular = "C:/Windows/Fonts/msyh.ttc"
font_bold = "C:/Windows/Fonts/msyhbd.ttc"
font_light = "C:/Windows/Fonts/msyhl.ttc"

def font(path, size):
    return ImageFont.truetype(path, size)

f_logo = font(font_bold, 34)
f_nav = font(font_bold, 22)
f_author = font(font_bold, 25)
f_sub = font(font_regular, 19)
f_body = font(font_regular, 25)
f_small = font(font_regular, 18)
f_dot = font(font_bold, 30)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

# Top site bar
d.rectangle([0, 0, W, 86], fill=(255, 255, 255))
d.rounded_rectangle([166, 10, 1000, 56], radius=24, fill=(239, 245, 252))
d.text((190, 26), "youle.zhipin.com/recommend/selected/?ka=header-find", fill=(44, 52, 64), font=f_small)
d.rectangle([0, 86, W, 178], fill=NAVY)
d.rectangle([0, 86, 360, 178], fill=(20, 92, 88))
d.text((118, 112), "BOSS 直聘", fill=TEAL, font=f_logo)
nav_items = ["首页", "职位", "公司", "校园·海归", "APP", "有了", "海外"]
nx = 320
for item in nav_items:
    color = TEAL if item == "有了" else (236, 246, 248)
    d.text((nx, 121), item, fill=color, font=f_nav)
    nx += 88 if item != "校园·海归" else 140
d.text((1160, 121), "范宇廷", fill=(236, 246, 248), font=f_nav)

# Tab bar
d.rectangle([0, 178, W, 288], fill=WHITE)
tabs = [("有了", 330), ("个人主页", 430), ("社区公约", 555)]
for label, x in tabs:
    d.text((x, 220), label, fill=(18, 28, 42), font=f_nav if label == "有了" else font(font_regular, 22))
d.rectangle([328, 272, 374, 276], fill=TEAL)
d.rounded_rectangle([920, 205, 1172, 264], radius=30, outline=(224, 230, 238), width=2, fill=(255,255,255))
d.text((948, 224), "搜索社区话题和内容", fill=(170, 178, 190), font=f_sub)

# Content panel
left, top, right = 210, 288, 1035
d.rectangle([left, top, right, H], fill=WHITE)
d.line([235, top+8, right-40, top+8], fill=LINE, width=2)

# Avatar
cx, cy = left + 43, top + 90
d.ellipse([cx-24, cy-24, cx+24, cy+24], fill=(247, 207, 197))
d.ellipse([cx-13, cy-20, cx+15, cy+8], fill=(237, 162, 145))
d.ellipse([cx-11, cy-2, cx+11, cy+20], fill=(255, 226, 211))
d.arc([cx-16, cy-8, cx+16, cy+20], 200, 340, fill=(106, 70, 70), width=2)
d.text((left+82, top+60), "奈财（互关互赞）", fill=TEXT, font=f_author)
d.text((left+82, top+96), "互关互赞互评～", fill=MUTED, font=f_sub)
d.text((right-70, top+70), "•••", fill=(160, 166, 176), font=f_dot)

post = [
    ("1、邀约时间尽量放在上午10:00", [
        "有经验的HR都知道，上午10:00是候选人状态相对稳定、手机也更容易接通的时间。太早像催命，太晚容易被各种会议、通勤和临时安排打断。",
        "如果岗位比较急，也不要一上来就连续轰炸。先确认对方是否方便沟通，再给两个可选时间，比单方面通知更容易被接受。",
    ]),
    ("2、介绍公司时不要只背官网", [
        "候选人不关心“我们成立于哪一年”这种流水账，他更关心三件事：这家公司靠什么赚钱、这个岗位具体做什么、进去以后有没有人带。",
        "介绍公司时，只讲好的地方，只讲跟岗位相关的地方，只讲对方能听懂的地方。重要的事情说三遍：别像念PPT，别像念PPT，别像念PPT。",
    ]),
    ("3、岗位缺点要换一种说法", [
        "公司小，不要说“体系不完善”，可以说“流程短，事情推进快，个人参与度高”。",
        "岗位新，不要说“什么都要从零开始”，可以说“空间比较大，适合想做完整项目的人”。",
        "工作忙，不要说“强度很高”，可以说“阶段性节奏会比较紧，适合执行力强、希望快速成长的人”。",
    ]),
    ("4、面试前一定要做一次预热", [
        "面试前一天发一句确认，比当天临时找人强很多。内容不用复杂：时间、地点、面试形式、联系人、需要准备什么，一次说清楚。",
        "很多候选人不是故意爽约，只是信息太散、成本太高、心里没底。你把确定性给足，对方来的概率就会高很多。",
    ]),
]

def draw_wrapped(text, x, y, max_chars=33, line_h=41):
    lines = []
    for para_line in text.split("\n"):
        lines.extend(textwrap.wrap(para_line, width=max_chars, break_long_words=False, replace_whitespace=False))
    for line in lines:
        d.text((x, y), line, fill=TEXT, font=f_body)
        y += line_h
    return y

x = left + 24
y = top + 150
for heading, paras in post:
    y = draw_wrapped(heading, x, y, max_chars=34)
    y += 34
    for para in paras:
        y = draw_wrapped(para, x, y, max_chars=36)
        y += 38
    y += 8

# Bottom platform UI hints
d.rounded_rectangle([1164, 1535, 1210, 1595], radius=10, fill=(255,255,255), outline=(229,235,242))
d.line([1178,1560,1187,1551,1196,1560], fill=(126,135,148), width=4)
d.text((1176, 1570), "TOP", fill=(126,135,148), font=f_small)
d.rounded_rectangle([62, 1710, 1120, 1730], radius=10, fill=(190, 199, 208))

img.save(OUT)
print(OUT)
