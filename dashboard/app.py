import dash 
from dash import html, Input, Output, callback, dcc
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('../data/bank_transactions_cleaned.csv')

df = df.sample(frac=0.1, random_state=1)

fig1 = px.scatter(data_frame=df,
                 x='CustAccountBalance',
                 y='TransactionAmount',
                 color='BalanceTransactionCluster',
                 title='Customer Account Balance vs Transaction Amount Cluster',
                 labels={'CustAccountBalance': 'Customer Account Balance', 'TransactionAmount': 'Transaction Amount', 'BalanceTransactionCluster': 'Cluster'})
fig1.update_xaxes(range=[0, 2_000_000])

fig2 = px.bar(data_frame=df,
              x='CustGender',
              y='TransactionAmount', 
              color='CustGender',
              title='Count of Transactions by The Gender of the Customer',
              labels={'CustGender': 'Customre Gender', 'TransactionAmount': 'Transaction Amount'})

fig3 = px.box(df, 
              x='AgeRatioCluster', 
              y='UtilizationRatio', 
              title="Utilization Ratio by Age Cluster",
              labels={'AgeRatioCluster': 'Age Ration Cluster', 'UtilizationRatio': 'Utilization Ratio'})

fig4 = px.imshow(
                    df[['CustAccountBalance', 'TransactionAmount', 'Age', 'UtilizationRatio']].corr(),
                    text_auto=True, 
                    title="Feature Correlation Heatmap",
                    labels={'value': 'Correlation Coefficient'})

fig5 = px.scatter(df, 
                  x='Age', 
                  y='UtilizationRatio', 
                  color='AgeRatioCluster', 
                  title='The Age vs Utilization Ratio Cluster',
                  labels={'Age': 'Age', 'UtilizationRatio': 'Utilization Ratio'})

fig6 = px.scatter(data_frame=df,
                  x='TransactionAmount',
                  y='UtilizationRatio',
                  color='GenderTransactionCluster',
                  title='Transaction Amount vs Utilization Ratio Cluster',)

transaction_counts = df.groupby(['TransactionMonth', 'CustGender']).size().reset_index(name='TransactionCount')

fig7 = px.bar(transaction_counts, 
             x='TransactionMonth', 
             y='TransactionCount', 
             color='CustGender', 
             title='Number of Transactions by Month and Gender',
             labels={'TransactionMonth': 'Month', 'TransactionCount': 'Number of Transactions', 'CustGender': 'Gender'})

fig8 = px.scatter(df, 
                  x='CustAccountBalance', y='TransactionAmount', 
                  color='GenderTransactionCluster', size='UtilizationRatio', 
                 hover_data=['CustGender', 'Age'], title='Balance vs Transaction Amount Based Utilization Ratio')
fig8.update_xaxes(range=[0, 500000])
fig8.update_yaxes(range=[0, 100000])

fig9 = px.histogram(df, x='Age', nbins=20, title='Age Distribution of Customers')

fig10 = px.scatter(df, 
                  x='CustAccountBalance', y='TransactionAmount', 
                  color='GenderTransactionCluster', size='TransactionAmount', 
                  hover_data=['CustGender', 'Age'], title='Balance vs Transaction Amount Based on Transaction Amount')
fig10.update_xaxes(range=[0, 5000000])
fig10.update_yaxes(range=[0, 100000])

df['TransactionCount'] = df.groupby('CustGender')['TransactionAmount'].transform('count')

fig11 = px.scatter(df, 
                  x='CustAccountBalance', y='TransactionAmount', 
                  color='GenderTransactionCluster', size='TransactionCount', 
                  hover_data=['CustGender', 'Age'], title='Balance vs Transaction Amount Based on Transaction Count')

df_location = df.groupby('CustLocation')['UtilizationRatio'].mean().reset_index()

fig12 =  px.bar(
    df_location, x='CustLocation', y='UtilizationRatio', 
    title='Average Utilization Ratio by Location',
    labels={'CustLocation': 'Custumer Location', 'UtilizationRatio': 'Utilization Ratio'}
)
fig12.update_xaxes(tickangle=40)

fig13 = px.pie(df, names='CustGender', title='Customer Distribution by Gender', hole=0.4)

