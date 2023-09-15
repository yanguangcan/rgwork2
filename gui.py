import tkinter
# 使用tkinter创建爬取luogu.com.cn题目的GUI界面

def get_filter():
    # 获取用户选择的筛选框
    difficulty = difficulty_var.get()
    keyword = keyword_var.get()
    print("题目难度：", difficulty)
    print("其他关键词：", keyword)

root = tkinter.Tk()
root.title("洛谷爬虫")
root.geometry("600x400")

title_label = tkinter.Label(root, text="欢迎使用洛谷爬虫", font=("Arial", 20))
title_label.pack()

# 添加题目难度和关键词选择框
difficulty_label = tkinter.Label(root, text="题目难度选择：", font=("Arial", 20))
difficulty_label.pack()
difficulty_var = tkinter.StringVar()
dificulties=["暂无评定","入门", "普及-", "普及/提高−", "普及+/提高", "提高+/省选−", "省选/NOI-", "NOI/NOI+/CTSC"]
keywords=["算法", "来源", "标题", "题目编号"]
difficulty_var.set(dificulties[0])  # 默认选择第一个
difficulty_menu = tkinter.OptionMenu(root, difficulty_var, *dificulties)
difficulty_menu.pack()

keyword_label = tkinter.Label(root, text="其他关键词：", font=("Arial", 12))
keyword_label.pack()
keyword_var = tkinter.StringVar()
keyword_entry = tkinter.Entry(root, textvariable=keyword_var, width=30)
keyword_entry.pack()

select_button = tkinter.Button(root, text="爬取题目", font=("Arial", 20), command=get_filter)
select_button.pack()

root.mainloop()



