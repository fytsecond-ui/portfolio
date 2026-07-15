from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "boss_zhipin_experience_scene.png"

W, H = 1400, 900
BG_TOP = (231, 249, 250)
BG_BOTTOM = (246, 250, 252)
TEAL = (0, 196, 190)
DEEP = (28, 39, 76)
INK = (36, 46, 60)
MUTED = (112, 126, 143)
ORANGE = (255, 151, 87)
YELLOW = (255, 210, 87)
GREEN = (73, 191, 137)
WHITE = (255, 255, 255)
LINE = (218, 229, 236)

font_regular = "C:/Windows/Fonts/msyh.ttc"
font_bold = "C:/Windows/Fonts/msyhbd.ttc"

def font(path, size):
    return ImageFont.truetype(path, size)

f_title = font(font_bold, 54)
f_mid = font(font_bold, 30)
f_body = font(font_regular, 22)
f_small = font(font_regular, 18)
f_icon = font(font_bold, 24)

img = Image.new("RGB", (W, H), BG_TOP)
d = ImageDraw.Draw(img)

for y in range(H):
    t = y / H
    col = tuple(int(BG_TOP[i] * (1 - t) + BG_BOTTOM[i] * t) for i in range(3))
    d.line([(0, y), (W, y)], fill=col)

# Soft abstract background grid
for x in range(80, W, 90):
    d.line([(x, 90), (x, H - 80)], fill=(226, 238, 243), width=1)
for y in range(110, H, 80):
    d.line([(70, y), (W - 80, y)], fill=(226, 238, 243), width=1)

def rounded_box(x1, y1, x2, y2, radius=22, fill=WHITE, outline=None, width=2):
    d.rounded_rectangle([x1, y1, x2, y2], radius=radius, fill=fill, outline=outline, width=width)

def shadow_box(x1, y1, x2, y2, radius=22, fill=WHITE):
    d.rounded_rectangle([x1 + 8, y1 + 10, x2 + 8, y2 + 10], radius=radius, fill=(206, 221, 229))
    rounded_box(x1, y1, x2, y2, radius, fill)

# Central flow path
points = [(250, 530), (420, 420), (610, 515), (790, 390), (990, 505), (1150, 390)]
for i in range(len(points) - 1):
    d.line([points[i], points[i + 1]], fill=TEAL, width=7)
    x1, y1 = points[i + 1]
    x0, y0 = points[i]
    ang = math.atan2(y1 - y0, x1 - x0)
    a1 = ang + math.pi * 0.78
    a2 = ang - math.pi * 0.78
    arrow = [(x1, y1), (x1 + 20 * math.cos(a1), y1 + 20 * math.sin(a1)), (x1 + 20 * math.cos(a2), y1 + 20 * math.sin(a2))]
    d.polygon(arrow, fill=TEAL)

# Header copy
d.text((95, 80), "招聘邀约经验贴", fill=DEEP, font=f_title)
d.text((98, 150), "从触达到到面，把候选人的决策成本降下来", fill=MUTED, font=f_body)
d.rounded_rectangle([1035, 78, 1268, 126], radius=24, fill=DEEP)
d.text((1070, 89), "10:00 优先沟通", fill=WHITE, font=f_body)

# Resume card
shadow_box(95, 250, 390, 470, 24)
d.text((128, 282), "简历筛选", fill=INK, font=f_mid)
d.rounded_rectangle([128, 338, 356, 357], radius=9, fill=(230, 238, 244))
d.rounded_rectangle([128, 378, 320, 397], radius=9, fill=(230, 238, 244))
d.rounded_rectangle([128, 418, 260, 437], radius=9, fill=TEAL)
d.ellipse([315, 280, 355, 320], fill=(255, 222, 205))
d.arc([317, 294, 353, 322], 200, 340, fill=ORANGE, width=3)

# Phone/chat card
shadow_box(455, 225, 720, 415, 24)
d.text((488, 257), "开场三件事", fill=INK, font=f_mid)
for i, txt in enumerate(["我是谁", "岗位是什么", "占用多久"]):
    y = 320 + i * 42
    d.ellipse([492, y, 510, y + 18], fill=TEAL if i == 0 else (211, 229, 235))
    d.text((526, y - 5), txt, fill=INK, font=f_body)
d.rounded_rectangle([652, 300, 690, 365], radius=14, outline=DEEP, width=4)
d.ellipse([668, 352, 674, 358], fill=DEEP)

# Calendar card
shadow_box(805, 205, 1130, 440, 24)
d.text((840, 238), "面试确认", fill=INK, font=f_mid)
d.rounded_rectangle([842, 300, 1088, 398], radius=16, fill=(238, 248, 249), outline=LINE, width=2)
d.rectangle([842, 300, 1088, 330], fill=TEAL)
d.text((870, 346), "时间  链接  联系人", fill=INK, font=f_body)
d.text((872, 374), "准备内容一次说清", fill=MUTED, font=f_small)
d.ellipse([1038, 233, 1088, 283], fill=YELLOW)
d.line([1063, 246, 1063, 260], fill=DEEP, width=4)
d.line([1063, 260, 1076, 267], fill=DEEP, width=4)

# Interview table abstraction
shadow_box(215, 600, 565, 785, 24)
d.text((250, 632), "岗位讲具体的一天", fill=INK, font=f_mid)
d.line([270, 715, 510, 715], fill=DEEP, width=8)
d.ellipse([300, 670, 346, 716], fill=(255, 222, 205))
d.ellipse([432, 670, 478, 716], fill=(255, 222, 205))
d.rounded_rectangle([286, 717, 360, 758], radius=20, fill=TEAL)
d.rounded_rectangle([418, 717, 492, 758], radius=20, fill=ORANGE)

# Salary/offer abstraction
shadow_box(625, 585, 900, 790, 24)
d.text((660, 618), "薪资说结构", fill=INK, font=f_mid)
bars = [(670, 720, 52, TEAL), (735, 690, 82, YELLOW), (800, 655, 117, GREEN)]
for x, y, h, color in bars:
    d.rounded_rectangle([x, y, x + 42, 772], radius=10, fill=color)
d.text((665, 665), "底薪", fill=MUTED, font=f_small)
d.text((730, 635), "绩效", fill=MUTED, font=f_small)
d.text((796, 600), "奖金", fill=MUTED, font=f_small)

# Review funnel
shadow_box(960, 575, 1260, 790, 24)
d.text((995, 608), "复盘看漏斗", fill=INK, font=f_mid)
funnel = [(1010, 675, 1210, 675), (1040, 715, 1180, 715), (1075, 755, 1145, 755)]
for i, (x1, y, x2, _) in enumerate(funnel):
    color = [TEAL, YELLOW, ORANGE][i]
    d.rounded_rectangle([x1, y, x2, y + 20], radius=10, fill=color)
d.text((1010, 645), "触达  接通  约面  到面", fill=MUTED, font=f_small)

# Decorative abstract nodes tied to workflow
for x, y, color in [(250,530,TEAL),(420,420,YELLOW),(610,515,GREEN),(790,390,ORANGE),(990,505,TEAL),(1150,390,DEEP)]:
    d.ellipse([x - 15, y - 15, x + 15, y + 15], fill=color)
    d.ellipse([x - 6, y - 6, x + 6, y + 6], fill=WHITE)

# Footer hint
d.text((96, 828), "主题：筛选、邀约、确认、谈薪、复盘", fill=MUTED, font=f_small)
d.text((1125, 828), "BOSS 有了风格配图", fill=(145, 156, 168), font=f_small)

img.save(OUT)
print(OUT)
