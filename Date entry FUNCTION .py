#  Date entry method revolution
#  **************************************

#  Latest is the first

# **************************************************
# Function inside function removed and straight running
# Bug resolved : Now Day and month can not be 00
# Complete leap year conditions included date will never be wrong
# *************************************************


def date_entry(date_to_be_entered):  # date entry function
    loop_exit_value = "value error"  # While loop should continue "loop exit value" is equal to "value error"
    while loop_exit_value == "value error":  # While loop should continue "loop exit value" is equal to "value error"
        try:
            date_format = input(f'Enter {date_to_be_entered} in "dd/mm/yyyy" format: ')
            [day, month, year] = date_format.split("/")
            day = int(day)
            month = int(month)
            year = int(year)
            loop_exit_value = "perfect"

            while year > 2099 or year < 1950:
                print('Entered Year is too far from the current period !!!!')
                year = int(input('Enter any year in between 1950 and 2099: '))
            while month > 12 or month <= 0:  # There are only maximum of 12 months
                print('Invalid month entry !!! ')  # so if the user enter something greater than 12
                month = int(input('enter the month: '))  # it should be shown invalid
            # **********************************
            # Finding max number of days in a month
            # **********************************
            # 28 days for FEB in normal year and 29 days in leap year FEB (FEB 02)
            # 30 days months are (APRIL 04), (JUNE 06), (SEPTEMBER 09), (NOVEMBER 11)
            # 31 days months are (JAN 01), (MARCH 03), (MAY 05), (JULY 07), (AUGUST 08), (OCTOBER 10), (DECEMBER 12)
            # **********************************
            # Leap year condition below
            # **********************************
            # Every year that is exactly divisible by four is a leap year, except for years that are exactly
            # divisible by 100, but these centurial years are leap years if they are exactly divisible by 400.
            # For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are

            if month == 2:
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    max_num_of_days = 29
                else:
                    max_num_of_days = 28

            elif month in [4, 6, 9, 11]:
                max_num_of_days = 30
            else:
                max_num_of_days = 31
            # ******************************************
            # Finding max number of days in a month FINISHED
            # ******************************************

            while day > max_num_of_days or day <= 0:
                print('Invalid day entry for the month !!!')
                day = int(input('Enter the day: '))
            date_to_be_entered = f'{day}/{month}/{year}'
            show_months = {1: "January",
                           2: "February",
                           3: "March",
                           4: "April",
                           5: "May",
                           6: "June",
                           7: "july",
                           8: "August",
                           9: "September",
                           10: "October",
                           11: "November",
                           12: "December"}
            print(f"{day}-{show_months.get(month)}-{year}")

        except ValueError:
            print("invalid date format..enter again")
            loop_exit_value = "value error"
    return date_to_be_entered

date_entry("date")

# **************************************************
# Function inside function removed and straight running
# Bug resolved : Now Day and month can not be 00
# *************************************************

