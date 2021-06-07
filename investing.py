import plotly.graph_objects as go
import amount
import variables

def get_months(months_length):
    i = 0
    months = []

    while i < variables.months:
        months.append(i)
        i+=1

    return months

def plot_graph(months):
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

def growth_with_rent():
    start_amount = variables.csn
    rent = amount.rent  
    current_amount = 0
    adjustment = 0
    i = 0

    data_exponential = []
    acctual_value = []
    rent_data = []

    while i < variables.months:
        current_amount = current_amount * variables.roi + start_amount - rent
        data_exponential.append(current_amount)

        if i < variables.csn_length:
            adjustment += start_amount

        elif i == variables.csn_length:
            start_amount = 0
            rent = 0

        acctual_value.append(current_amount - adjustment)
        rent_data.append((-rent*(i+1)))

        i+=1

    return data_exponential, acctual_value, rent_data

def growth_without_rent():
    start_amount = variables.csn
    exponential_growth = variables.roi
    adjustment = 0
    current_amount = 0
    i = 0

    data_exponential = []
    acctual_value = []

    while i < variables.months:
        current_amount = current_amount*exponential_growth + start_amount
        data_exponential.append(current_amount)

        if i < variables.csn_length:
            adjustment += start_amount
        elif i == variables.csn_length:
            start_amount = 0

        acctual_value.append(current_amount - adjustment)

        i+=1

    return data_exponential, acctual_value

def adjust_winnings():
    exponential_growth = variables.roi
    start_amount = variables.csn
    current_amount = 0
    adjustment = 0
    last_amount = 0
    total_rent = 0
    i = 0

    data_exponential = []
    acctual_value = []
    rent_data = []

    while i < variables.months:
        if i < variables.csn_length:
            adjustment += start_amount
        elif i == variables.csn_length:
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

def main():
    MONTHS = get_months()
    #DATA_WITH_RENT, ACCTUAL_VALUE_RENT, RENT = growth_with_rent()
    #DATA_WITHOUT_RENT, ACCTUAL_VALUE = growth_without_rent()
    #DATA_ADJUST_RENT, ACCTUAL_ADJUST, ADJUST_RENT = adjust_winnings()
    plot_graph(MONTHS)

if __name__ == '__main__':
    main()
