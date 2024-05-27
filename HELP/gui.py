# gui.py
import tkinter as tk
from tkinter import messagebox


class TradingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("自动交易系统")
        self.prediction_count = 0
        self.trade_count = 0

        self.label = tk.Label(root, text="系统正在运行...")
        self.label.pack(pady=20)

        self.prediction_label = tk.Label(root, text=f"预测次数: {self.prediction_count}")
        self.prediction_label.pack(pady=10)

        self.trade_label = tk.Label(root, text=f"交易次数: {self.trade_count}")
        self.trade_label.pack(pady=10)

        self.update_button = tk.Button(root, text="更新状态", command=self.update_status)
        self.update_button.pack(pady=10)

    def update_status(self):
        # 在这里添加更新逻辑，例如从文件读取最新统计数据
        self.prediction_count += 1  # 示例，实际应从外部获取数据
        self.trade_count += 1  # 示例，实际应从外部获取数据

        self.prediction_label.config(text=f"预测次数: {self.prediction_count}")
        self.trade_label.config(text=f"交易次数: {self.trade_count}")
        messagebox.showinfo("更新", "系统状态已更新")


if __name__ == "__main__":
    root = tk.Tk()
    app = TradingApp(root)
    root.mainloop()
