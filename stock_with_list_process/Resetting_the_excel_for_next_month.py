from a_Xcel_functions import *
from Stock_functions import float_entry
import Xcel_files

# ********************** Add your excel file path here ********************** #
Common_excel_file_name = f"{Xcel_files.file_path}{Xcel_files.file1_name}"
Jasi_excel_file_name = f"{Xcel_files.file_path}{Xcel_files.file2_name}"
sheet_name_for_common_and_jasi = "P&L writing"
# ********************** Add your excel file path here ********************** #
# For reading & writing intraday list from & to excel file
intraday_list_row_start = 11
intraday_list_row_ending = 67
intraday_list_column_start = 2
intraday_list_column_ending = 6
intraday_blank_list_format = ['', '', '', '', '']

# For reading & writing delivery buy list from excel file
delivery_list_row_start = 73
delivery_list_row_ending = 198
delivery_list_column_start = 2
delivery_list_column_ending = 8
delivery_blank_list_format = [None, None, None, None, None, None, None]


def to_write_current_month_profit_for_recording(excel_filename):
    current_month_pnl = float_entry('Prev month P&L to be added : ')
    print("Processing.....")
    row_number_to_write = iteration_to_find_a_filled_till(excel_filename, sheet_name_for_common_and_jasi, 18, 66,
                                                          16, 16, [None])
    # print(excel_filename, sheet_name_for_common_and_jasi, row_number_to_write, 16,
    #                              current_month_pnl)
    over_writing_a_cell_to_excel(excel_filename, sheet_name_for_common_and_jasi, row_number_to_write, 16,
                                 current_month_pnl)
    # input(f'Copy "{month} {year} P&L" and paste in the excel file and press enter')
    # over_writing_a_cell_to_excel(excel_filename, sheet_name_for_common_and_jasi, row_number_to_write, 15,
    #                              f"{Month} {Year} P&L")


def intraday_trade_resetting(excel_filename):
    list_for_resetting = []
    for y in range(56):
        list_for_resetting.append(intraday_blank_list_format)
    over_write_list_of_list_to_excel(excel_filename, sheet_name_for_common_and_jasi, intraday_list_row_start,
                                     intraday_list_column_start, list_for_resetting)


def delivery_trade_resetting(excel_filename):
    delivery_list_of_list = reading_list_from_excel(excel_filename, sheet_name_for_common_and_jasi,
                                                    delivery_list_row_start, delivery_list_row_ending,
                                                    delivery_list_column_start, delivery_list_column_ending)
    x = 0
    new_list_of_list = []
    for individual_list in delivery_list_of_list:
        if individual_list[0:4] != [None, None, None] and individual_list[4:7] == [None, None, None]:
            new_list_of_list.append(individual_list)
        else:
            x += 1
    for y in range(x):
        new_list_of_list.append([None, None, None, None, None, None, None])
    delivery_list_of_list = new_list_of_list
    over_write_list_of_list_to_excel(excel_filename, sheet_name_for_common_and_jasi,
                                     delivery_list_row_start, intraday_list_column_start, delivery_list_of_list)


def to_reset_excel_file():
    file_name = Common_excel_file_name
    if True:
        if file_name != Jasi_excel_file_name and file_name == Common_excel_file_name:
            to_write_current_month_profit_for_recording(file_name)
            intraday_trade_resetting(file_name)
            delivery_trade_resetting(file_name)
            print(f'"{Xcel_files.file1_name}" is reset successfully!!')
            if file_name == Jasi_excel_file_name:
                pass
            else:
                to_jasi = input("\nTo reset Jasi's file also: press 'y':")
                if to_jasi == "y":
                    file_name = Jasi_excel_file_name
                    to_write_current_month_profit_for_recording(file_name)
                    intraday_trade_resetting(file_name)
                    delivery_trade_resetting(file_name)
                    print(f'"{Xcel_files.file2_name}" is reset successfully!!\n')

# ******************************************************************************************************
# ************************************** END OF CODE ***************************************************
# ******************************************************************************************************

# ******************************************************************************************************
# *********************************TEST CODES BELOW  ***************************************************
# ******************************************************************************************************


# to_reset_excel_file()

# intraday_trade_resetting(f"{Xcel_files.file_path}{Xcel_files.file1_name}")
# print('first done')
# delivery_trade_resetting(f"{Xcel_files.file_path}{Xcel_files.file1_name}")
# print('second done')

# to_write_current_month_profit_for_recording(f"{Xcel_files.file_path}{Xcel_files.file1_name}")
