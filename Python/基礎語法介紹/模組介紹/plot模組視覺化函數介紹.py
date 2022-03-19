# 數據視覺化 ========================================================

plt.hist(df['Fare']) #histogram是直方圖的意思
plt.show()

#資料的分布狀況
df.describe()

#變數間的關係，用圖表現
sns.pairplot(df[['Survived', 'Pclass', 'SibSp', 'Parch', 'Fare']])
#變數間相關係數
colormap = plt.cm.viridis
plt.figure(figsize=(14,12))
plt.title('Pearson Correlation of Features', y=1.05, size=15)
sns.heatmap(df[['Survived', 'Pclass', 'SibSp', 'Parch', 'Fare']].astype(float).corr(),linewidths=0.1,vmax=1.0, square=True, cmap=colormap, linecolor='white', annot=True)

# 使用plotly畫出可互動式的圖 ===========================================
import plotly
import plotly.plotly as py
from plotly.grid_objs import Grid, Column
from plotly.tools import FigureFactory as FF

import pandas as pd
import time

plotly.tools.set_credentials_file(username='event107421', api_key='8es5I8EnFjaGwGB4itHc')

url = 'https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv'
dataset = pd.read_csv(url)

table = FF.create_table(dataset.head(10))
py.plot(table, filename='animations-gapminder-data-preview')

# 用set去除重複，创建一个无順序不重复元素集
years_from_col = set(dataset['year'])
# 先將剛剛的dict格式傳盛list，再用sort對剛剛取出來的年份元素排序
years_ints = sorted(list(years_from_col))
# 把years_ints內的每個元素轉成字串
years = [str(year) for year in years_ints]
# 移除year內的1957這個類別
years.remove('1957')

# make list of continents
continents = []
for continent in dataset['continent']:
    if continent not in continents:
        continents.append(continent)

columns = []
# make grid
for year in years:
    for continent in continents:
        dataset_by_year = dataset[dataset['year'] == int(year)]
        dataset_by_year_and_cont = dataset_by_year[dataset_by_year['continent'] == continent]
        for col_name in dataset_by_year_and_cont:
            # each column name is unique
            column_name = '{year}_{continent}_{header}_gapminder_grid'.format(
                year=year, continent=continent, header=col_name
            )
            a_column = Column(list(dataset_by_year_and_cont[col_name]), column_name)
            columns.append(a_column)

# upload grid
grid = Grid(columns)
url = py.grid_ops.upload(grid, 'gapminder_grid'+str(time.time()), auto_open=False)
url

#
figure = {
    'data': [],
    'layout': {},
    'frames': [],
    'config': {'scrollzoom': True}
}

# fill in most of layout
figure['layout']['xaxis'] = {'range': [30, 85], 'title': 'Life Expectancy', 'gridcolor': '#FFFFFF'}
figure['layout']['yaxis'] = {'title': 'GDP per Capita', 'type': 'log', 'gridcolor': '#FFFFFF'}
figure['layout']['hovermode'] = 'closest'
figure['layout']['plot_bgcolor'] = 'rgb(223, 232, 243)'

sliders_dict = {
    'active': 0,
    'yanchor': 'top',
    'xanchor': 'left',
    'currentvalue': {
        'font': {'size': 20},
        'prefix': 'Year:',
        'visible': True,
        'xanchor': 'right'
    },
    'transition': {'duration': 300, 'easing': 'cubic-in-out'},
    'pad': {'b': 10, 't': 50},
    'len': 0.9,
    'x': 0.1,
    'y': 0,
    'steps': []
}

figure['layout']['updatemenus'] = [
    {
        'buttons': [
            {
                'args': [None, {'frame': {'duration': 500, 'redraw': False},
                         'fromcurrent': True, 'transition': {'duration': 300, 'easing': 'quadratic-in-out'}}],
                'label': 'Play',
                'method': 'animate'
            },
            {
                'args': [[None], {'frame': {'duration': 0, 'redraw': False}, 'mode': 'immediate',
                'transition': {'duration': 0}}],
                'label': 'Pause',
                'method': 'animate'
            }
        ],
        'direction': 'left',
        'pad': {'r': 10, 't': 87},
        'showactive': False,
        'type': 'buttons',
        'x': 0.1,
        'xanchor': 'right',
        'y': 0,
        'yanchor': 'top'
    }
]

custom_colors = {
    'Asia': 'rgb(171, 99, 250)',
    'Europe': 'rgb(230, 99, 250)',
    'Africa': 'rgb(99, 110, 250)',
    'Americas': 'rgb(25, 211, 243)',
    'Oceania': 'rgb(50, 170, 255)'
}


col_name_template = '{year}_{continent}_{header}_gapminder_grid'
year = 1952
for continent in continents:
    data_dict = {
        'xsrc': grid.get_column_reference(col_name_template.format(
            year=year, continent=continent, header='lifeExp'
        )),
        'ysrc': grid.get_column_reference(col_name_template.format(
            year=year, continent=continent, header='gdpPercap'
        )),
        'mode': 'markers',
        'textsrc': grid.get_column_reference(col_name_template.format(
            year=year, continent=continent, header='country'
        )),
        'marker': {
            'sizemode': 'area',
            'sizeref': 200000,
            'sizesrc': grid.get_column_reference(col_name_template.format(
                 year=year, continent=continent, header='pop'
            )),
            'color': custom_colors[continent]
        },
        'name': continent
    }
    figure['data'].append(data_dict)


for year in years:
    frame = {'data': [], 'name': str(year)}
    for continent in continents:
        data_dict = {
            'xsrc': grid.get_column_reference(col_name_template.format(
                year=year, continent=continent, header='lifeExp'
            )),
            'ysrc': grid.get_column_reference(col_name_template.format(
                year=year, continent=continent, header='gdpPercap'
            )),
            'mode': 'markers',
            'textsrc': grid.get_column_reference(col_name_template.format(
                year=year, continent=continent, header='country'
                )),
            'marker': {
                'sizemode': 'area',
                'sizeref': 200000,
                'sizesrc': grid.get_column_reference(col_name_template.format(
                    year=year, continent=continent, header='pop'
                )),
                'color': custom_colors[continent]
            },
            'name': continent
        }
        frame['data'].append(data_dict)

    figure['frames'].append(frame)
    slider_step = {'args': [
        [year],
        {'frame': {'duration': 300, 'redraw': False},
         'mode': 'immediate',
       'transition': {'duration': 300}}
     ],
     'label': year,
     'method': 'animate'}
    sliders_dict['steps'].append(slider_step)

figure['layout']['sliders'] = [sliders_dict]

py.create_animations(figure, 'gapminder_example'+str(time.time()))