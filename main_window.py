from PySide.QtGui import *
from alg_stats_table_model import AlgStatsTableModel
import urllib2
from json_parser import json_parser


header = ['Algorithm Name', 'Count', 'Run as child', 'Mantid Version']


class MainWindow(QWidget):

    def __init__(self, *args):
        QWidget.__init__(self, *args)
        # setGeometry(x_pos, y_pos, width, height)
        self.setGeometry(300, 200, 800, 600)
        self.setWindowTitle("Click on column title to sort")
        data_list = self.get_data()
        table_model = AlgStatsTableModel(self, data_list, header)
        table_view = QTableView()
        table_view.setModel(table_model)
        # set font
        font = QFont("Courier New", 11)
        table_view.setFont(font)
        # set column width to fit contents (set font first!)
        table_view.resizeColumnsToContents()
        # enable sorting
        table_view.setSortingEnabled(True)
        layout = QVBoxLayout(self)
        layout.addWidget(table_view)
        self.setLayout(layout)

    def get_data(self):
        resp = urllib2.urlopen("http://reports.mantidproject.org/api/feature?format=json")
        alg_records = json_parser(resp.read())
        table_data = []
        for record in alg_records:
            table_data.append(record.get_data_list())
        return table_data
