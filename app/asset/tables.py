from flask_table import Table, Col, DatetimeCol

class Transactions_Table(Table):
    classes = ['table', 'table-bordered', 'table-striped', 'table-hover']
    id = Col('Id')
    type = Col('Type', td_html_attrs={'type':'button', 'src':'static/img/harddisk.svg'})
    asset_name = Col('Asset Name')
    person_name = Col('Person')
    start_time = DatetimeCol('Start Time', datetime_format='dd-MM-yyyy HH:mm')
    end_time = DatetimeCol('End Time', datetime_format='dd-MM-yyyy HH:mm')
    status = Col('Status')