#
# def date_entry(date_to_be_entered):  # date entry function
#     loop_exit_value = "value error"  # While loop should continue "loop exit value" is equal to "value error"
#     while loop_exit_value == "value error":  # While loop should continue "loop exit value" is equal to "value error"
#         try:
#             date_format = input(f'Enter {date_to_be_entered} in "dd/mm/yyyy" format: ')
#             [day, month, year] = date_format.split("/")
#             day = int(day)
#             month = int(month)
#             year = int(year)
#             loop_exit_value = "perfect"
#
#             while year > 2099 or year < 1950:
#                 print('Entered Year is too far away from the current period !!!!!')
#                 year = int(input('Enter any year in between 1950 and 2050: '))
#             while month > 12 or month == 0 :  # As the case of date there is only maximum of 12 months
#                 print('Invalid month entry !!! ')  # so if the user enter something greater than 12
#                 month = int(input('enter the month: '))  # it should be shown invalid
#             # **********************************
#             # Finding max number of days in a month
#             # **********************************
#             # 28 days for FEB in normal year and 29 days in leap year FEB (FEB 02)
#             # 30 days months are (APRIL 04), (JUNE 06), (SEPTEMBER 09), (NOVEMBER 11)
#             # 31 days months are (JAN 01), (MARCH 03), (MAY 05), (JULY 07), (AUGUST 08), (OCTOBER 10), (DECEMBER 12)
#             if month == 2:
#                 if year % 4 != 0:
#                     max_num_of_days = 28
#                 else:
#                     max_num_of_days = 29  # For leap year adjustment
#             elif month in [4, 6, 9, 11]:
#                 max_num_of_days = 30
#             else:
#                 max_num_of_days = 31
#             # ******************************************
#             # Finding max number of days in a month FINISHED
#             # ******************************************
#
#             while day > max_num_of_days or day == 0:
#                 print('Invalid day entry, Exceeds maximum number of days in the given month')
#                 day = int(input('enter the day: '))
#             date_to_be_entered = f'{day}/{month}/{year}'
#
#         except ValueError:
#             print("invalid date format..enter again")
#             loop_exit_value = "value error"
#     return date_to_be_entered
#
#
# date = date_entry("whatever date")
# print(date)
#
# # **************************************************
# # Function inside function removed and straight running
# # Bug found.. program finishes even when day and month are "00"
# # *************************************************
#
#
# def date_entry(date_to_be_entered):  # date entry function
#     loop_exit_value = "value error"  # While loop should continue "loop exit value" is equal to "value error"
#     while loop_exit_value == "value error":  # While loop should continue "loop exit value" is equal to "value error"
#         try:
#             date_format = input(f'Enter {date_to_be_entered} in "dd/mm/yyyy" format: ')
#             [day, month, year] = date_format.split("/")
#             day = int(day)
#             month = int(month)
#             year = int(year)
#             loop_exit_value = "perfect"
#
#             while year > 2050 or year < 1950:
#                 print('Year is too far away from the current era')
#                 year = int(input('enter the year in between 1950 and 2050: '))
#             while month > 12:  # As the case of date there is only maximum of 12 months
#                 print('Invalid month entry')  # so if the user enter something greater than 12
#                 month = int(input('enter the month: '))  # it should be shown invalid
#             # **********************************
#             # Finding max number of days in a month
#             # **********************************
#             # 28 days for FEB in normal year and 29 days in leap year FEB (FEB 02)
#             # 30 days months are (APRIL 04), (JUNE 06), (SEPTEMBER 09), (NOVEMBER 11)
#             # 31 days months are (JAN 01), (MARCH 03), (MAY 05), (JULY 07), (AUGUST 08), (OCTOBER 10), (DECEMBER 12)
#             if month == 2:
#                 if year % 4 != 0:
#                     max_num_of_days = 28
#                 else:
#                     max_num_of_days = 29  # For leap year adjustment
#             elif month in [4, 6, 9, 11]:
#                 max_num_of_days = 30
#             else:
#                 max_num_of_days = 31
#             # ******************************************
#             # Finding max number of days in a month FINISHED
#             # ******************************************
#
#             while day > max_num_of_days:
#                 print('Invalid day entry, Exceeds maximum number of days in the given month')
#                 day = int(input('enter the day: '))
#             date_to_be_entered = f'{day}/{month}/{year}'
#
#         except ValueError:
#             print("invalid date format..enter again")
#             loop_exit_value = "value error"
#     return date_to_be_entered
#
# # *********************************
# # Function inside function method
# # *********************************
#
#
# def date_entry(date_to_be_entered):  # date entry function
#     def day_error_check(day_to_be_checked, max_num_of_days): # defined this function inside another defined function# defined this function inside another defined function
#         while day_to_be_checked > max_num_of_days:
#             # Maximum number of days in any month is less than 31.
#             # So while loop will continue if user enters "day" greater than
#             print('Invalid day entry, Exceeds maximum number of days in the given month')
#             day_to_be_checked = int(input('enter the day: '))
#         return day_to_be_checked
#     loop_exit_value = "value error"  # While loop should continue "loop exit value" is equal to "value error"
#     while loop_exit_value == "value error":  # While loop should continue "loop exit value" is equal to "value error"
#         try:
#             date_format = input(f'Enter {date_to_be_entered} in "dd/mm/yyyy" format: ')
#             [day, month, year] = date_format.split("/")
#             day = int(day)
#             month = int(month)
#             year = int(year)
#             # print(day)
#             # print(month)
#             # print(year)
#             loop_exit_value = "perfect"
#
#             while year > 2050 or year < 1950:
#                 print('Year is too far away from the current era')
#                 year = int(input('enter the year in between 1950 and 2050: '))
#             while month > 12:  # As the case of date there is only maximum of 12 months
#                 print('Invalid month entry')  # so if the user enter something greater than 12
#                 month = int(input('enter the month: '))  # it should be shown invalid
#             # 28/29 bays FEB 02
#             # 30 days months are APRIL 04, JUNE 06, SEPTEMBER 09, NOVEMBER 11
#             # 31 days months are JAN 01, MARCH 03, MAY 05, JULY 07, AUGUST 08, OCTOBER 10, DECEMBER 12
#             if month == 2:
#                 day = day_error_check(day,28)
#             elif month in [4,6,9,11]:
#                 day = day_error_check(day, 30)
#             else:
#                 day = day_error_check(day, 31)
#
#             date_to_be_entered = f'{day}/{month}/{year}'
#
#         except ValueError:
#             print("invalid date format..enter again")
#             loop_exit_value = "value error"
#     return date_to_be_entered
#
#
# date = date_entry("whatever date")
# print(date)
#
#
# # *********************************
# # Old method,
# # Max no: of days in a month error check is not available in this method
# # *********************************
#
# def date_entry(date_to_be_entered):  # date entry function
#     loop_exit_value = "value error"
#     while loop_exit_value == "value error":
#         try:
#             date_format = input(f'Enter {date_to_be_entered} in "dd/mm/yyyy" format ')
#             [day, month, year] = date_format.split("/")
#             day = int(day)
#             month = int(month)
#             year = int(year)
#             loop_exit_value = "perfect"  # To change the value "loop_exit_value" to get out of the while loop (loop_exit_value=ValueError)
#             while day > 31:  # Maximum number of days in any month is less than 31
#                 # print('Invalid day entry')  # So if the user enters something greater than 31, it should be stated as invalid
#                 day = int(input('enter the day '))
#             while month > 12:  # As the case of date_x there is only maximum of 12 months
#                 print('Invalid month entry')  # so if the user enter something greater than 12
#                 month = int(input('enter the month '))  # it should be shown invalid
#             while year > 2050 or year < 1950:
#                 print('Year is too far away from the current era')
#                 year = int(input('enter the year in between 1950 and 2050 '))
#             print(' ')
#             date_to_be_entered = f'{day}/{month}/{year}'
#             # print(f'Date is {day}/{month}/{year}')
#         except ValueError:
#             print("invalid date_x format..enter again")
#             loop_exit_value = "value error"
#     return date_to_be_entered
#
#
# date_x = date_entry("Whatever date you needed")  # invoking date function
# print(date_x)
#
# # *********************************
# # Old method, date format in ddmmyyy : no "/" in between
# # Max no: of days in a month error check is not available in this method
# # *********************************
#
#
# def date_entry_another_method(date_to_be_entered):  # date entry function
#     loop_exit_value = "value error"  # While loop should continue "loop exit value" is equal to "value error"
#     while loop_exit_value == "value error":  # While loop should continue "loop exit value" is equal to "value error"
#         try:
#             date_format = input(f'Enter {date_to_be_entered} in "ddmmyyyy" format: ')
#             [day, month, year] = [date_format[0:2], date_format[2:4], date_format[4:8]]
#             day = int(day)
#             month = int(month)
#             year = int(year)
#             # print(day)
#             # print(month)
#             # print(year)
#             loop_exit_value = "perfect"
#             while day > 31:  # Maximum number of days in any month is less than 31. So while loop will continue if user
#                 # enter "day" greater than 31
#                 print('Invalid day entry')
#                 day = int(input('enter the day: '))
#             while month > 12:  # As the case of date there is only maximum of 12 months
#                 print('Invalid month entry')  # so if the user enter something greater than 12
#                 month = int(input('enter the month: '))  # it should be shown invalid
#             while year > 2050 or year < 1950:
#                 print('Year is too far away from the current era')
#                 year = int(input('enter the year in between 1950 and 2050: '))
#             date_to_be_entered = f'{day}/{month}/{year}'
#         except ValueError:
#             print("invalid date format..enter again")
#             loop_exit_value = "value error"
#     return date_to_be_entered
#
#
# date = date_entry_another_method("whatever date")
# print(date)
#
# def date_entry():
#   day = 0
#  while day == 0:
#     try:
#        day = int(input('enter the day '))  # To get the date input from the user
#       while day > 31:  # Maximum number of days in any month is less than 31
#          print(
#             'Invalid day entry')  # So if the user enters something greater than 31, it should be stated as
# invalid
#        day = int(input('enter the day '))
# except ValueError:
#   print('invalid day entry')  # If the user enter something other than number an error will come.

# month = 0
# while month == 0:
#  try:
#     month = int(input('enter the month '))  # show the input prompter again
#    while month > 12:  # As the case of date there is only maximum of 12 months
#       print('Invalid month entry')  # so if the user enter something greater than 12
#      month = int(input('enter the month '))  # it should be shown invalid
# except ValueError:
#   print('invalid month entry')
# year = 0
# while year == 0:
#   try:
#      year = int(input('enter the year '))
#     while year > 2050 or year < 1950:
#        print('Year is too far away from the current era')
#       year = int(input('enter the year in between 1950 and 2050 '))
# except ValueError:
#   print('invalid year entry')
# print(' ')
# print(f'Date is {day}/{month}/{year}')
# date_entry()
