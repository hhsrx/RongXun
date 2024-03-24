from pyecharts.faker import Faker
from pyecharts import options as opts
from pyecharts.charts import Geo
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
    Geo()
    .add_schema(maptype="china")
#    .add("geo", [list(z) for z in zip(Faker.provinces, Faker.values())])
    .add('', 
         [("北京", 190091), ("上海", 179401), 
          ("江苏", 144475), ("福建", 126845), 
          ("浙江", 118830)],
        #省市标记参数是由元组项组成的列表，图上标记的颜色和数值有关
        )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    .set_global_opts(
        visualmap_opts=opts.VisualMapOpts(min_=100000, max_=200000), 
        title_opts=opts.TitleOpts(title="中国2022各省市人均GDP前五（单位：元）")
    )
    .render("./output/gdp_provinces.html")
)