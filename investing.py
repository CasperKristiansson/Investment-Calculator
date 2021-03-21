import plotly.graph_objects as go

def get_months(months_length):
    i = 0
    months = []

    while i < months_length:
        months.append(i)
        i+=1

    return months

def plot_graph(months, data_with_rent, data_without_rent, acctual_value, acctual_value_rent, rent, data_adjust_rent, acctual_adjust, adjust_rent):
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=months, y=data_with_rent,
                    mode='lines+markers',
                    name='With Rent'))
    
    fig.add_trace(go.Scatter(x=months, y=data_without_rent,
                    mode='lines+markers',
                    name='Without Rent'))

    fig.add_trace(go.Scatter(x=months, y=acctual_value,
                    mode='lines+markers',
                    name='Acctual Value No Rent'))

    fig.add_trace(go.Scatter(x=months, y=acctual_value_rent,
                    mode='lines+markers',
                    name='Acctual Value Rent'))
    
    fig.add_trace(go.Scatter(x=months, y=rent,
                    mode='lines+markers',
                    name='Rent'))

    fig.show()

    fig2 = go.Figure()

    fig2.add_trace(go.Scatter(x=months, y=data_adjust_rent,
                    mode='lines+markers',
                    name='Acctual Value Adjusted Rent'))

    fig2.add_trace(go.Scatter(x=months, y=acctual_adjust,
                    mode='lines+markers',
                    name='Acctual Value'))
    
    fig2.add_trace(go.Scatter(x=months, y=adjust_rent,
                    mode='lines+markers',
                    name='New Rent'))
    
    fig2.show()

def growth_with_rent(months_length):
    data_exponential = []
    acctual_value = []
    rent_data = []
    i = 0
    j = 0
    start_amount = 6315.167     # 75782/år = 6315.167kr/mån
    current_amount = 0
    exponential_growth = 1.01
    rent = 2250                 # 27000kr/år = 2250kr/mån
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
    j = 0
    start_amount = 6315.167     # 75782/år = 6315.167kr/mån
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
    j = 0
    start_amount = 6315.167     # 75782/år = 6315.167kr/mån
    current_amount = 0
    exponential_growth = 1.01
    rent = 2250                 # 27000kr/år = 2250kr/mån
    adjustment = 0
    last_amount = 6315.167
    total_rent = 0

    while i < months_length:
        if i < 36:
            adjustment += start_amount
        elif i == 36:
            start_amount = 0
            rent = 0

        current_amount = current_amount*exponential_growth + start_amount
        change_amount = (current_amount - last_amount) * 0.2

        current_amount -= change_amount
        total_rent += change_amount

        data_exponential.append(current_amount)
        acctual_value.append(current_amount - adjustment)
        rent_data.append(total_rent)

        i+=1

        last_amount = current_amount

    return data_exponential, acctual_value, rent_data

def main():
    LENGTH = 36
    MONTHS = get_months(LENGTH)
    DATA_WITH_RENT, ACCTUAL_VALUE_RENT, RENT = growth_with_rent(LENGTH)
    DATA_WITHOUT_RENT, ACCTUAL_VALUE = growth_without_rent(LENGTH)
    DATA_ADJUST_RENT, ACCTUAL_ADJUST, ADJUST_RENT = adjust_winnings(LENGTH)
    plot_graph(MONTHS, DATA_WITH_RENT, DATA_WITHOUT_RENT, ACCTUAL_VALUE, ACCTUAL_VALUE_RENT, RENT, DATA_ADJUST_RENT, ACCTUAL_ADJUST, ADJUST_RENT)

if __name__ == '__main__':
    main()
