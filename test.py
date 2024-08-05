import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 模拟从JSON读取的数据
keyboard_data = [
        ["Esc",{"x":1},"F1","F2","F3","F4",{"x":0.5},"F5","F6","F7","F8",{"x":0.5},"F9","F10","F11","F12",{"x":0.25},"PrtSc","Scroll Lock","Pause\nBreak"],
        [{"y":0.5},"~\n`","!\n1","@\n2","#\n3","$\n4","%\n5","^\n6","&\n7","*\n8","(\n9",")\n0","_\n-","+\n=",{"w":2},"Backspace",{"x":0.25},"Insert","Home","PgUp",{"x":0.25},"Num Lock","/","*","-"],
        [{"w":1.5},"Tab","Q","W","E","R","T","Y","U","I","O","P","{\n[","}\n]",{"w":1.5},"|\n\\",{"x":0.25},"Delete","End","PgDn",{"x":0.25},"7\nHome","8\n↑","9\nPgUp",{"h":2},"+"],
        [{"w":1.75},"Caps Lock","A","S","D","F","G","H","J","K","L",":\n;","\"\n'",{"w":2.25},"Enter",{"x":3.5},"4\n←","5","6\n→"],
        [{"w":2.25},"Shift","Z","X","C","V","B","N","M","<\n,",">\n.","?\n/",{"w":2.75},"Shift",{"x":1.25},"↑",{"x":1.25},"1\nEnd","2\n↓","3\nPgDn",{"h":2},"Enter"],
        [{"w":1.25},"Ctrl",{"w":1.25},"Win",{"w":1.25},"Alt",{"w":6.25},"",{"w":1.25},"Alt",{"w":1.25},"Win",{"w":1.25},"Menu",{"w":1.25},"Ctrl",{"x":0.25},"←","↓","→",{"x":0.25,"w":2},"0\nIns",".\nDel"]
    ]

# keyboard_data = [
#         ["Esc",{"x":1},"F1","F2","F3","F4",{"x":0.5},"F5","F6","F7","F8",{"x":0.5},"F9","F10","F11","F12",{"x":0.25},"PrtSc","Scroll Lock","Pause\nBreak"],
# ]

# 初始化绘图
fig, ax = plt.subplots(figsize=(14, 6))

ax.set_xlim(0, 23)
ax.set_ylim(0, 6.5)

def default_key():
    return 1, 1

# 绘制键盘的函数
def draw_keyboard(data):
    y_offset = 0
    width, height = default_key()
    for row in data:
        x_offset = 0
        for item in row:
            if isinstance(item, dict):
                if 'x' in item:
                    x_offset += float(item['x'])
                if 'y' in item:
                    y_offset += float(item['y'])
                if 'w' in item:
                    width = float(item['w'])
                if 'h' in item:
                    height = float(item['h'])
                continue
            # 绘制键
            ax.add_patch(patches.Rectangle((x_offset, y_offset), width, height, edgecolor='black', facecolor='lightgray'))
            if isinstance(item, str):
                lines = item.split("\n")
                for i, line in enumerate(lines):
                    ax.text(x_offset + 0.5 * width, y_offset + (0.5 + i / 2) * height / len(lines), line,
                            horizontalalignment='center', verticalalignment='center')
            elif isinstance(item, dict):
                # Handle multiple characters with specified positions
                for text, pos in item.get("text_positions", {}).items():
                    ax.text(x_offset + pos['x'] * width, y_offset + pos['y'] * height, text,
                            horizontalalignment='center', verticalalignment='center')            
            x_offset += width
            width, height = default_key()
        y_offset += 1
    ax.invert_yaxis()


draw_keyboard(keyboard_data)

# 配置显示
ax.set_aspect('equal')
ax.axis('off')  # 关闭坐标轴
plt.show()
