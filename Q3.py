from pyecharts.charts import WordCloud,Page,Bar,Pie
import jieba.posseg as pseg
import csv
from pyecharts import options as opts


txt_filename = './data/倚天屠龙记.txt'
result_filename = './output/倚天屠龙记-人物词频-pseg.csv'
"""
# 从文件读取文本
txt_file = open(txt_filename, 'r', encoding='utf-8')
content = txt_file.read()
txt_file.close()
print('文件读取完成')

#接下来找到出现的所有人名
words =pseg.cut(content)
name_dict = {}
notnames = ['洪水','安危','智慧','大德','木剑','多谢','冷笑','言语','小姐','小兄弟','二人','令人','师叔',\
            '奥妙','恩师',"武当派","武功","明白","约莫","师兄","师兄弟","师哥","寻思","比武","明白","师哥"]

    
for w in words:
    if(len(w.word)==1):
        continue#忽略一个字的情况
    if 'nr' in w.flag:  # nr代表人名
        if(w.word in notnames):#记录不是人名被误判的
            continue
        if w.word in name_dict.keys():
            name_dict[w.word] += 1
        else:
            name_dict[w.word] = 1

delete = []    

for key in name_dict.keys():
    if(key == "芷若" or key=="周姑娘"):
        name_dict['周芷若'] += name_dict[key]
        delete.append(key)
    elif(key == "郡主" or key=="赵姑娘" or key=="敏敏"):
        name_dict['赵敏'] += name_dict[key]
        delete.append(key)
    elif(key == "蛛儿" or key=="阿离" or key=="殷姑娘"):
        name_dict['殷离'] += name_dict[key]
        delete.append(key)
        
for d in delete:
    del name_dict[d]
            
with open('./data/人物出现频次.csv', 'w') as f:
    for key in name_dict.keys():
        f.write("%s, %s\n" % (key, name_dict[key]))
"""

src_filename = './data/人物出现频次.csv'
src_file = open(src_filename, 'r')
line_list = src_file.readlines()  #返回列表，文件中的一行是一个元素
src_file.close()

wordfreq_list = []  #用于保存元组(人物姓名,出现次数)
girls = {"赵敏":0,"周芷若":0,"殷离":0,"小昭":0}

for line in line_list:
    line = line.strip()  #删除'\n'
    line_split = line.split(',') # 以逗号作为标志，把字符串切分成词，存在列表中
    wordfreq_list.append([line_split[0],line_split[1]])
    if(line_split[0] in girls.keys()):
        girls[line_split[0]] = line_split[1]
    
wordfreq_list.sort(key=lambda row: int(row[1]), reverse=True)

def cloud() -> WordCloud:

    cloud = WordCloud() # 初始化词云对象

    # 设置词云图
    cloud.add('', 
          wordfreq_list[0:80], #元组列表，词和词频
          shape='diamond', # 轮廓形状：'circle','cardioid','diamond',
                           # 'triangle-forward','triangle','pentagon','star'
          is_draw_out_of_bound=False, #允许词云超出画布边界
          word_size_range=[15, 100], #字体大小范围
          textstyle_opts=opts.TextStyleOpts(font_family="华文行楷"),
          #字体：例如，微软雅黑，宋体，华文行楷，Arial
          )

    # 设置标题
    cloud.set_global_opts(title_opts=opts.TitleOpts(title="倚天屠龙记人物词云"))
    return cloud

#比较四个女主角的次数
def bar() -> Bar:
    v1 = [girls['赵敏'],girls['周芷若'],girls['殷离'],girls['小昭']]
    #c.set_global_opts(title_opts=opts.TitleOpts(title="四位女主角提及次数"))
    
    c = (
        Bar()
        .add_xaxis(['赵敏','周芷若','殷离','小昭'])
        .add_yaxis("", v1)
        .set_global_opts(title_opts=opts.TitleOpts(title="四位女主角提及次数"))
        )
    return c

def page_default_layout():
    page = Page()
    page.add(
        bar(),
        cloud())
    page.render("./output/倚天屠龙记人物.html")

if __name__ == "__main__":
    page_default_layout()


