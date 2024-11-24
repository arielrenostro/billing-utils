
import csv
from datetime import datetime
from prettytable import PrettyTable
import re
import sys
from consts import nubank_desc_col_idx, nubank_date_col_idx, nubank_value_col_idx,\
        nubank_categories_by_place, has_installment_regex, first_installment_regex, first_installment,\
        categories_to_ignore, refund_regex, nubank_categories_translate
from validations import validate_header, validate_line


def has_installment(description):
    return re.match(has_installment_regex, description)


def is_first_installment(description):
    return re.match(first_installment_regex, description)


def get_category(line):
    description = line[nubank_desc_col_idx]
    if not has_installment(description):
        category = nubank_categories_by_place.get(description, None)
        if category is not None:
            return category
        for place in nubank_categories_by_place.keys():
            if place.startswith('regexp:') and re.match(place[7:], description):
                return nubank_categories_by_place.get(place, 'Desconhecido')
        return 'Desconhecido'
    
    if is_first_installment(description):
        for place in nubank_categories_by_place.keys():
            regexp = None
            if place.startswith('regexp:'):
                regexp = f'{place[7:]} - {first_installment}'
            else:
                regexp = f'{place} - {first_installment}'
            if re.match(regexp, description):
                category = nubank_categories_by_place.get(place, None)
                if category is not None:
                    return category
        return 'Desconhecido'

    return 'Parcela'


def main():
    report_file_name = sys.argv[1]
    if not report_file_name or len(report_file_name) == 0:
        print('Usage: main.py nubank.csv')
        sys.exit(1)

    lines = []

    with open(report_file_name, 'r') as f:
        idx = 0
        reader = csv.reader(f)
        for line in reader:
            if idx == 0:
                validate_header(line)
            else:
                validate_line(idx, line)
                lines.append(line)
            idx += 1

    # lines_without_refund = [*lines]
    # for line in lines:
    #     groups = re.findall(refund_regex, line[nubank_desc_col_idx])
    #     if len(groups) == 1:
    #         for l_aux in lines:
    #             if float(l_aux[nubank_value_col_idx]) == (float(line[nubank_value_col_idx]) * -1) and\
    #                  groups[0] in l_aux[nubank_desc_col_idx]:
    #                 lines_without_refund.remove(l_aux)
    #                 lines_without_refund.remove(line)
    #                 break

    # lines = lines_without_refund

    for line in lines:
        description = line[nubank_desc_col_idx]
        if description in nubank_categories_translate:
            line[nubank_desc_col_idx] = nubank_categories_translate[description]

    lines_by_category = {}
    for line in lines:
        category = get_category(line)
        items = lines_by_category.get(category, [])
        items.append(line)
        lines_by_category[category] = items
    
    table = PrettyTable()
    table.field_names = ['Date', 'Description', 'Value', 'Category']
    table.align['Description'] = 'l'
    table.align['Value'] = 'r'
    table.align['Category'] = 'l'

    for category, items in lines_by_category.items():
        if category in categories_to_ignore:
            continue
        items.sort(key=lambda x: x[nubank_date_col_idx])

        for item in items:
            table.add_row([
                datetime.strptime(item[nubank_date_col_idx], "%Y-%m-%d").strftime("%d/%m/%Y"),
                item[nubank_desc_col_idx],
                item[nubank_value_col_idx],
                category,
            ])

    print(table.get_string())


if __name__ == '__main__':
    main()
