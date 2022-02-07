<!--
 * @Author: Zhanglei
 * @Date: 2022-02-02 15:06:30
 * @LastEditors: Zhanglei
 * @LastEditTime: 2022-02-02 15:28:29
 * @Description: file content
-->

# GDB调试

## gdb调试准备
- `gdb 调试程序 --slient`
- 调试程序必须带有debugging信息
- gcc 编译带 -g 
- 调试命令
  - b 行数 设置断点
  - r run程序到断点位置
  - c continue到下一个断点
  - n  next下一行
  - p print参数值
  - l list列出当前程序源码
  - q quit退出gdb调试

## 调试带参数的程序
- `run/start 参数`
- ```cpp
   set args 参数
   run
   ```
- `gdb --args 程序 参数`

## 调试core文件
- `gdb 程序 core文件`
- `ulimit -c unlimited ` 不设置core文件大小

## 调试已经运行的程序
- `ps -ef|grep 进程名`
- `attach pid`