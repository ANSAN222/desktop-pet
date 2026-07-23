@echo off
chcp 65001 >nul
cls

echo ========================================
echo     Windows 桌面宠物程序 - 启动
echo ========================================
echo.

REM 第一步：安装依赖
echo [1/3] 正在安装依赖库...
python -m pip install Pillow --user -q
if %errorlevel% neq 0 (
    echo 安装失败，尝试其他方法...
    pip install Pillow --user -q
)
echo ✓ 依赖库安装完成
echo.

REM 第二步：生成宠物图片
if not exist "pet_image.png" (
    echo [2/3] 正在生成宠物图片...
    python generate_pet.py
)
echo ✓ 宠物图片已就绪
echo.

REM 第三步：启动程序
echo [3/3] 正在启动程序...
echo.
python main.py

if %errorlevel% neq 0 (
    echo.
    echo ========================================
    echo 程序出错！错误代码: %errorlevel%
    echo ========================================
    echo.
    pause
)
