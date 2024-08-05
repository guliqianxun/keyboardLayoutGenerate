# Keyboard Layout Generator

This is a simple tool to generate keyboard layouts for virtual keyboards. It is written in Python and uses the Tkinter library for the GUI.

### 绘制键盘布局
绘制键盘布局的程序使用`matplotlib`库的`patches`模块来创建矩形代表键盘上的每个键。每个键可以通过一个字典指定其大小和位置的偏移。这些键可以包含文本，且文本可以跨越多行。

#### 键的属性定义
- **`w`**: 定义键的宽度。
- **`h`**: 定义键的高度。
- **`x`**: 定义横向偏移量，即该键距离前一个键的右边缘的距离。
- **`y`**: 定义纵向偏移量，即该键所在行的起始绘制点距离上一行的底部的距离。

#### 函数功能
- **`default_key()`**: 返回默认键的宽度和高度（1x1）。
- **`draw_keyboard(data)`**: 根据输入数据绘制整个键盘。该函数遍历`data`中的每一行和每一个元素，根据元素属性（如宽度、高度、偏移等）来绘制每个键。

#### 文本处理
对于有两行文本的键，如"Shift\nUp"，文本会被分割成两行并在键内垂直居中显示。每行文本的垂直位置是通过键的高度动态计算，以确保文本在键内均匀分布。

### 坐标系调整
`ax.invert_yaxis()`函数的使用是为了调整matplotlib的默认坐标系统，使得绘图的起点从左上角开始，而不是通常的左下角。这样做更符合计算机图形和GUI设计中常用的坐标系统，使得视觉呈现与实际的物理键盘布局更为一致。

results how to use the tool are shown below.
![./keyboard_layout_generate_result.png]
## Cited
https://github.com/ijprest/kle-serial/tree/master
http://www.keyboard-layout-editor.com/#/
https://github.com/ijprest/keyboard-layout-editor/wiki/Serialized-Data-Format