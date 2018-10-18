class DataTransformer:
    @staticmethod
    def parse_deck(cabin):
        if cabin is not None:
            cabin_str = str(cabin)
            if cabin_str != 'nan':
                return cabin_str[0]
            else:
                # print(cabin)
                return 'NaN'
        else:
            return 'NaN'

    @staticmethod
    def generate_decks_data(row, empty_df):
        deck = DataTransformer.parse_deck(row['Cabin'])
        empty_entry = {deck: 1, 'PassengerId': row['PassengerId']}
        return empty_df.append(empty_entry, ignore_index=True).iloc[0]

