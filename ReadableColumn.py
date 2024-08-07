# Common functions to return user-friendly readable column names

column_data = [
    ["ID", "Name"],
    ['statefips', 'countyfips', 'avghouseholdsize', 'avganncount', 'geography',
        'avgdeathsperyear', 'target_deathrate', 'incidencerate', 'medincome',
        'popest2015', 'povertypercent', 'studypercap', 'binnedinc',
        'medianage', 'medianagemale', 'medianagefemale', 'percentmarried',
        'pctnohs18_24', 'pcths18_24', 'pctsomecol18_24', 'pctbachdeg18_24',
        'pcths25_over', 'pctbachdeg25_over', 'pctemployed16_over', 'birthrate',
        'pctunemployed16_over', 'pctprivatecoverage', 'pctprivatecoveragealone',
        'pctempprivcoverage', 'pctpubliccoverage', 'pctpubliccoveragealone',
        'pctwhite', 'pctblack', 'pctasian', 'pctotherrace', 'pctmarriedhouseholds'],
    ['State ID', 'County ID', 'Average Household Size', 'Average Annual Count of Cancer Cases',
        'Location', 'Average Deaths per Year', 'Number of Deaths per 100K', 'incidencerate',
        'Median Household Income', 'Population Estimates 2015', 'Poverty %', 
        'Number of Clinical Trials per Capita', 'Binned Income', 'Median Age', 'Median Male Age',
        'Median Female Age', 'Married %', 'No High School 18-24 %', 'High School 18-24 %',
        'Some College %', 'Bachelor Degree 18-24 %', 'High School 25+ %', 'Bachelor Degree 25+ %',
        'Employed 16+ %', 'Birth Rate', 'Unemployed 16+ %', 'Pvt Health Ins %', 'Only Pvt Health Ins %',
        'Temp Pvt Health Ins %', 'Pub Health Ins %', 'Only Pub Health Ins %',
        'White %', 'Black %', 'Asian %', 'Other Race %', 'Married Households %']
]

""" Create a ReadableColumn class with methods"""

class ReadableColumn:

    def __init__(self):
        len(column_data[1])
        column_dict = []
        for i in range(len(column_data[1])):
            column_dict.append({
                column_data[0][0]: column_data[1][i],
                column_data[0][1]: column_data[2][i]
            })
        column_dict

    # This method gets the user friendly column name
    def get_readable_column(self, col):
        """Sets the balance for the for the account"""
        for i in range(len(column_data[1])):
            if column_data[1][i] == col:
                return column_data[2][i]
        return "Column" + col + "not found"
