from PIL import Image
import os

# 从图片1生成pet_image.png
# 这个脚本会创建一个处理好的宠物图片文件

# 创建一个示例图片（如果需要）
img = Image.new('RGBA', (300, 300), (255, 255, 255, 0))

# 保存为pet_image.png
if not os.path.exists('pet_image.png'):
    # 创建一个占位符
    from PIL import ImageDraw
    draw = ImageDraw.Draw(img)
    
    # 绘制一个简单的圆形作为示例
    draw.ellipse([50, 50, 250, 250], fill=(100, 100, 100, 200), outline=(0, 0, 0, 255))
    
    img.save('pet_image.png')
    print("已创建示例 pet_image.png")
else:
    print("pet_image.png 已存在")
