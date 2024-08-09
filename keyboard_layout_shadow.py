import matplotlib.pyplot as plt
import matplotlib.patches as patches

# keyboard layout data
keyboard_data = [
    ["Esc",{"x":1},"F1","F2","F3","F4",{"x":0.5},"F5","F6","F7","F8",{"x":0.5},"F9","F10","F11","F12",{"x":0.25},"PrtSc","Scroll","Pause"],
    [{"y":0.5},"~\n`","!\n1","@\n2","#\n3","$\n4","%\n5","^\n6","&\n7","*\n8","(\n9",")\n0","_\n-","+\n=",{"w":2},"Backspace",{"x":0.25},"Insert","Home","PgUp",{"x":0.25},"Num","/","*","-"],
    [{"w":1.5},"Tab","Q","W","E","R","T","Y","U","I","O","P","{\n[","}\n]",{"w":1.5},"|\n\\",{"x":0.25},"Delete","End","PgDn",{"x":0.25},"7\nHome","8\n↑","9\nPgUp",{"h":2},"+"],
    [{"w":1.75},"Caps","A","S","D","F","G","H","J","K","L",":\n;","\"\n'",{"w":2.25},"Enter",{"x":3.5},"4\n←","5","6\n→"],
    [{"w":2.25},"Shift","Z","X","C","V","B","N","M","<\n,",">\n.","?\n/",{"w":2.75},"Shift",{"x":1.25},"↑",{"x":1.25},"1\nEnd","2\n↓","3\nPgDn",{"h":2},"Enter"],
    [{"w":1.25},"Ctrl",{"w":1.25},"Win",{"w":1.25},"Alt",{"w":6.25},"",{"w":1.25},"Alt",{"w":1.25},"Win",{"w":1.25},"Menu",{"w":1.25},"Ctrl",{"x":0.25},"←","↓","→",{"x":0.25,"w":2},"0\nIns",".\nDel"]
]

fig, ax = plt.subplots(figsize=(16, 7))

ax.set_xlim(0, 23)
ax.set_ylim(0, 6.6)

def default_key():
    return 1, 1

def draw_key(ax, x, y, width, height, text):
    shadow = patches.Rectangle((x+0.05, y-0.05), width, height, facecolor='darkgray', edgecolor='none', zorder=1)
    ax.add_patch(shadow)
    key = patches.Rectangle((x, y), width, height, facecolor='white', edgecolor='black', linewidth=1, zorder=2)
    ax.add_patch(key)
    top = patches.Rectangle((x+0.05, y+0.05), width-0.1, height-0.1, facecolor='lightgray', edgecolor='black', linewidth=0.5, zorder=3)
    ax.add_patch(top)
    lines = text.split("\n")
    for i, line in enumerate(lines):
        ax.text(x + width/2, y + (i+1)/(len(lines)+1) * height, line, ha='center', va='center', fontdict={'size': 8}, color='black', zorder=4)

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
            if isinstance(item, str):
                draw_key(ax, x_offset, y_offset, width, height, item)
            x_offset += width
            width, height = default_key()
        y_offset += 1
    ax.invert_yaxis()

draw_keyboard(keyboard_data)

ax.set_aspect('equal')
ax.axis('off')
plt.tight_layout()
plt.show()