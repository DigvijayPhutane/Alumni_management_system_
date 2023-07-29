from alumni_info import Alumni
from alumni_services_impl import Alumni_Services_Impl

services = Alumni_Services_Impl()
while True:
    print('''
                1. Add Alumni Details.
                2. Total List Of Alumni.
                3. Delete Alumni Details.
                4. Search Alumni. 
                5. List according to Year of graduation.  
                6. Export Data Into Excel.
                7. Import Excel Into DataBase.
    ''')

    choice = int(input('Enter Your Choice : '))
    if choice == 1 : #add alumni
        try:
            almid = int(input('Enter Alumni ID: '))
            alnam = input('Enter Alumni Name: ')
            aldep = input('Enter Alumni Department: ')
            alcom = input('Enter Alumni Company: ')
            ygrad = int(input('Enter Year Of Graduation: '))
            alphone = int(input('Enter Alumni Phone Number: '))
        except ValueError as v:
            print('Invalid Input...Re-enter Values..!')
        else:
            a1 = Alumni(alid=almid,alnm=alnam,aldepart=aldep,alcompany=alcom,yearg=ygrad,alnum=alphone)
            services.add_alumni(a1)

    elif choice == 2: #list alumni
        alumni_list = services.list_alumni()
        print(alumni_list)

    elif choice == 3: #delete alumni
        alumnid = int(input("Enter Alumni ID: "))
        services.delete_alumni(alumnid)
    elif choice == 4: #search alumni
        print(
            '''
            1.ID    2.NAME    3.DEPARTMENT   4.COMPANY   5.YEAR_OF_GRADUATION
            '''
        )
        ch = int(input('Enter Your Criteria For Search : '))
        if ch == 1:
            val = int(input('Enter Alumni ID For Search: '))
            print(services.search_alumni('ID',val))
        elif ch ==2:
            val = input('Enter Alumni Name: ')
            print(services.search_alumni('NAME',val))
        elif ch ==3:
            val = input('Enter Alumni Department: ')
            print(services.search_alumni('DEPARTMENT',val))
        elif ch ==4:
            val = input('Enter Alumni Company: ')
            print(services.search_alumni('COMPANY',val))
        elif ch ==5:
            val = int(input('Enter Alumni Year Of Graduation: '))
            print(services.search_alumni('YEAR_OF_GRADUATION',val))
        else:
            print('Invalid Choice...!')


    elif choice == 5: #yearin range
        from_year = int(input("Enter From Year: "))
        to_year = int(input("Enter To Year: "))
        if from_year>to_year:
            print('Invalid Input...!')
        else:
            al_list = services.alumni_of_year_in_range(from_year,to_year)
            print(al_list)

    elif choice == 6: #Export into Excel
        excel = services.export_data_excel()

    elif choice == 7:
        excel_import = services.import_excel_data()
        print("The new list is : ")
        excel_list = services.list_alumni()
        print(excel_list)

    else:
        print('Invalid Choice...')

    choice = input('Do you want to continue ? : yes/no :')
    if choice.lower() in ['n', 'no']:
        break
print('Program Completed...Thank you!')