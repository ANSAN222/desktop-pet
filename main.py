import tkinter as tk
from tkinter import Menu
import tkinter.font as tkFont
from PIL import Image, ImageTk, ImageDraw
import os
import random
import math
import threading
import time

class DesktopPet:
    def __init__(self, root):
        self.root = root
        self.root.attributes('-topmost', True)
        self.root.attributes('-transparentcolor', '#ffffff')
        self.root.overrideredirect(True)
        
        # 配置窗口
        self.pet_size = 200
        self.pet_x = 100
        self.pet_y = 100
        self.is_topmost = True
        self.is_dragging = False
        self.drag_start_x = 0
        self.drag_start_y = 0
        
        # 动画状态
        self.animation_state = 0
        self.animation_type = None
        self.animation_frame = 0
        self.animation_playing = False
        
        # 对话框
        self.bubble = None
        self.bubble_text = ""
        self.bubble_timer = None
        
        # 对话文本
        self.dialogues = [
            "你好呀~",
            "摸我~",
            "嘿嘿",
            "汪！",
            "不要挠我！",
            "哈哈，痒痒~",
            "再来一次！",
            "我很可爱吧",
            "你在吗？",
            "给我零食！",
            "困了呢",
            "玩得开心！",
            "别走~",
            "呀！",
            "嗷呜~"
        ]
        
        # 初始化窗口
        self.setup_window()
        self.load_pet_image()
        self.setup_events()
        self.create_context_menu()
        
    def setup_window(self):
        """设置窗口属性"""
        self.root.geometry(f"{self.pet_size}x{self.pet_size}+{self.pet_x}+{self.pet_y}")
        self.canvas = tk.Canvas(self.root, bg='white', highlightthickness=0, 
                                width=self.pet_size, height=self.pet_size)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
    def load_pet_image(self):
        """加载并处理宠物图片"""
        image_path = "pet_image.png"
        
        if not os.path.exists(image_path):
            self.create_placeholder_image()
        
        self.original_image = Image.open(image_path)
        self.update_pet_display()
        
    def create_placeholder_image(self):
        """如果没有图片，创建占位符"""
        img = Image.new('RGBA', (200, 200), (255, 255, 255, 0))
        draw = ImageDraw.Draw(img)
        draw.ellipse([50, 50, 150, 150], fill=(100, 100, 100, 200))
        img.save("pet_image.png")
        
    def remove_background(self, image):
        """移除图片白色背景"""
        if image.mode != 'RGBA':
            image = image.convert('RGBA')
        
        data = image.getdata()
        new_data = []
        
        for item in data:
            # 如果像素接近白色，设为透明
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                new_data.append((255, 255, 255, 0))
            else:
                new_data.append(item)
        
        image.putdata(new_data)
        return image
        
    def update_pet_display(self):
        """更新宠物显示"""
        img = self.original_image.copy()
        img = self.remove_background(img)
        
        # 根据动画状态变形图片
        if self.animation_type == "compress":
            # 压扁效果
            progress = min(self.animation_frame / 5, 1.0)
            if progress < 0.5:
                scale = 1 - progress
            else:
                scale = progress
            height = int(img.height * scale * 1.2)
            img = img.resize((img.width, max(height, 10)), Image.Resampling.LANCZOS)
            
        elif self.animation_type == "shake":
            # 抖动效果
            offset = 5 * math.sin(self.animation_frame * 0.5)
            new_img = Image.new('RGBA', img.size, (255, 255, 255, 0))
            new_img.paste(img, (int(offset), 0), img)
            img = new_img
            
        elif self.animation_type == "jump":
            # 跳跃效果
            progress = (self.animation_frame % 10) / 10
            bounce = abs(math.sin(progress * math.pi)) * 20
            new_img = Image.new('RGBA', (img.width, img.height + 30), (255, 255, 255, 0))
            new_img.paste(img, (0, int(30 - bounce)), img)
            img = new_img
        
        # 调整大小
        img_resized = img.resize((self.pet_size, self.pet_size), Image.Resampling.LANCZOS)
        self.pet_photo = ImageTk.PhotoImage(img_resized)
        
        self.canvas.delete("pet")
        self.canvas.create_image(self.pet_size // 2, self.pet_size // 2, 
                                 image=self.pet_photo, tag="pet")
        
    def play_animation(self, anim_type):
        """播放动画"""
        if self.animation_playing:
            return
            
        self.animation_type = anim_type
        self.animation_frame = 0
        self.animation_playing = True
        
        frames = 20 if anim_type == "jump" else 15
        
        def animate():
            if self.animation_frame < frames:
                self.animation_frame += 1
                self.update_pet_display()
                self.root.after(30, animate)
            else:
                self.animation_playing = False
                self.animation_type = None
                self.animation_frame = 0
                self.update_pet_display()
        
        animate()
        
    def show_dialogue(self):
        """显示对话气泡"""
        if self.bubble_timer:
            self.root.after_cancel(self.bubble_timer)
        
        self.bubble_text = random.choice(self.dialogues)
        
        # 创建气泡
        if self.bubble is None:
            self.bubble = tk.Toplevel(self.root)
            self.bubble.attributes('-topmost', True)
            self.bubble.overrideredirect(True)
            self.bubble_label = tk.Label(self.bubble, text=self.bubble_text,
                                        font=("Arial", 12, "bold"),
                                        bg="#FFE680", fg="#000000",
                                        padx=10, pady=5, relief=tk.SOLID, borderwidth=2)
            self.bubble_label.pack()
        else:
            self.bubble_label.config(text=self.bubble_text)
        
        # 位置
        bubble_x = self.pet_x + self.pet_size
        bubble_y = self.pet_y
        self.bubble.geometry(f"+{bubble_x}+{bubble_y}")
        
        # 3秒后消失
        self.bubble_timer = self.root.after(3000, self.hide_dialogue)
        
    def hide_dialogue(self):
        """隐藏对话气泡"""
        if self.bubble:
            self.bubble.destroy()
            self.bubble = None
        self.bubble_timer = None
        
    def on_canvas_click(self, event):
        """点击宠物触发互动"""
        animations = ["jump", "compress", "shake"]
        self.play_animation(random.choice(animations))
        self.show_dialogue()
        
    def on_mouse_down(self, event):
        """鼠标按下开始拖动"""
        self.is_dragging = True
        self.drag_start_x = event.x_root - self.pet_x
        self.drag_start_y = event.y_root - self.pet_y
        
    def on_mouse_move(self, event):
        """鼠标移动时拖动宠物"""
        if self.is_dragging:
            self.pet_x = event.x_root - self.drag_start_x
            self.pet_y = event.y_root - self.drag_start_y
            self.root.geometry(f"{self.pet_size}x{self.pet_size}+{self.pet_x}+{self.pet_y}")
            
    def on_mouse_up(self, event):
        """鼠标释放"""
        self.is_dragging = False
        
    def on_mouse_wheel(self, event):
        """滚轮调整大小"""
        if event.delta > 0:
            self.pet_size = min(self.pet_size + 20, 400)
        else:
            self.pet_size = max(self.pet_size - 20, 50)
        
        self.root.geometry(f"{self.pet_size}x{self.pet_size}+{self.pet_x}+{self.pet_y}")
        self.canvas.config(width=self.pet_size, height=self.pet_size)
        self.update_pet_display()
        
    def toggle_topmost(self):
        """切换置顶状态"""
        self.is_topmost = not self.is_topmost
        self.root.attributes('-topmost', self.is_topmost)
        
    def resize_pet(self):
        """调整大小菜单项"""
        pass
        
    def exit_app(self):
        """退出程序"""
        if self.bubble:
            self.bubble.destroy()
        self.root.quit()
        
    def create_context_menu(self):
        """创建右键菜单"""
        self.context_menu = Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="调整大小", command=self.resize_pet)
        self.context_menu.add_command(label="置顶开关", command=self.toggle_topmost)
        self.context_menu.add_separator()
        self.context_menu.add_command(label="退出", command=self.exit_app)
        
    def on_right_click(self, event):
        """右键菜单"""
        try:
            self.context_menu.tk_popup(event.x_root, event.y_root)
        except:
            pass
        
    def setup_events(self):
        """设置事件"""
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<B1-Motion>", self.on_mouse_move)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)
        self.canvas.bind("<Button-2>", self.on_mouse_down)
        self.canvas.bind("<Button-3>", self.on_right_click)
        self.root.bind("<MouseWheel>", self.on_mouse_wheel)
        self.root.bind("<Button-4>", self.on_mouse_wheel)
        self.root.bind("<Button-5>", self.on_mouse_wheel)


def main():
    root = tk.Tk()
    root.title("Desktop Pet")
    app = DesktopPet(root)
    root.mainloop()


if __name__ == "__main__":
    main()
