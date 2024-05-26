# Progressive taxation system for India and US

def india(income):
    update = income

#111111111111111111111111
    if update > 300000:
        br0 = 300000 / 100 * 0
    else:
        br0 = update / 100 * 0
    if update-300000<0:
        update = 0
    else:
        update = update - 300000
    print(br0, update)
#2222222222222222222222222
    if update > 300000:
        br1 = 300000 / 100 * 5
    else:
        br1 = update / 100 * 5
    if update - 300000 < 0:
        update = 0
    else:
        update = update - 300000
    print(br1, update)
#3333333333333333333333333333
    if update > 300000:
        br2 = 300000 / 100 * 10
    else:
        br2 = update / 100 * 10
    if update - 300000 < 0:
        update = 0
    else:
        update = update - 300000
    print(br2, update)
#44444444444444444444444444444444444
    if update > 300000:
        br3 = 300000 / 100 * 15
    else:
        br3 = update / 100 * 15
    if update - 300000 < 0:
        update = 0
    else:
        update = update - 300000
    print(br3, update)
#555555555555555555555555555555555555
    if update > 300000:
        br4 = 300000 / 100 * 20
    else:
        br4 = update / 100 * 20
    if update - 300000 < 0:
        update = 0
    else:
        update = update - 300000
    print(br4, update)
#666666666666666666666666666666666666
    br5 = update / 100 * 30


    print(br5, update)
#--------------------------------------
    tax = br0 + br1 + br2 + br3 + br4 + br5
    if tax < 0:
        tax = 0
   # print(br0, br1, br2, br3, br4, br5)
    return tax


def usa(income):

    lmt0 = 11000-0      #10
    lmt1 = 44725-11001  #12
    lmt2 = 95375-44726  #22
    lmt3 = 182100-95376 #24 =
    lmt4 = 231250-182101#32 =
    lmt5 = 578125-231251#35 =   121405.9
    lmt6 = 578126-0     #37 =   8093.38

    update = income
    if update >= lmt0:
        br0 = lmt0/100*10     #10%
        update = income - lmt0
    else :
        br0 = update/100*10
        update = 0

    print(update)

    if update >= lmt1:
        br1 = lmt1/100*12      #12%
        update = update - lmt1
    else :
        br1 = update/100*12
        update = 0

    print(update)


    if update >= lmt2:
        br2 = lmt2 / 100 * 22  # 22%
        update = update - lmt2
    else:
        br2 = update / 100 * 22
        update = 0

    print(update)


    if update >= lmt3:
        br3 = lmt3/100*24      #24%
        update = update - lmt3
    else :
        br3 = update/100*24
        update = 0

    print(update)


    if update >= lmt4:
        br4 = lmt4/100*32      #32%
        update = update - lmt4
    else :
        br4 = update/100*32
        update = 0

    print(update)


    if update >= lmt5:
        br5 = lmt5/100*35      #35%
        update = update - lmt5
    else :
        br5 = update/100*35
        update = 0

    print(update)


    br6 = (income - lmt6)/100*37      #37%

    print(update)


    tax = br0 + br1 + br2 + br3 + br4 + br5 + br6
    if tax < 0:
        tax = 0
    print(br0, "\n" , br1, "\n" , br2, "\n" , br3, "\n" , br4, "\n" , br5, "\n" , br6)
    return tax







print("\n"
      "***************|   Hello    World    |*******************\n"
      "***************| TAXATION    SYSTEM  |*****************\n"
      "***************|Enter \"1\" for India|**************\n")
      #"***************|Enter \"2\" for USA  |**************")
choice = int(input("Enter choice:             "))
if choice == 1:
    income = float(input("Enter your annual income: "))
    print("The tax to be paid is:   INR", india(income),
          "\nThe amount you keep is:  INR", income-india(income))

#elif choice == 2:
#    income = float(input("Enter your annual income: "))
#    print("The tax to be paid is:   USD", usa(income),
#          "\nThe amount you keep is:  USD", income-usa(income))
else:
    print("WRONG CHOICE")


