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
    tax_AF_list, tax_ISK_list, amount_AF_list, amount_ISK_list = ISK_AF(LENGTH)
    plot_graph(MONTHS, tax_AF_list, tax_ISK_list, amount_AF_list, amount_ISK_list)

if __name__ == '__main__':
    main()
