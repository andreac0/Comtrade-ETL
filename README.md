# Comtrade-ETL
 Python module for ETL and automatic data preprocessing of trade data from Comtrade


## Functions available

- _comtrade.hs_list(HSlist)_: this function processes the HS list of codes provided by the United Nations, with titles and detailed descriptions, and returns the keywords for each HS6 code. It can be passed to the __keyword_search_ function. It is useful in case a new update of HS codes occur.

- _comtrade.keyword_search(hs_keyword,user_keywords)_: This function gets the output of the previous function and a list of user-defined keywords, which are preprocessed and matched against the hs_keywords. It returns a list of HS codes that have a desired keyword.

- _comtrade.get_data(period, commodity_code, trade_type, frequency, flow_code, comtradeAPIKey, name_output)_: This is the main function of the module, as it retrieves the data from Comtrade database, allowing users to choose the desired interval (_period_), the commodity_code(s), the trade_type, the frequency, the direction of the trade flow (_flow_code_). It needs also a personal Comtrade API Key and the name of the file it will be generated.

- _comtrade.analyse_reporting(df)_: compute summary statistics on the dataframe obtained with the _get_data_ function

- _comtrade.integrate_trade_data(df, period)_: it applies the data integration techniques, outlined in the paper _"Extending network tools to explore trends in temporal granular trade networks"_ presented at CompleNet2024.
