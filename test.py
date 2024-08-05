import matplotlib.pyplot as plt
import matplotlib.patches as patches

# 模拟从JSON读取的数据
# keyboard_data = [
#         ["Esc",{"x":1},"F1","F2","F3","F4",{"x":0.5},"F5","F6","F7","F8",{"x":0.5},"F9","F10","F11","F12",{"x":0.25},"PrtSc","Scroll Lock","Pause\nBreak"],
#         [{"y":0.5},"~\n`","!\n1","@\n2","#\n3","$\n4","%\n5","^\n6","&\n7","*\n8","(\n9",")\n0","_\n-","+\n=",{"w":2},"Backspace",{"x":0.25},"Insert","Home","PgUp",{"x":0.25},"Num Lock","/","*","-"],
#         [{"w":1.5},"Tab","Q","W","E","R","T","Y","U","I","O","P","{\n[","}\n]",{"w":1.5},"|\n\\",{"x":0.25},"Delete","End","PgDn",{"x":0.25},"7\nHome","8\n↑","9\nPgUp",{"h":2},"+"],
#         [{"w":1.75},"Caps Lock","A","S","D","F","G","H","J","K","L",":\n;","\"\n'",{"w":2.25},"Enter",{"x":3.5},"4\n←","5","6\n→"],
#         [{"w":2.25},"Shift","Z","X","C","V","B","N","M","<\n,",">\n.","?\n/",{"w":2.75},"Shift",{"x":1.25},"↑",{"x":1.25},"1\nEnd","2\n↓","3\nPgDn",{"h":2},"Enter"],
#         [{"w":1.25},"Ctrl",{"w":1.25},"Win",{"w":1.25},"Alt",{"w":6.25},"",{"w":1.25},"Alt",{"w":1.25},"Win",{"w":1.25},"Menu",{"w":1.25},"Ctrl",{"x":0.25},"←","↓","→",{"x":0.25,"w":2},"0\nIns",".\nDel"]
#     ]

keyboard_data = [
        ["Esc",{"x":1},"F1","F2","F3","F4",{"x":0.5},"F5","F6","F7","F8",{"x":0.5},"F9","F10","F11","F12",{"x":0.25},"PrtSc","Scroll Lock","Pause\nBreak"],
        [{"y":0.5},"~\n`","!\n1","@\n2","#\n3","$\n4","%\n5","^\n6","&\n7","*\n8","(\n9",")\n0","_\n-","+\n=",{"w":2},"Backspace",{"x":0.25},"Insert","Home","PgUp",{"x":0.25},"Num Lock","/","*","-"],
]

# 初始化绘图
fig, ax = plt.subplots(figsize=(12, 4))
ax.set_xlim(0, 20)
ax.set_ylim(0, 5)

def default_key():
    return 1, 1

# 绘制键盘的函数
def draw_keyboard(data):
    dict_last = False
    y_offset = 0
    width, height = default_key()
    for row in data[::-1]:
        x_offset = 0
        for item in row:
            if isinstance(item, dict):
                dict_last = True
                if 'x' in item:
                    x_offset += int(item['x'])
                if 'y' in item:
                    y_offset += int(item['y'])
                if 'w' in item:
                    width = int(item['w'])
                if 'h' in item:
                    height = int(item['h'])
                continue
            if dict_last == False:
                 width, height = default_key()

            
            # 绘制键
            ax.add_patch(patches.Rectangle((x_offset, y_offset), width, height, edgecolor='black', facecolor='lightgray'))
            ax.text(x_offset + 0.5 * width, y_offset + 0.5 * height, item.split("\n")[0],
                    horizontalalignment='center', verticalalignment='center')
            x_offset += width
            dict_last = False
        y_offset += 1

draw_keyboard(keyboard_data)

# 配置显示
ax.set_aspect('equal')
ax.axis('off')  # 关闭坐标轴
plt.show()
