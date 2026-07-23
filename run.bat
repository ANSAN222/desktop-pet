@echo off
chcp 65001 >nul
echo ========================================
echo     Windows 桌面宠物程序 - 快速启动
echo ========================================
echo.

REM 检查Python是否已安装
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo 错误: 未检测到Python环境
    echo 请先安装Python 3.7+
    echo 下载地址: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo ✓ Python已安装
echo.

REM 检查依赖
echo 检查依赖库...
pip show Pillow >nul 2>&1
if %errorlevel% neq 0 (
    echo 正在安装 Pillow...
    pip install Pillow -q
)

echo ✓ 依赖库已就绪
echo.

REM 检查宠物图片
if not exist "pet_image.png" (
    echo 正在生成默认宠物...
    python -c "from main import DesktopPet; from PIL import Image, ImageDraw; img = Image.new('RGBA', (300, 300), (255, 255, 255, 0)); draw = ImageDraw.Draw(img); draw.ellipse([75, 50, 225, 200], fill=(200, 180, 150, 255), outline=(0, 0, 0, 255), width=3); draw.ellipse([110, 100, 140, 130], fill=(0, 0, 0, 255)); draw.ellipse([160, 100, 190, 130], fill=(0, 0, 0, 255)); draw.ellipse([120, 110, 130, 120], fill=(255, 255, 255, 255)); draw.ellipse([170, 110, 180, 120], fill=(255, 255, 255, 255)); draw.ellipse([145, 145, 155, 155], fill=(0, 0, 0, 255)); draw.arc([130, 150, 170, 180], 0, 180, fill=(0, 0, 0, 255), width=2); draw.ellipse([70, 50, 110, 100], fill=(200, 180, 150, 255), outline=(0, 0, 0, 255), width=2); draw.ellipse([190, 50, 230, 100], fill=(200, 180, 150, 255), outline=(0, 0, 0, 255), width=2); img.save('pet_image.png')" 2>nul || (
        echo 已生成默认宠物图片
    )
)

echo ✓ 宠物图片已就绪
echo.
echo ========================================
echo 正在启动桌面宠物...
echo 按 Ctrl+C 关闭程序
echo ========================================
echo.

python main.py

pause
