"""Show Information"""
import pygal #create graph
from xlrd import open_workbook #import file from excel
from pygal.style import BlueStyle #style of graph(color)
def function():
    """Percent Average"""

    #open_worksheet
    book = open_workbook('D:/Book1.xlsx') #openfile in ---> (name of file)
    sheet = book.sheet_by_index(2) #sheet cell
    kill_honest = [sheet.cell(3, col_index).value for col_index in range(7, 8)] #sheet.cell(row, col_index) ,,,, range(column)
    kill_bad = [sheet.cell(4, col_index).value for col_index in range(7, 8)]
    careless = [sheet.cell(5, col_index).value for col_index in range(7, 8)]
    try_to_kill = [sheet.cell(6, col_index).value for col_index in range(7, 8)]
    attrack = [sheet.cell(7, col_index).value for col_index in range(7, 8)]
    rape = [sheet.cell(8, col_index).value for col_index in range(7, 8)]

    #pie_chart
    pie_chart = pygal.Pie(inner_radius=.4, fill=True, interpolate='cubic', style=BlueStyle)
    pie_chart.title = sheet.cell(0, 0).value
    pie_chart.add(sheet.cell(3, 0).value, sheet.cell(3, 7).value)
    pie_chart.add(sheet.cell(4, 0).value, sheet.cell(4, 7).value)
    pie_chart.add(sheet.cell(5, 0).value, sheet.cell(5, 7).value)
    pie_chart.add(sheet.cell(6, 0).value, sheet.cell(6, 7).value)
    pie_chart.add(sheet.cell(7, 0).value, sheet.cell(7, 7).value)
    pie_chart.add(sheet.cell(8, 0).value, sheet.cell(8, 7).value)
    pie_chart.render_to_file('AverageNortheasten.svg')

function()