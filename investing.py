import plotly.graph_objects as go
import pandas
import variables

def get_months():
    i = 0
    months = []

    while i < variables.months:
        months.append(i)
        i+=1

    return months

def plot_graph(months, dataframe_no_rent, dataframe_rent):
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=months, y=dataframe_no_rent.Amount,
                    mode='lines+markers',
                    name='Amount No Rent'))

    fig.add_trace(go.Scatter(x=months, y=dataframe_no_rent.Net_Worth,
                    mode='lines+markers',
                    name='Net Worth No Rent'))

    fig.add_trace(go.Scatter(x=months, y=dataframe_rent.CSN_Debt,
                    mode='lines+markers',
                    name='CSN Debt'))
    
    fig.add_trace(go.Scatter(x=months, y=dataframe_rent.Amount,
                    mode='lines+markers',
                    name='Amount Rent'))

    fig.add_trace(go.Scatter(x=months, y=dataframe_rent.Net_Worth,
                    mode='lines+markers',
                    name='Net Worth Rent'))

    fig.show()

def growth_with_rent():
    amount = variables.start_amount
    csn_debt = variables.csn_debt
    i = 1
    
    amount_list = []
    net_worth = []
    csn_debt_list = []

    while i < variables.months:

        amount *= variables.roi

        if i == 8 or i == 20:
            amount += variables.csn_8
            csn_debt += variables.csn_8
        elif i == 9 or i == 21:
            amount += variables.csn_normal
            csn_debt += variables.csn_normal
        elif i == 10 or i == 22:
            amount += variables.csn_normal
            csn_debt += variables.csn_normal
        elif i == 11 or i == 23:
            amount += variables.csn_normal
            csn_debt += variables.csn_normal
        elif i == 12 or i == 24:
            amount += variables.csn_12
            csn_debt += variables.csn_12
        elif i == 1 or i == 13:
            amount += variables.csn_1
            csn_debt += variables.csn_1
        elif i == 2 or i == 14:
            amount += variables.csn_normal
            csn_debt += variables.csn_normal
        elif i == 3 or i == 15:
            amount += variables.csn_normal
            csn_debt += variables.csn_normal
        elif i == 4 or i == 16:
            amount += variables.csn_normal
            csn_debt += variables.csn_normal
        elif i == 5 or i == 17:
            amount += variables.csn_5
            csn_debt += variables.csn_5

        if i % 12 == 0:
            csn_debt *= variables.csn_intrest
            amount *= 1 - variables.tax_ISK
        
        if i == 24:
            csn_debt_pay_fixed = csn_debt / (30*12)
        
        if i > 24:
            amount -= csn_debt_pay_fixed
            csn_debt -= csn_debt_pay_fixed
        
        if i % 6 == 0 or i % 7 == 0 or i % 12 == 0 or i > 26:
            pass
        else:
            amount -= variables.rent
        
        if i == 26:
            amount -= variables.appartment_value

        amount_list.append(amount)
        net_worth.append(amount - csn_debt)
        csn_debt_list.append(csn_debt)

        i+=1

    df = pandas.DataFrame()
    df['Amount'] = amount_list
    df['Net_Worth'] = net_worth
    df['CSN_Debt'] = csn_debt_list

    return df

def growth_no_rent():
    amount = variables.start_amount
    csn_debt = variables.csn_debt
    i = 1
    
    amount_list = []
    net_worth = []
    csn_debt_list = []

    while i < variables.months:

        amount *= variables.roi

        # if i == 8 or i == 20:
        #     amount += variables.csn_8
        #     csn_debt += variables.csn_8
        # elif i == 9 or i == 21:
        #     amount += variables.csn_normal
        #     csn_debt += variables.csn_normal
        # elif i == 10 or i == 22:
        #     amount += variables.csn_normal
        #     csn_debt += variables.csn_normal
        # elif i == 11 or i == 23:
        #     amount += variables.csn_normal
        #     csn_debt += variables.csn_normal
        # elif i == 12 or i == 24:
        #     amount += variables.csn_12
        #     csn_debt += variables.csn_12
        # elif i == 1 or i == 13:
        #     amount += variables.csn_1
        #     csn_debt += variables.csn_1
        # elif i == 2 or i == 14:
        #     amount += variables.csn_normal
        #     csn_debt += variables.csn_normal
        # elif i == 3 or i == 15:
        #     amount += variables.csn_normal
        #     csn_debt += variables.csn_normal
        # elif i == 4 or i == 16:
        #     amount += variables.csn_normal
        #     csn_debt += variables.csn_normal
        # elif i == 5 or i == 17:
        #     amount += variables.csn_5
        #     csn_debt += variables.csn_5

        if i % 12 == 0:
            csn_debt *= variables.csn_intrest
            amount *= 1 - variables.tax_ISK
        
        if i == 24:
            csn_debt_pay_fixed = csn_debt / (30*12)
        
        if i > 24:
            amount -= csn_debt_pay_fixed
            csn_debt -= csn_debt_pay_fixed

        if i == 26:
            amount -= variables.appartment_value

        amount_list.append(amount)
        net_worth.append(amount - csn_debt)

        i+=1

    df = pandas.DataFrame()
    df['Amount'] = amount_list
    df['Net_Worth'] = net_worth

    return df

def compare(dataframe_no_rent, dataframe_rent):
    no_rent = list(dataframe_no_rent.Net_Worth)
    rent = list(dataframe_rent.Net_Worth)
    i=0
    
    while i < len(rent):
        if no_rent[i] < rent[i]:
            print(i)
            break

        i+=1

def main():
    MONTHS = get_months()

    DATFRAME_NO_RENT = growth_no_rent()
    DATFRAME_RENT = growth_with_rent()

    compare(DATFRAME_NO_RENT, DATFRAME_RENT)

    plot_graph(MONTHS, DATFRAME_NO_RENT, DATFRAME_RENT)

if __name__ == '__main__':
    main()
