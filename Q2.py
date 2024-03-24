from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Bar, Page, Pie, Timeline

#资料来源：https://www.olympedia.org/statistics/medal/country
gold =[[32,36,28,9,11],
       [48,36,24,19,7],
       [39,48,18,29,11],
       [26,46,19,27,10],
       [38,39,20,22,10]]

silver = [
    [17,39,26,9,9],
    [22,39,13,13,16],
    [31,26,21,18,11],
    [18,37,17,23,18],
    [32,41,28,20,12]]

bronze = [
    [17,39,26,12,13],
    [30,37,23,19,20],
    [22,30,26,18,13],
    [26,38,20,17,14],
    [19,33,23,22,11]]

city = ["悉尼","北京","伦敦","里约","东京"]

tl = Timeline()
for i in range(5):
    bar = (
        Bar()
        .add_xaxis(['中国','美国','俄罗斯','英国','法国'])
        .add_yaxis("金牌", gold[i], color="#D4AF37")
        .add_yaxis("银牌", silver[i], color="#C0C0C0")
        .add_yaxis("铜牌", bronze[i], color="#CD7F32")
        .set_global_opts(title_opts=opts.TitleOpts(title = "中、美、俄、英、法夏季奥运会奖牌数"))
    )
    tl.add(bar, "{}年{}".format(2004+i*4, city[i]))

tl.render('./output/olympicmedals_bar.html')

