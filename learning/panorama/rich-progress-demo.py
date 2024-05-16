from rich.progress import track
import time
from rich.console import Console
console = Console()
console.print("Hello, [bold magenta]World[/bold magenta]!", ":vampire:", locals(),style="bold red")
# 模拟一个耗时的任务
for step in track(range(100)):  # range的范围就是进度条的总步数
    time.sleep(0.1)  # 这里是模拟耗时操作，实际使用中可能是数据处理、文件读写等