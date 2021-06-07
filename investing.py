import plotly.graph_objects as go
import amount

def get_months(months_length):
    i = 0
    months = []

    while i < months_length:
        months.append(i)
        i+=1

    return months

def plot_graph(months, tax_AF_list, tax_ISK_list, amount_AF_list, amount_ISK_list):
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=months, y=tax_AF_list,
                    mode='lines+markers',
                    name='Tax AF'))

    fig.add_trace(go.Scatter(x=months, y=tax_ISK_list,
                    mode='lines+markers',
                    name='Tax ISK'))

    fig.add_trace(go.Scatter(x=months, y=amount_AF_list,
                    mode='lines+markers',
                    name='AF'))

    fig.add_trace(go.Scatter(x=months, y=amount_ISK_list,
                    mode='lines+markers',
                    name='ISK'))

    fig.show()
    # fig2 = go.Figure()

    # fig2.add_trace(go.Scatter(x=months, y=data_adjust_rent,
    #                 mode='lines+markers',
    #                 name='Acctual Value Adjusted Rent'))

    # fig2.add_trace(go.Scatter(x=months, y=acctual_adjust,
    #                 mode='lines+markers',
    #                 name='Acctual Value'))

    # fig2.add_trace(go.Scatter(x=months, y=adjust_rent,
    #                 mode='lines+markers',
    #                 name='New Rent'))

    # fig2.show()

def growth_with_rent(months_length):
    data_exponential = []
    acctual_value = []
    rent_data = []
    i = 0
    start_amount = 6315.167     # 75782/år = 6315.167kr/mån (CSN)
    current_amount = 0
    exponential_growth = 1.01
    rent = amount.rent                 # 27000kr/år = 2250kr/mån
    adjustment = 0

    while i < months_length:
        current_amount = current_amount*exponential_growth + start_amount - rent
        data_exponential.append(current_amount)

        if i < 36:
            adjustment += start_amount
        elif i == 36:
            start_amount = 0
            rent = 0
        acctual_value.append(current_amount - adjustment)

        rent_data.append((-rent*(i+1)))

        i+=1

    return data_exponential, acctual_value, rent_data

def growth_without_rent(months_length):
    data_exponential = []
    acctual_value = []
    i = 0
    start_amount = 6315.167     # 75782/år = 6315.167kr/mån (CSN)
    current_amount = 0
    exponential_growth = 1.01
    adjustment = 0

    while i < months_length:
        current_amount = current_amount*exponential_growth + start_amount
        data_exponential.append(current_amount)

        if i < 36:
            adjustment += start_amount
        elif i == 36:
            start_amount = 0

        acctual_value.append(current_amount - adjustment)

        i+=1

    return data_exponential, acctual_value

def adjust_winnings(months_length):
    data_exponential = []
    acctual_value = []
    rent_data = []
    i = 0
    start_amount = 6315.167     # 75782/år = 6315.167kr/mån (CSN)
    current_amount = 0
    exponential_growth = 1.01   # 27000kr/år = 2250kr/mån
    adjustment = 0
    last_amount = 0
    total_rent = 0

    while i < months_length:
        if i < 36:
            adjustment += start_amount
        elif i == 36:
            start_amount = 0

        current_amount *= exponential_growth
        change_amount = (current_amount - last_amount) * 0.2
        current_amount += start_amount
        current_amount -= change_amount
        total_rent += change_amount

        data_exponential.append(current_amount)
        acctual_value.append(current_amount - adjustment)
        rent_data.append(total_rent)

        i+=1

        last_amount = current_amount

    return data_exponential, acctual_value, rent_data

def ISK_AF(length_month):

    i = 0
    amount_ISK = amount.money
    amount_AF = amount.money
    tax_AF = 0
    tax_ISK = 0
    avkastning = 1.20

    tax_AF_list = []
    tax_ISK_list = []
    amount_AF_list = []
    amount_ISK_list = []

    while i < length_month:
        tax_AF += (amount_AF * avkastning - amount_AF) * 0.3
        tax_ISK += amount_ISK * avkastning * 0.00375

        amount_AF = amount_AF * 1.12 - (amount_AF * 1.12 - amount_AF) * 0.3
        #amount_AF *= avkastning
        amount_ISK = amount_ISK * avkastning - amount_ISK * avkastning * 0.00375

        tax_AF_list.append(tax_AF)
        tax_ISK_list.append(tax_ISK)
        amount_AF_list.append(amount_AF)
        amount_ISK_list.append(amount_ISK)

        i+=1
    
    #amount_AF_list[-1] = amount_AF - tax_AF
    
    print(round(amount_ISK_list[-1] / amount_AF_list[-1] - 1, 3))

    return tax_AF_list, tax_ISK_list, amount_AF_list, amount_ISK_list

def main():
    LENGTH = 15
    MONTHS = get_months(LENGTH)
    #DATA_WITH_RENT, ACCTUAL_VALUE_RENT, RENT = growth_with_rent(LENGTH)
    #DATA_WITHOUT_RENT, ACCTUAL_VALUE = growth_without_rent(LENGTH)
    #DATA_ADJUST_RENT, ACCTUAL_ADJUST, ADJUST_RENT = adjust_winnings(LENGTH)
    tax_AF_list, tax_ISK_list, amount_AF_list, amount_ISK_list = ISK_AF(LENGTH)
    plot_graph(MONTHS, tax_AF_list, tax_ISK_list, amount_AF_list, amount_ISK_list)

if __name__ == '__main__':
    main()
