"""Show Information"""
import pygal
from xlrd import open_workbook
def function(): #hello mom 
    """_"""

    #open_worksheet
    book = open_workbook('D:/Thailand.xls')
    sheet = book.sheet_by_index(0)
    kill_honest = [sheet.cell(3, col_index).value for col_index in range(1, 6)]
    kill_bad = [sheet.cell(4, col_index).value for col_index in range(1, 6)]
    careless = [sheet.cell(5, col_index).value for col_index in range(1, 6)]
    try_to_kill = [sheet.cell(6, col_index).value for col_index in range(1, 6)]
    attrack = [sheet.cell(7, col_index).value for col_index in range(1, 6)]
    rape = [sheet.cell(8, col_index).value for col_index in range(1, 6)]

    #make
    line_chart = pygal.Bar()
    line_chart.title = sheet.cell(0, 0).value
    year = ["2554", "2555", "2556", "2557", "2558"]
    line_chart.x_labels = map(str, year)
    line_chart.add(sheet.cell(3, 0).value, kill_honest)
    line_chart.add(sheet.cell(4, 0).value, kill_bad)
    line_chart.add(sheet.cell(5, 0).value, careless)
    line_chart.add(sheet.cell(6, 0).value, try_to_kill)
    line_chart.add(sheet.cell(7, 0).value, attrack)
    line_chart.add(sheet.cell(8, 0).value, rape)
    line_chart.render_to_file('line_chart.svg')

function()