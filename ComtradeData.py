import urllib.request, json
import pandas as pd
import time
import country_converter as coco
from gensim.utils import deaccent
from gensim.parsing.preprocessing import preprocess_string, strip_tags
from gensim.parsing.preprocessing import remove_stopwords, strip_punctuation

class comtrade:

    def get_country_code(self):
 
        country_list = [{'Code': 826, 'Label': 'United Kingdom'},
        {'Code': 4, 'Label': 'Afghanistan'},
        {'Code': 8, 'Label': 'Albania'},
        {'Code': 12, 'Label': 'Algeria'},
        {'Code': 16, 'Label': 'American Samoa'},
        {'Code': 20, 'Label': 'Andorra'},
        {'Code': 24, 'Label': 'Angola'},
        {'Code': 28, 'Label': 'Antigua and Barbuda'},
        {'Code': 31, 'Label': 'Azerbaijan'},
        {'Code': 32, 'Label': 'Argentina'},
        {'Code': 36, 'Label': 'Australia'},
        {'Code': 40, 'Label': 'Austria'},
        {'Code': 44, 'Label': 'Bahamas'},
        {'Code': 48, 'Label': 'Bahrain'},
        {'Code': 50, 'Label': 'Bangladesh'},
        {'Code': 51, 'Label': 'Armenia'},
        {'Code': 52, 'Label': 'Barbados'},
        {'Code': 56, 'Label': 'Belgium'},
        {'Code': 60, 'Label': 'Bermuda'},
        {'Code': 64, 'Label': 'Bhutan'},
        {'Code': 68, 'Label': 'Bolivia (Plurinational State of)'},
        {'Code': 70, 'Label': 'Bosnia and Herzegovina'},
        {'Code': 72, 'Label': 'Botswana'},
        {'Code': 74, 'Label': 'Bouvet Island'},
        {'Code': 76, 'Label': 'Brazil'},
        {'Code': 80, 'Label': 'British Antarctic Territory'},
        {'Code': 84, 'Label': 'Belize'},
        {'Code': 86, 'Label': 'British Indian Ocean Territory'},
        {'Code': 90, 'Label': 'Solomon Islands'},
        {'Code': 92, 'Label': 'British Virgin Islands'},
        {'Code': 96, 'Label': 'Brunei Darussalam'},
        {'Code': 100, 'Label': 'Bulgaria'},
        {'Code': 104, 'Label': 'Myanmar'},
        {'Code': 108, 'Label': 'Burundi'},
        {'Code': 112, 'Label': 'Belarus'},
        {'Code': 116, 'Label': 'Cambodia'},
        {'Code': 120, 'Label': 'Cameroon'},
        {'Code': 124, 'Label': 'Canada'},
        {'Code': 132, 'Label': 'Cabo Verde'},
        {'Code': 136, 'Label': 'Cayman Islands'},
        {'Code': 140, 'Label': 'Central African Republic'},
        {'Code': 144, 'Label': 'Sri Lanka'},
        {'Code': 148, 'Label': 'Chad'},
        {'Code': 152, 'Label': 'Chile'},
        {'Code': 156, 'Label': 'China'},
        {'Code': 158, 'Label': 'China, Taiwan Province of'},
        {'Code': 162, 'Label': 'Christmas Island'},
        {'Code': 166, 'Label': 'Cocos (Keeling) Islands'},
        {'Code': 170, 'Label': 'Colombia'},
        {'Code': 174, 'Label': 'Comoros'},
        {'Code': 178, 'Label': 'Congo'},
        {'Code': 180, 'Label': 'Congo, Dem. Rep. of the'},
        {'Code': 184, 'Label': 'Cook Islands'},
        {'Code': 188, 'Label': 'Costa Rica'},
        {'Code': 191, 'Label': 'Croatia'},
        {'Code': 192, 'Label': 'Cuba'},
        {'Code': 196, 'Label': 'Cyprus'},
        {'Code': 203, 'Label': 'Czechia'},
        {'Code': 204, 'Label': 'Benin'},
        {'Code': 208, 'Label': 'Denmark'},
        {'Code': 212, 'Label': 'Dominica'},
        {'Code': 214, 'Label': 'Dominican Republic'},
        {'Code': 218, 'Label': 'Ecuador'},
        {'Code': 222, 'Label': 'El Salvador'},
        {'Code': 226, 'Label': 'Equatorial Guinea'},
        {'Code': 231, 'Label': 'Ethiopia'},
        {'Code': 232, 'Label': 'Eritrea'},
        {'Code': 233, 'Label': 'Estonia'},
        {'Code': 234, 'Label': 'Faroe Islands'},
        {'Code': 238, 'Label': 'Falkland Islands (Malvinas)'},
        {'Code': 239, 'Label': 'South Georgia and South Sandwich Islands'},
        {'Code': 242, 'Label': 'Fiji'},
        {'Code': 246, 'Label': 'Finland'},
        {'Code': 251, 'Label': 'France'},
        {'Code': 258, 'Label': 'French Polynesia'},
        {'Code': 260, 'Label': 'French Southern Territories'},
        {'Code': 262, 'Label': 'Djibouti'},
        {'Code': 266, 'Label': 'Gabon'},
        {'Code': 268, 'Label': 'Georgia'},
        {'Code': 270, 'Label': 'Gambia'},
        {'Code': 275, 'Label': 'State of Palestine'},
        {'Code': 276, 'Label': 'Germany'},
        {'Code': 288, 'Label': 'Ghana'},
        {'Code': 292, 'Label': 'Gibraltar'},
        {'Code': 296, 'Label': 'Kiribati'},
        {'Code': 300, 'Label': 'Greece'},
        {'Code': 304, 'Label': 'Greenland'},
        {'Code': 308, 'Label': 'Grenada'},
        {'Code': 316, 'Label': 'Guam'},
        {'Code': 320, 'Label': 'Guatemala'},
        {'Code': 324, 'Label': 'Guinea'},
        {'Code': 328, 'Label': 'Guyana'},
        {'Code': 332, 'Label': 'Haiti'},
        {'Code': 334, 'Label': 'Heard Island and McDonald Islands'},
        {'Code': 336, 'Label': 'Holy See'},
        {'Code': 340, 'Label': 'Honduras'},
        {'Code': 344, 'Label': 'China, Hong Kong SAR'},
        {'Code': 348, 'Label': 'Hungary'},
        {'Code': 352, 'Label': 'Iceland'},
        {'Code': 356, 'Label': 'India'},
        {'Code': 699, 'Label': 'India'},
        {'Code': 360, 'Label': 'Indonesia'},
        {'Code': 364, 'Label': 'Iran (Islamic Republic of)'},
        {'Code': 368, 'Label': 'Iraq'},
        {'Code': 372, 'Label': 'Ireland'},
        {'Code': 376, 'Label': 'Israel'},
        {'Code': 380, 'Label': 'Italy'},
        {'Code': 381, 'Label': 'Italy'},
        {'Code': 384, 'Label': "Côte d'Ivoire"},
        {'Code': 388, 'Label': 'Jamaica'},
        {'Code': 392, 'Label': 'Japan'},
        {'Code': 398, 'Label': 'Kazakhstan'},
        {'Code': 400, 'Label': 'Jordan'},
        {'Code': 404, 'Label': 'Kenya'},
        {'Code': 408, 'Label': "Korea, Dem. People's Rep. of"},
        {'Code': 410, 'Label': 'Korea, Republic of'},
        {'Code': 414, 'Label': 'Kuwait'},
        {'Code': 417, 'Label': 'Kyrgyzstan'},
        {'Code': 418, 'Label': "Lao People's Dem. Rep."},
        {'Code': 422, 'Label': 'Lebanon'},
        {'Code': 426, 'Label': 'Lesotho'},
        {'Code': 428, 'Label': 'Latvia'},
        {'Code': 430, 'Label': 'Liberia'},
        {'Code': 434, 'Label': 'Libya'},
        {'Code': 440, 'Label': 'Lithuania'},
        {'Code': 442, 'Label': 'Luxembourg'},
        {'Code': 446, 'Label': 'China, Macao SAR'},
        {'Code': 450, 'Label': 'Madagascar'},
        {'Code': 454, 'Label': 'Malawi'},
        {'Code': 458, 'Label': 'Malaysia'},
        {'Code': 462, 'Label': 'Maldives'},
        {'Code': 466, 'Label': 'Mali'},
        {'Code': 470, 'Label': 'Malta'},
        {'Code': 478, 'Label': 'Mauritania'},
        {'Code': 480, 'Label': 'Mauritius'},
        {'Code': 484, 'Label': 'Mexico'},
        {'Code': 496, 'Label': 'Mongolia'},
        {'Code': 498, 'Label': 'Moldova, Republic of'},
        {'Code': 499, 'Label': 'Montenegro'},
        {'Code': 500, 'Label': 'Montserrat'},
        {'Code': 504, 'Label': 'Morocco'},
        {'Code': 508, 'Label': 'Mozambique'},
        {'Code': 512, 'Label': 'Oman'},
        {'Code': 516, 'Label': 'Namibia'},
        {'Code': 520, 'Label': 'Nauru'},
        {'Code': 524, 'Label': 'Nepal'},
        {'Code': 528, 'Label': 'Netherlands'},
        {'Code': 531, 'Label': 'Curaçao'},
        {'Code': 533, 'Label': 'Aruba'},
        {'Code': 534, 'Label': 'Sint Maarten (Dutch part)'},
        {'Code': 535, 'Label': 'Bonaire, Sint Eustatius and Saba'},
        {'Code': 540, 'Label': 'New Caledonia'},
        {'Code': 548, 'Label': 'Vanuatu'},
        {'Code': 554, 'Label': 'New Zealand'},
        {'Code': 558, 'Label': 'Nicaragua'},
        {'Code': 562, 'Label': 'Niger'},
        {'Code': 566, 'Label': 'Nigeria'},
        {'Code': 570, 'Label': 'Niue'},
        {'Code': 574, 'Label': 'Norfolk Island'},
        {'Code': 579, 'Label': 'Norway'},
        {'Code': 580, 'Label': 'Northern Mariana Islands'},
        {'Code': 581, 'Label': 'United States Minor Outlying Islands'},
        {'Code': 583, 'Label': 'Micronesia (Federated States of)'},
        {'Code': 584, 'Label': 'Marshall Islands'},
        {'Code': 585, 'Label': 'Palau'},
        {'Code': 586, 'Label': 'Pakistan'},
        {'Code': 591, 'Label': 'Panama'},
        {'Code': 598, 'Label': 'Papua New Guinea'},
        {'Code': 600, 'Label': 'Paraguay'},
        {'Code': 604, 'Label': 'Peru'},
        {'Code': 608, 'Label': 'Philippines'},
        {'Code': 612, 'Label': 'Pitcairn'},
        {'Code': 616, 'Label': 'Poland'},
        {'Code': 620, 'Label': 'Portugal'},
        {'Code': 624, 'Label': 'Guinea-Bissau'},
        {'Code': 626, 'Label': 'Timor-Leste'},
        {'Code': 634, 'Label': 'Qatar'},
        {'Code': 642, 'Label': 'Romania'},
        {'Code': 643, 'Label': 'Russian Federation'},
        {'Code': 646, 'Label': 'Rwanda'},
        {'Code': 652, 'Label': 'Saint Barthélemy'},
        {'Code': 654, 'Label': 'Saint Helena'},
        {'Code': 659, 'Label': 'Saint Kitts and Nevis'},
        {'Code': 660, 'Label': 'Anguilla'},
        {'Code': 662, 'Label': 'Saint Lucia'},
        {'Code': 663, 'Label': 'Saint Martin (French part)'},
        {'Code': 666, 'Label': 'Saint Pierre and Miquelon'},
        {'Code': 670, 'Label': 'Saint Vincent and the Grenadines'},
        {'Code': 674, 'Label': 'San Marino'},
        {'Code': 678, 'Label': 'Sao Tome and Principe'},
        {'Code': 682, 'Label': 'Saudi Arabia'},
        {'Code': 686, 'Label': 'Senegal'},
        {'Code': 688, 'Label': 'Serbia'},
        {'Code': 690, 'Label': 'Seychelles'},
        {'Code': 694, 'Label': 'Sierra Leone'},
        {'Code': 702, 'Label': 'Singapore'},
        {'Code': 703, 'Label': 'Slovakia'},
        {'Code': 704, 'Label': 'Viet Nam'},
        {'Code': 705, 'Label': 'Slovenia'},
        {'Code': 706, 'Label': 'Somalia'},
        {'Code': 710, 'Label': 'South Africa'},
        {'Code': 716, 'Label': 'Zimbabwe'},
        {'Code': 724, 'Label': 'Spain'},
        {'Code': 728, 'Label': 'South Sudan'},
        {'Code': 729, 'Label': 'Sudan'},
        {'Code': 732, 'Label': 'Western Sahara'},
        {'Code': 740, 'Label': 'Suriname'},
        {'Code': 748, 'Label': 'Eswatini'},
        {'Code': 752, 'Label': 'Sweden'},
        {'Code': 757, 'Label': 'Switzerland, Liechtenstein'},
        {'Code': 760, 'Label': 'Syrian Arab Republic'},
        {'Code': 762, 'Label': 'Tajikistan'},
        {'Code': 764, 'Label': 'Thailand'},
        {'Code': 768, 'Label': 'Togo'},
        {'Code': 772, 'Label': 'Tokelau'},
        {'Code': 776, 'Label': 'Tonga'},
        {'Code': 780, 'Label': 'Trinidad and Tobago'},
        {'Code': 784, 'Label': 'United Arab Emirates'},
        {'Code': 788, 'Label': 'Tunisia'},
        {'Code': 792, 'Label': 'Türkiye'},
        {'Code': 795, 'Label': 'Turkmenistan'},
        {'Code': 796, 'Label': 'Turks and Caicos Islands'},
        {'Code': 798, 'Label': 'Tuvalu'},
        {'Code': 800, 'Label': 'Uganda'},
        {'Code': 804, 'Label': 'Ukraine'},
        {'Code': 807, 'Label': 'North Macedonia'},
        {'Code': 818, 'Label': 'Egypt'},
        {'Code': 834, 'Label': 'Tanzania, United Republic of'},
        {'Code': 842, 'Label': 'United States of America'},
        {'Code': 854, 'Label': 'Burkina Faso'},
        {'Code': 858, 'Label': 'Uruguay'},
        {'Code': 860, 'Label': 'Uzbekistan'},
        {'Code': 862, 'Label': 'Venezuela (Bolivarian Rep. of)'},
        {'Code': 876, 'Label': 'Wallis and Futuna Islands'},
        {'Code': 882, 'Label': 'Samoa'},
        {'Code': 887, 'Label': 'Yemen'},
        {'Code': 894, 'Label': 'Zambia'},
        {'Code': 460, 'Label': 'Other Asia (Taiwan)'}]

        return pd.DataFrame(country_list)
    

    def get_data(self, period, commodity_code, name_output):

        # List of countries
        countries = self.get_country_code()
        # Convert the numeric code to string
        list_codes_country = countries['Code'].astype(str).str.cat(sep=',')

        trade = pd.DataFrame(columns=['year','reporterCode','reporter','partnerCode','partner','value','flowCode', 'commodityCode'])
        
        for year in period:
            
            try:

                url = "https://comtradeapi.un.org/data/v1/get/"
                
                trade_type = "C" # commodities
                frequency = "A" # annual
                trade_classification_type = "HS" 
                reporter_code = list_codes_country
                partner_code = list_codes_country
                flow_code = "M,X"
                customs_code = "C01"

                url = url + trade_type + "/" + frequency + "/" + trade_classification_type + "?reporterCode=" + reporter_code +\
                    "&period=" + str(year) + "&partnerCode=" + partner_code + "&cmdCode=" + str(commodity_code) + "&flowCode=" + flow_code +\
                    "&customsCode=" + customs_code + "&aggregateBy=cmdCode&breakdownMode=classic&includeDesc=false"

                hdr ={
                # Request headers
                'Cache-Control': 'no-cache',
                # 'Ocp-Apim-Subscription-Key': '6e5dcb09f95d466bb29dcbd2bfb7405f',
                'Ocp-Apim-Subscription-Key': '9fd596513bdc40b58059459772916810',
                }

                req = urllib.request.Request(url, headers=hdr)
                print('Querying data for year ' + str(year) +'...')
                req.get_method = lambda: 'GET'
                X = urllib.request.urlopen(req).read()
                # response = urllib.request.urlopen(req)
                # print(response.getcode())
                print('Download for year ' + str(year) + ' successful!')

            except Exception as e:
                print(e)

            # Parse into pandas
            my_json = X.decode('utf8').replace("'", '"')
            data = json.loads(my_json)
            df = pd.DataFrame.from_dict(data["data"])

            # Rename columns
            df = df[['refYear','reporterCode', 'primaryValue','partnerCode','flowCode']].rename(columns={"refYear":"year", "primaryValue": "value"})

            # Merge with country code to add name
            newdf = df.merge(countries, left_on='reporterCode', right_on='Code').drop('Code', axis = 1).rename(columns={"Label":"reporter"})
            newdf = newdf.merge(countries, left_on='partnerCode', right_on='Code').drop('Code', axis = 1).rename(columns={"Label":"partner"})

            # Save data
            # newdf[['commodityCode']] = str(commodity_code)
            trade = pd.concat([trade, newdf[['year','reporterCode','reporter','partnerCode','partner','value','flowCode']]])
            
            time.sleep(10)

        trade.to_csv('Data/Comtrade/'+ name_output + '.csv', index=False)

        print('Data saved in path:'+' /Data/Comtrade/'+ name_output + '.csv')

    def analyse_reporting(self, df):

        # Split importers and exporters
        importers = df[df['flowCode'] == "M"].drop("flowCode", axis = 1).reset_index(drop = True).rename(columns={'value':'imp_value'})
        exporters = df[df['flowCode'] == "X"].drop("flowCode", axis = 1).reset_index(drop = True).rename(columns={'value':'exp_value'})

        # Compare the values in relative terms
        compare = importers.merge(exporters, left_on=['year','reporterCode','partnerCode'], right_on=['year','partnerCode','reporterCode'])
        compare['diff'] = (compare['imp_value']-compare['exp_value'])/compare['exp_value']
        print('Distribution of differences between values reported by importers and exporters:\n')
        print(compare['diff'].describe())

        print('N° of importers: ' + str(len(importers)))
        print('N° of exporters: ' + str(len(exporters)))
    
    def integrate_trade_data(self, df, period):

        # Split importers and exporters
        importers = df[df['flowCode'] == "M"].drop("flowCode", axis = 1).reset_index(drop = True).rename(columns={'value':'imp_value'})
        exporters = df[df['flowCode'] == "X"].drop("flowCode", axis = 1).reset_index(drop = True).rename(columns={'value':'exp_value'})

        # Compare the values in relative terms
        compare = importers.merge(exporters, left_on=['year','reporterCode','partnerCode'], right_on=['year','partnerCode','reporterCode'])
        compare['diff'] = (compare['imp_value']-compare['exp_value'])/compare['exp_value']

        # For both reports and low difference:
        similar_values = compare[abs(compare['diff']) <= 0.2][['year','reporterCode_x','reporter_x','partnerCode_x','partner_x','imp_value','exp_value']].rename(columns={'reporterCode_x':'importer', 'reporter_x':'importer_name','partnerCode_x':'exporter','partner_x':'exporter_name'})
        similar_values['value'] = (similar_values['imp_value']+similar_values['exp_value'])/2
        similar_values = similar_values[['year','importer','importer_name','exporter','exporter_name','value']]

        # For both reports and high difference:
        different_value = compare[abs(compare['diff']) > 0.2][['year','reporterCode_x','reporter_x','partnerCode_x','partner_x','imp_value']].rename(columns={'reporterCode_x':'importer','reporter_x':'importer_name' ,'partnerCode_x':'exporter', 'partner_x':'exporter_name' ,'imp_value':'value'})

        # Union data
        trades = pd.concat([similar_values,different_value])

        # finding cases when only the importer is reporting something 
        outer_join = importers.merge(trades, how = 'outer', left_on=['year','reporterCode','partnerCode'], right_on=['year','importer','exporter'] , indicator = True)
        anti_join = outer_join[outer_join['_merge'] == 'left_only']
        importers_remaining = anti_join[['year','reporterCode','partnerCode','reporter','partner','imp_value']].rename(columns={'reporterCode':'importer',\
                                                                                                        'partnerCode':'exporter',\
                                                                                                        'reporter': 'importer_name',\
                                                                                                        'partner':'exporter_name',\
                                                                                                        'imp_value':'value'})
        trades = pd.concat([trades,importers_remaining])

        # finding cases when only the exporter is reporting something
        outer_join = exporters.merge(trades, how = 'outer', left_on=['year','partnerCode','reporterCode'], right_on=['year','importer','exporter'] , indicator = True)
        anti_join = outer_join[outer_join['_merge'] == 'left_only']
        exporters_remaining = anti_join[['year','reporterCode','partnerCode','reporter','partner','exp_value']].rename(columns={'reporterCode':'exporter',\
                                                                                                        'partnerCode':'importer',\
                                                                                                        'reporter': 'exporter_name',\
                                                                                                        'partner':'importer_name',\
                                                                                                        'exp_value':'value'})
        trades = pd.concat([trades,exporters_remaining]).reset_index(drop = True)

        countries = self.get_country_code()

        # Retrieve and append ISO3 codes via COCO library (do not consider Liechtenstein as it is grouped toghether with Switzerland)
        countries['Label'] = countries['Label'].replace('Switzerland, Liechtenstein', 'Switzerland')
        countries['Label'] = countries['Label'].replace('China, Taiwan Province of', 'Taiwan ')
        countries['ISO3'] = coco.convert(countries['Label'], to = 'ISO3', not_found = None)
        trades = pd.merge(trades, countries.drop('Label', axis = 1), how='inner', left_on='importer', right_on = 'Code').drop('Code', axis = 1).rename(columns = {'ISO3':'importer_ISO3'})
        df = pd.merge(trades, countries.drop('Label', axis = 1), how='inner', left_on='exporter', right_on = 'Code').drop('Code', axis = 1).rename(columns = {'ISO3':'exporter_ISO3'})

        if len(period) > 1:
            t2 = trades.pivot_table(index=['importer','importer_name','exporter','exporter_name'], values='value', columns = 'year').reset_index()
            t2 = pd.concat([t2[['importer','importer_name','exporter','exporter_name']],t2[period].interpolate(axis = 1)], axis=1)
            t2 = t2.dropna()
            trades = pd.melt(t2, id_vars=['importer','importer_name','exporter','exporter_name'], var_name='year')

        return(df)
    
    def hs_list(self, HS):
        processing_filters = [deaccent, strip_tags, remove_stopwords]

        HS.rename(columns={'Self-explanatory texts':'contents'},inplace=True)
        HS["contents"] = HS.contents.apply(str)
        HS['cont'] = HS['contents'].copy()
        # Lower case
        HS['contents'] = HS.contents.apply(lambda x: x.lower())
        HS['contents'] = HS.contents.apply(strip_punctuation)
        # # Preprocess speech
        word_list = HS.contents.apply(lambda cont: preprocess_string(cont, processing_filters))
    
        keywords_HS = pd.DataFrame(columns=['code','keyword','Description'])
        for i in range(len(word_list)):
            for j in range(len(word_list[i])):
                d = {'code': [HS['Code.1'][i]], 'keyword': [word_list[i][j]], 'cont':[HS['cont'][i]], 'Description': [HS['Description'][i]]}
                # keywords_HS = keywords_HS.append(pd.DataFrame(d))
                keywords_HS = pd.concat([keywords_HS,pd.DataFrame(d)])

        keywords_HS = keywords_HS.reset_index(drop = True)

        return keywords_HS


    def keyword_search(self, df, keywords):

        matching_rows = []
        for i in range(len(df)):
            for keyword in keywords:
                if keyword.lower() == str(df.loc[i, 'keyword']).lower():
                    matching_rows.append(df.iloc[i])
        if matching_rows:
            return pd.DataFrame(matching_rows).reset_index(drop=True)[['code','cont','Description']].drop_duplicates()
        else:
            return pd.DataFrame(columns=df.columns)
        