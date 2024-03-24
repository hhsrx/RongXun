from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Map,Geo
from pyecharts.globals import ChartType, SymbolType
import csv

geo = Geo()

geo.add_coordinate_json(json_file='./data/world_country.json')

geo.add_schema(maptype="world")

#读取文件，获得世界各国人均GDP
gdp_country_list = []

with open('./data/世界各国人均GDP.csv', mode ='r')as file:
  csvFile = csv.reader(file)
  for lines in csvFile:
      gdp_country_list.append(tuple(lines))

del gdp_country_list[0]

for c in gdp_country_list:
    try:
        (geo.add("",
           [c],
           type_=ChartType.EFFECT_SCATTER
    ))
    except:
        continue
    
        
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=80000),
                    title_opts=opts.TitleOpts(title="2022各国人均GDP（单位：美元）"))

geo.render('./output/gdp_per_capita.html')


c = (
    Map()
#    .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
    .add('', 
         [("甘肃省",44986),("黑龙江省",50883),("广西壮族自治区",52215),("贵州省",52348),("吉林省",55033),("河北省",56888),\
          ("西藏自治区",58269),("青海省",60776),("云南省",61736),("河南省",62071),("海南省",66845),("四川省",67785),\
              ("辽宁省",68515),("新疆维吾尔自治区",68526),("宁夏回族自治区",69925),("江西省",71009),("湖南省",73498),("山西省",73686),\
                  ("安徽省",73687),("陕西省",82885),("山东省",85973),("重庆市",90688),("湖北省",92170),("内蒙古自治区",96496),\
                      ("广东省",101796),("天津市",118801),("浙江省",118830),("福建省",126845),("江苏省",144475),\
                          ("上海市",179401),("北京市",190091)],
        "china")
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(min_=44986, max_=190091, is_piecewise=True), 
        title_opts=opts.TitleOpts(title="中国2022各省市人均GDP（单位：元）")
    )
    .render("./output/gdp_provinces.html")
)