location_counts = df['CustLocation'].value_counts().reset_index()
location_counts.columns = ['CustLocation', 'Count']
total_cust_account_balance = df['CustAccountBalance'].sum()
total_transaction_amount = df['TransactionAmount'].sum()

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        html.H1('Bank Transactions Dashboard'),

    html.Div([
        html.Div([
            html.P('Number of Locations with High Transactions:', style={'font-size': '18px'}),
            html.H4(f"{location_counts.shape[0]:,}".replace(",", "_"))
        ], style={
            'border': '1px solid #ddd', 
            'padding': '20px', 
            'backgroundColor': '#ffffff', 
            'borderRadius': '15px', 
            'margin': '10px',
            'flex': '1'
        }),

        html.Div([
            html.P('Total Account Balance of The Customer :', style={'font-size': '18px'}),
            html.H4(f"{total_cust_account_balance:,.2f}".replace(",", "_"))
        ], style={
            'border': '1px solid #ddd', 
            'padding': '20px', 
            'backgroundColor': '#ffffff', 
            'borderRadius': '15px', 
            'margin': '10px',
            'flex': '1'
        }),

        html.Div([
            html.P('Total Transaction Amount Done by Customer:', style={'font-size': '18px'}),
            html.H4(f"{total_transaction_amount:,.2f}".replace(",", "_"))
        ], style={
            'border': '1px solid #ddd', 
            'padding': '20px', 
            'backgroundColor': '#ffffff', 
            'borderRadius': '15px', 
            'margin': '10px',
            'flex': '1'
        }),

        html.Div([
            html.P('Maximum Customer Account Balance:', style={'font-size': '18px'}),
            html.H4(f"{df['CustAccountBalance'].max():,.2f}".replace(",", "_"))
        ], style={
            'border': '1px solid #ddd', 
            'padding': '20px', 
            'backgroundColor': '#ffffff', 
            'borderRadius': '15px', 
            'margin': '10px',
            'flex': '1'
        }),
        
    ], style={'display': 'flex', 'gap': '20px', 'marginBottom': '30px'}),

        html.Div([
            html.Div([
                dcc.Tabs(
                    id='tabs',
                    value='Tab 1',
                    children=[
                        dcc.Tab(label='The Fisrt cluster', 
                                value='Tab 1',
                                children=[
                                    dcc.Graph(id='scatter3-plot',figure=fig1, config={'displayModeBar': False}),
                                ]),
                        dcc.Tab(label='The Second Cluster', 
                                value='Tab 2',
                                children=[
                                    dcc.Graph(id='scatter4-plot', figure=fig5, config={'displayModeBar': False}),
                                ]),
                        dcc.Tab(label='The Third Cluster', 
                                value='Tab 3',
                                children=[
                                    dcc.Graph(id='last1-plot', figure=fig6, config={'displayModeBar': False}),
                                ]),
                    ],
                ),

                html.Div(id='tabs-content'),
                
                html.Div([
                    dcc.Slider(
                    id='month-slider-tab',
                    min=df['TransactionMonth'].min(),
                    max=df['TransactionMonth'].max(),
                    step=1,
                    value=df['TransactionMonth'].min(),
                    marks={i: f'Month {i}' for i in range(df['TransactionMonth'].min(), df['TransactionMonth'].max() + 1)},
                    tooltip={"placement": "top", "always_visible": False},
                ),
                ], style={'width': '100%'})

        ], style={'width': '50%'}),

            html.Div([
                dcc.Tabs(
                    id='tabs2',
                    value='Tab 4',
                    children=[
                        dcc.Tab(label='Utilization Ratio', 
                                value='Tab 4',
                                children=[
                                    dcc.Graph(id='bar-plot-tab2', figure=fig8, config={'displayModeBar': False}),
                                ]),
                        dcc.Tab(label='Transaction Amount', 
                                value='Tab 5',
                                children=[
                                    dcc.Graph(id='box-plot-tab2', figure=fig10, config={'displayModeBar': False}),
                                ]),
                        dcc.Tab(label='Transaction Count', 
                                value='Tab 6',
                                children=[
                                    dcc.Graph(id='heatmap-plot-tab2', figure=fig11, config={'displayModeBar': False}),
                                ]),
                    ],
                ),
                
                html.Div([
                    dcc.Slider(
                    id='month-slider-tab-second',
                    min=df['TransactionMonth'].min(),
                    max=df['TransactionMonth'].max(),
                    step=1,
                    value=df['TransactionMonth'].min(),
                    marks={i: f'Month {i}' for i in range(df['TransactionMonth'].min(), df['TransactionMonth'].max() + 1)},
                    tooltip={"placement": "top", "always_visible": False},
                ),
                ], style={'width': '100%'})

            ], style={'width': '50%'}),

        ], style={'display': 'flex', 'gap': '10px'}),


        html.Div([
                html.Div([
                    dcc.Graph(id='scatter-plot',figure=fig7, config={'displayModeBar': False}),
                ], style={'width': '50%'}),

                html.Div([
                    dcc.Graph(id='scatter2-plot', figure=fig9, config={'displayModeBar': False}),
            ], style={'width': '60%'}),

        ], style={'display': 'flex', 'gap': '10px'}),

        html.Div([
            html.Div([
                dcc.Graph(id='pie-plot', figure=fig13, config={'displayModeBar': False}),
            ], style={'width': '30%'}),

            html.Div([
                dcc.Graph(id='heatmap-plot', figure=fig12, config={'displayModeBar': False}),
            ], style={'width': '70%'}),

        ], style={'display': 'flex', 'gap': '10px'}),

    ], style={'width': '90%'}),
], style={'width': '100%', 'display': 'flex', 'justifyContent': 'center', 'gap': '20px'})

