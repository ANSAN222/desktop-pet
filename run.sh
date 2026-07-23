#!/bin/bash

echo "========================================"
echo "  Windows 桌面宠物程序 - 快速启动"
echo "========================================"
echo ""

# 检查Python
if ! command -v python3 &> /dev/null; then
    echo "❌ 错误: 未检测到Python3环境"
    echo "请先安装Python 3.7+"
    exit 1
fi

echo "✓ Python已安装"
echo ""

# 检查依赖
echo "检查依赖库..."
python3 -m pip show Pillow > /dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "正在安装 Pillow..."
    pip3 install Pillow -q
fi

echo "✓ 依赖库已就绪"
echo ""

# 检查宠物图片
if [ ! -f "pet_image.png" ]; then
    echo "正在生成默认宠物..."
    python3 << 'EOF'
from PIL import Image, ImageDraw

img = Image.new('RGBA', (300, 300), (255, 255, 255, 0))
draw = ImageDraw.Draw(img)

# 绘制头部
draw.ellipse([75, 50, 225, 200], fill=(200, 180, 150, 255), outline=(0, 0, 0, 255), width=3)

# 绘制眼睛
draw.ellipse([110, 100, 140, 130], fill=(0, 0, 0, 255))
draw.ellipse([160, 100, 190, 130], fill=(0, 0, 0, 255))
draw.ellipse([120, 110, 130, 120], fill=(255, 255, 255, 255))
draw.ellipse([170, 110, 180, 120], fill=(255, 255, 255, 255))

# 绘制鼻子
draw.ellipse([145, 145, 155, 155], fill=(0, 0, 0, 255))

# 绘制嘴巴
draw.arc([130, 150, 170, 180], 0, 180, fill=(0, 0, 0, 255), width=2)

# 绘制耳朵
draw.ellipse([70, 50, 110, 100], fill=(200, 180, 150, 255), outline=(0, 0, 0, 255), width=2)
draw.ellipse([190, 50, 230, 100], fill=(200, 180, 150, 255), outline=(0, 0, 0, 255), width=2)

img.save('pet_image.png')
print("✓ 已生成默认宠物图片")
EOF
fi

echo "✓ 宠物图片已就绪"
echo ""
echo "========================================"
echo "正在启动桌面宠物..."
echo "按 Ctrl+C 关闭程序"
echo "========================================"
echo ""

python3 main.py
