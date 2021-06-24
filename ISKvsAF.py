import plotly.graph_objects as go
import amount
import variables
import ad_calculator

def get_months():
    i = 0
    months = []

    while i < variables.months:
        months.append(i)
        i+=1

    return months

def plot_graph(months, tax_AF_list, tax_ISK_list, amount_AF_list, amount_ISK_list, amount_AF_EndTax_List):
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
    
    fig.add_trace(go.Scatter(x=months, y=amount_AF_EndTax_List,
                    mode='lines+markers',
                    name='AF End Tax'))

    fig.show()

def isk_calculator():
    amount_ISK = amount.money
    tax_ISK = 0
    i = 0

    amount_ISK_list = []
    tax_ISK_list = []

    while i < variables.months:

        if i % 12 == 0:
            current_tax = amount_ISK * variables.roi * variables.tax_ISK
        else:
            current_tax = 0

        tax_ISK += current_tax
        amount_ISK = amount_ISK * variables.roi - current_tax

        tax_ISK_list.append(tax_ISK)
        amount_ISK_list.append(amount_ISK)

        i+=1
    
    return tax_ISK_list, amount_ISK_list

def af_calculator():
    amount_AF = amount.money
    amount_AF_EndTax = amount.money
    tax_AF = 0
    i = 0
    
    tax_AF_list = []
    amount_AF_list = []
    amount_AF_EndTax_List = []
    
    while i < variables.months:

        current_tax = (amount_AF * variables.roi - amount_AF) * variables.tax_AF
        tax_AF += current_tax
        amount_AF = amount_AF * variables.roi - current_tax
        amount_AF_EndTax = amount_AF_EndTax * variables.roi

        tax_AF_list.append(tax_AF)
        amount_AF_list.append(amount_AF)
        amount_AF_EndTax_List.append(amount_AF_EndTax)

        i+=1
    
    amount_AF_EndTax_List[-1] = amount_AF_EndTax_List[-1] - ((amount_AF_EndTax_List[-1] - amount.money) * variables.tax_AF)

    return tax_AF_list, amount_AF_list, amount_AF_EndTax_List

def main():
    MONTHS = get_months()
    TAX_AF_LIST, AMOUNT_AF_LIST, AMOUNT_AF_ENDTAX_LIST = af_calculator()
    TAX_ISK_LIST, AMOUNT_ISK_LIST = isk_calculator()
    plot_graph(MONTHS, TAX_AF_LIST, TAX_ISK_LIST, AMOUNT_AF_LIST, AMOUNT_ISK_LIST, AMOUNT_AF_ENDTAX_LIST)

if __name__ == '__main__':
    main()