@callback(
    [Output('scatter3-plot', 'figure'),
    Output('scatter4-plot', 'figure'),
    Output('last1-plot', 'figure'),
    Output('bar-plot-tab2', 'figure'),
    Output('box-plot-tab2', 'figure'),
    Output('heatmap-plot-tab2', 'figure')],
    [Input('month-slider-tab', 'value'),
    Input('month-slider-tab-second', 'value')]
)
def update_graph(selected_month_tab, month_slider_tab_second):
    filtered_df_tab = df[df['TransactionMonth'] == selected_month_tab]
    filtered_df_tab_second = df[df['TransactionMonth'] == month_slider_tab_second]

    fig1 = px.scatter(data_frame=filtered_df_tab,
                 x='CustAccountBalance',
                 y='TransactionAmount',
                 color='BalanceTransactionCluster',
                 title=f'Customer Account Balance vs Transaction Amount Cluster For Month {selected_month_tab}',
                 labels={'CustAccountBalance': 'Customer Account Balance', 'TransactionAmount': 'Transaction Amount', 'BalanceTransactionCluster': 'Cluster'})

    fig5 = px.scatter(filtered_df_tab, 
                  x='Age', 
                  y='UtilizationRatio', 
                  color='AgeRatioCluster', 
                  title=f'The Age vs Utilization Ratio Cluster For Month {selected_month_tab}',
                  labels={'Age': 'Age', 'UtilizationRatio': 'Utilization Ratio', 'AgeRatioCluster': 'Cluster'})
    
    fig6 = px.scatter(data_frame=filtered_df_tab,
                  x='TransactionAmount',
                  y='UtilizationRatio',
                  color='GenderTransactionCluster',
                  title=f'Transaction Amount vs Utilization Ratio Cluster For Month {selected_month_tab}',
                  labels={'TransactionAmount': 'Transaction Amount', 'UtilizationRatio': 'Utilization Ratio', 'GenderTransactionCluster': 'Cluster'})
    
    fig8 = px.scatter(filtered_df_tab_second, 
                  x='CustAccountBalance', y='TransactionAmount', 
                  color='GenderTransactionCluster', size='UtilizationRatio', 
                 hover_data=['CustGender', 'Age'], title=f'Balance vs Transaction Amount Based Utilization Ratio For Month {month_slider_tab_second}',
                 labels={'CustAccountBalance': 'Customer Account Balance', 'TransactionAmount': 'Transaction Amount', 'GenderTransactionCluster': 'Cluster'})

    fig10 = px.scatter(filtered_df_tab_second, 
                  x='CustAccountBalance', y='TransactionAmount', 
                  color='GenderTransactionCluster', size='TransactionAmount', 
                  hover_data=['CustGender', 'Age'], title=f'Balance vs Transaction Amount Based on Transaction Amount For Month {month_slider_tab_second}',
                  labels={'CustAccountBalance': 'Customer Account Balance', 'TransactionAmount': 'Transaction Amount', 'GenderTransactionCluster': 'Cluster'})

    fig11 = px.scatter(filtered_df_tab_second, 
                  x='CustAccountBalance', y='TransactionAmount', 
                  color='GenderTransactionCluster', size='TransactionCount', 
                  hover_data=['CustGender', 'Age'], title=f'Balance vs Transaction Amount Based on Transaction Count For Month {month_slider_tab_second}',
                  labels={'CustAccountBalance': 'Customer Account Balance', 'TransactionAmount': 'Transaction Amount', 'GenderTransactionCluster': 'Cluster'})

    return [fig1, fig5, fig6, fig8, fig10, fig11]


if __name__ == '__main__':
    app.run_server(debug=True)